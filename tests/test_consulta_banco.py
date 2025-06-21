"""Aplicação web para banco feature tests."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import os

# Desabilita verificação SSL do webdriver_manager
os.environ['WDM_SSL_VERIFY'] = '0'

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@pytest.fixture
def navegador():
    opts = Options()
    opts.headless = True
    servico = Service(ChromeDriverManager().install())
    chrome = Chrome(service=servico, options=opts)
    yield chrome
    chrome.quit()

@scenario('features/banco.feature', 'Obter o saldo das contas.')
def test_obter_o_saldo_das_contas(navegador):
    """Cenário: Obter o saldo das contas."""

@given('visito o app do banco.')
def visito_o_app_do_banco(navegador):
    navegador.get('http://127.0.0.1:5000/nova_conta')
    form = navegador.find_element(By.ID, "form_conta")
    num_conta = navegador.find_element(By.ID, "numero")
    num_conta.send_keys("111")
    saldo = navegador.find_element(By.ID, "saldo")
    saldo.send_keys("50")
    form.submit()

@when('entro com o número da conta "111".')
def entro_com_numero_da_conta(navegador):
    navegador.get('http://127.0.0.1:5000/consulta')
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "form_consulta_conta")))
    form = navegador.find_element(By.ID, "form_consulta_conta")
    num_conta = navegador.find_element(By.NAME, "numero_conta")
    num_conta.send_keys("111")
    form.submit()


@then('obtenho saldo == 50.')
def valido_saldo(navegador):
    result = navegador.find_element(By.TAG_NAME, 'p')
    assert result.text == 'Saldo: 50'
