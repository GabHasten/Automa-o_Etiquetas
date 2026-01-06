import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# =========================================================
# DADOS FIXOS (HOJE HARDCODED)
# ---------------------------------------------------------
# ⚠️ NO FUTURO:
# Esses dados serão substituídos por dados vindos da API
# do Google Sheets (lidos em outro arquivo Python).
# =========================================================

CEP = "32670-278"
ENDERECO = "R. dos Inconfidentes"
NUMERO = "437"
NOME = "TH Gráfica"
COMPLEMENTO = "Galpão / Gráfica"
BAIRRO = "Chácaras"
CIDADE = "BETIM"

# =========================================================
# INICIALIZAÇÃO DO SELENIUM
# ---------------------------------------------------------
# Abre o Chrome e acessa o Endereçador dos Correios
# =========================================================

driver = webdriver.Chrome()
driver.get(
    "https://www2.correios.com.br/enderecador/encomendas/default.cfm?etq=1&tipo=rem#form1"
)
driver.maximize_window()

# Aguarda carregamento completo da página
time.sleep(5)

# =========================================================
# FUNÇÃO: prenchimento (REMETENTE)
# ---------------------------------------------------------
# Preenche os dados do REMETENTE nas 4 etiquetas
# Os IDs seguem o padrão: campo_1, campo_2, campo_3, campo_4
# =========================================================

def prenchimento():

    # -----------------------------------------------------
    # Função interna para fechar pop-ups (botão "X")
    # Os Correios exibem modais aleatórios durante o uso
    # -----------------------------------------------------
    def bt_fechar():
        try:
            bt_x = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/span"
            )
            bt_x.click()
        except:
            # Caso o popup não exista, ignora
            pass

    # Fecha popup inicial, se existir
    bt_fechar()

    # -----------------------------------------------------
    # Loop principal
    # Preenche as 4 etiquetas (1 a 4)
    # -----------------------------------------------------
    for i in range(1, 5):

        # CEP do remetente
        driver.find_element(By.ID, f"cep_{i}").clear()
        driver.find_element(By.ID, f"cep_{i}").send_keys(CEP)

        # Clique no endereço força o site a validar o CEP
        driver.find_element(By.ID, f"endereco_{i}").click()
        time.sleep(2)

        # Fecha possíveis pop-ups após validação do CEP
        bt_fechar()

        # Nome do remetente
        driver.find_element(By.ID, f"nome_{i}").clear()
        driver.find_element(By.ID, f"nome_{i}").send_keys(NOME)

        # Endereço
        driver.find_element(By.ID, f"endereco_{i}").clear()
        driver.find_element(By.ID, f"endereco_{i}").send_keys(ENDERECO)

        # Número
        driver.find_element(By.ID, f"numero_{i}").clear()
        driver.find_element(By.ID, f"numero_{i}").send_keys(NUMERO)

        # Complemento
        driver.find_element(By.ID, f"complemento_{i}").clear()
        driver.find_element(By.ID, f"complemento_{i}").send_keys(COMPLEMENTO)

        # Bairro
        driver.find_element(By.ID, f"bairro_{i}").clear()
        driver.find_element(By.ID, f"bairro_{i}").send_keys(BAIRRO)

        # Cidade
        driver.find_element(By.ID, f"cidade_{i}").clear()
        driver.find_element(By.ID, f"cidade_{i}").send_keys(CIDADE)

# =========================================================
# FUNÇÃO: preencher_despachante (DESTINATÁRIO FIXO)
# ---------------------------------------------------------
# O despachante é FIXO e NÃO vem da planilha
# Os IDs seguem o padrão: desCampo_1, desCampo_2, etc.
# =========================================================

def preencher_despachante():

    # Função interna para fechar pop-ups
    def bt_fechar():
        try:
            bt_x = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div/span"
            )
            bt_x.click()
        except:
            pass

    # Loop para as 4 etiquetas
    for i in range(1, 5):

        bt_fechar()

        # CEP do despachante
        driver.find_element(By.ID, f"desCep_{i}").clear()
        driver.find_element(By.ID, f"desCep_{i}").send_keys(CEP)

        # Clique para validação do CEP
        driver.find_element(By.ID, f"desEndereco_{i}").click()
        time.sleep(2)

        bt_fechar()

        # Nome
        driver.find_element(By.ID, f"desNome_{i}").clear()
        driver.find_element(By.ID, f"desNome_{i}").send_keys(NOME)

        # Endereço
        driver.find_element(By.ID, f"desEndereco_{i}").clear()
        driver.find_element(By.ID, f"desEndereco_{i}").send_keys(ENDERECO)

        # Número
        driver.find_element(By.ID, f"desNumero_{i}").clear()
        driver.find_element(By.ID, f"desNumero_{i}").send_keys(NUMERO)

        # Complemento
        driver.find_element(By.ID, f"desComplemento_{i}").clear()
        driver.find_element(By.ID, f"desComplemento_{i}").send_keys(COMPLEMENTO)

        # Bairro
        driver.find_element(By.ID, f"desBairro_{i}").clear()
        driver.find_element(By.ID, f"desBairro_{i}").send_keys(BAIRRO)

        # Cidade
        driver.find_element(By.ID, f"desCidade_{i}").clear()
        driver.find_element(By.ID, f"desCidade_{i}").send_keys(CIDADE)

        # Autorização (checkbox / radio)
        driver.find_element(By.ID, f"aut0_{i}").click()
        

# =========================================================
# EXECUÇÃO DO SCRIPT
# ---------------------------------------------------------
# Ordem correta:
# 1) Preenche remetente
# 2) Preenche despachante
# =========================================================

try:
    prenchimento()
    preencher_despachante()
    time.sleep(5)
    print("O código rodou por completo!")
except Exception as e:
    print(f"Erro ocorrido: {e}")

    #https://www.youtube.com/watch?v=6XaF4ZF7LW0