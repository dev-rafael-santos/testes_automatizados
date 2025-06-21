from flask import Flask, render_template, request, redirect
from banco.banco import Banco
from banco.conta import Conta

app = Flask(__name__)
contas_banco = Banco()

@app.route("/")
def home():
    return '<h1>Aplicativo de banco</h1>'

@app.route("/nova_conta", methods=["GET", "POST"])
def nova_conta():
    if request.method == "POST":
        try:
            numero = request.form.get("numero")
            saldo = request.form.get("saldo")
            if not numero or not saldo:
                return "Número da conta ou saldo não informado", 400
            saldo = int(saldo)
            contas_banco.incluir_conta(Conta(numero, saldo))
            return redirect('/consulta')
        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"Erro interno: {str(e)}", 500
    return render_template("form_conta.html")


@app.route("/consulta", methods=["GET", "POST"])
def consulta():
    try:
        saldo = None
        conta_nao_encontrada = None
        if request.method == "POST":
            numero_conta = request.form.get('numero_conta')
            if numero_conta:
                try:
                    saldo = contas_banco.obter_saldo_da_conta(numero_conta)
                except:
                    conta_nao_encontrada = numero_conta
        return render_template('form_consulta_conta.html', saldo=saldo, conta_nao_encontrada=conta_nao_encontrada)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Erro interno na rota /consulta: {str(e)}", 500




@app.route("/contas")
def listar_contas():
    contas = []
    for numero, conta in contas_banco.contas.items():
        contas.append({'numero': numero, 'saldo': conta.saldo})
    contas = sorted(contas, key=lambda c: c['numero'])
    return render_template("lista_conta.html", contas=contas)

if __name__ == "__main__":
    app.run(debug=True)
