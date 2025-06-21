# 💼 Aplicação Web de Banco com Testes Automatizados (Flask + Selenium + BDD)

Este projeto simula um sistema bancário simples com interface web feita em Flask, além de testes automatizados utilizando Selenium e `pytest-bdd`.

---

## 📁 Estrutura do Projeto

```text
.
├── app.py                     # Ponto de entrada da aplicação Flask
├── banco/
│   ├── banco.py               # Classe Banco com operações de conta
│   └── conta.py               # Classe Conta (modelo de dados)
├── pytest.ini                 # Configuração do Pytest + BDD
├── static/                    # Arquivos estáticos (CSS, JS, imagens, se houver)
├── templates/                 # HTMLs utilizados pelas rotas Flask
│   ├── form_consulta_conta.html
│   ├── form_conta.html
│   └── lista_conta.html
├── tests/
│   ├── features/
│   │   └── banco.feature      # Especificações BDD do sistema
│   └── test_consulta_banco.py # Teste automatizado com Selenium e Pytest-BDD
```

---

## 📦 Dependências do Projeto

Você pode instalar todas as dependências com:

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install flask selenium pytest pytest-bdd webdriver-manager
```

### 📋 Lista completa de bibliotecas utilizadas

- `flask` – aplicação web
- `selenium` – testes automatizados com navegador
- `pytest` – framework de testes
- `pytest-bdd` – suporte a testes no formato Gherkin
- `webdriver-manager` – gerenciamento automático do ChromeDriver
- `os` – manipulação de variáveis de ambiente e sistema (padrão do Python)
- `time` – (caso usada para delays, via `WebDriverWait`, etc.)

---

## ▶️ Como Executar a Aplicação

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 🧪 Como Rodar os Testes Automatizados

Com o servidor Flask rodando, execute em outro terminal:

```bash
pytest -v
```

---

## 🛠️ Gerar Teste BDD automaticamente (opcional)

```bash
pytest-bdd generate tests/features/banco.feature > tests/test_consulta_banco.py
```

⚠️ **Gera apenas o esqueleto do teste, você deve implementar os passos.**

---

## 🌐 Funcionalidades

- Criar nova conta bancária
- Consultar saldo por número da conta
- Listar todas as contas
- Testes automatizados com BDD (Behavior-Driven Development)

---

## 📎 Requisitos do Ambiente

- Python 3.9+
- Google Chrome instalado
- Acesso à internet (para `webdriver-manager` baixar o ChromeDriver)

---

## 🧰 Extras

- Testes rodam em **modo headless** (sem abrir o navegador)
- Código pronto para integração contínua (CI/CD)

---

Feito com ❤️ por Rafa | Desenvolvedor de sistemas e automações
