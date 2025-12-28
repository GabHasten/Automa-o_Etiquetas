import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#=============== Dados remetente ========================== #

CEP = "32670-278"
ENDERECO = "R. dos Inconfidentes - Chácaras, Betim - MG"
NUMERO = "437"
NOME = "TH Gráfica"
COMPLEMENTO = "Galpão / Gráfica"
BAIRRO = "Chácaras"
CIDADE = "BETIM"


# ========================================================= #

# Código Principal

driver = webdriver.Chrome()
driver.get("https://www2.correios.com.br/enderecador/encomendas/default.cfm?etq=1&tipo=rem#form1")
driver.maximize_window()
time.sleep(5)

# Função Principal 

def abrir_correio():

    # botão span dos correios para logar

    def bt_fechar():
        bt_x = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/span")
        bt_x.click()
        time.sleep(1)

    bt_fechar()

    # Campo CEP

    campo_cep = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div/p/span/label/input[1]")
    campo_cep.clear()
    campo_cep.send_keys(CEP)
    time.sleep(0.8)
    
    campo_endereco = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div/span[2]/label/input")
    campo_endereco.click()
    time.sleep(2)
    bt_fechar()

    # Campo ENDEREÇO

    campo_endereco = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div/span[2]/label/input")
    campo_endereco.clear()
    campo_endereco.send_keys(ENDERECO)
    time.sleep(1)

    # campo NÚMERO

    campo_numero = driver.find_element(By.XPATH, "//*[@id='numero_1']")
    campo_numero.clear()
    campo_numero.send_keys(NUMERO)
    time.sleep(1)

    # campo NOME

    campo_nome = driver.find_element(By.XPATH, "//*[@id='nome_1']")
    campo_nome.clear()
    campo_nome.send_keys(NOME)

    # campo COMPLEMENTO
    
    campo_complemento = driver.find_element(By.XPATH, "//*[@id='complemento_1']")
    campo_complemento.clear()
    campo_complemento.send_keys(COMPLEMENTO)
    time.sleep(1)    

    # campo BAIRRO

    campo_bairro = driver.find_element(By.XPATH, "//*[@id='bairro_1']")
    campo_bairro.clear()
    campo_bairro.send_keys(BAIRRO)
    time.sleep(1)    

    # campo CIDADE

    campo_cidade = driver.find_element(By.XPATH, "//*[@id='cidade_1']")
    campo_cidade.clear()
    campo_cidade.send_keys(CIDADE)
    time.sleep(1)

    # 1. seleciona campo UF
    campo_uf = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div/span[8]/label/select")

    # 2. Instancia o objeto Select
    select_uf = campo_uf.find_elements(By.TAG_NAME,"MG")

    # 3. Seleciona uma opção
    for MG in select_uf:
        print("'O valor é: ")

    
    time.sleep(1)


    time.sleep(5)



try:
    abrir_correio()
    print("O código rodou por completo !")
except Exception as e:
    print(f"Erro ocorrido: {e}")