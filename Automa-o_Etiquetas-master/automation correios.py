import pyautogui
import time
import os

# ==============================================================================
# CONFIGURAÇÕES DE CAMINHO E DIRETÓRIO
# ==============================================================================
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_IMAGEM = os.path.join(DIRETORIO_ATUAL, "capturar.png")

# ==============================================================================
# FUNÇÃO: entrar()
# ==============================================================================
def entrar():
    # Abre o Menu Iniciar do Windows
    pyautogui.press('win')
    time.sleep(2)

    # Digita o nome do navegador
    pyautogui.write('chrome') # Corrigido para 'chrome'
    time.sleep(1)

    # Abre o navegador
    pyautogui.press('enter')
    time.sleep(5)

    # Seleção de perfil
    pyautogui.click(x=668, y=220)
    time.sleep(0.4)


    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

    # Navegação para o site
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.8)
    pyautogui.write('https://www2.correios.com.br/enderecador/encomendas/default.cfm')
    time.sleep(2)
    pyautogui.press('enter')

    # Aguarda o carregamento dos elementos do site
    print("Aguardando carregamento da página...")
    time.sleep(4)

    # --- PARTE DE LOCALIZAÇÃO DENTRO DA FUNÇÃO ---
    try:
        posicao = pyautogui.locateCenterOnScreen(CAMINHO_IMAGEM, confidence=0.8)
        if posicao:
            pyautogui.click(posicao)
            print(f"Botão clicado com sucesso em: {posicao}")
        else:
            print("Imagem não encontrada na tela.")
    except pyautogui.ImageNotFoundException:
        print("Erro: A imagem 'capturar.png' não foi detectada após o carregamento.")

    pyautogui.scroll(-500)

    pyautogui.click(x=501, y=376)
    time.sleep(0.5)
    pyautogui.write('32670656')
    time.sleep(3)


# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================
try:
    entrar()
    print("Processo finalizado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado no sistema: {e}")