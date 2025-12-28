import pyautogui
import time

def limpar_temp():
    try:
        # Configura o comportamento do PyAutoGUI
        # - FAILSAFE: mova o cursor até o canto da tela para abortar o script caso algo dê errado
        # - PAUSE: pausa entre as chamadas de PyAutoGUI para tornar a automação mais estável
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

        # #abre arquivos temporarios
        # Abre a caixa de execução do Windows (Win+R) para invocar o comando de abrir o diretório temporário
        pyautogui.hotkey('win','r')
        time.sleep(0.5)

        # Digita o caminho do diretório temporário usando a variável de ambiente %temp%
        pyautogui.write('%temp%')
        # Executa o comando para abrir o diretório temporário
        pyautogui.press('enter')

        # Aguarda o diretório abrir
        time.sleep(3.5)

        # #seleciona tudo e apaga
        # Clica em uma posição fixa na tela que deve corresponder ao conteúdo do diretório aberto
        pyautogui.click(400, 300)

        # Seleciona todo o conteúdo dentro do diretório (Ctrl+A)
        pyautogui.hotkey('ctrl','a')
        time.sleep(0.5)

        # Deleta o conteúdo selecionado
        pyautogui.press('delete')
        time.sleep(0.5)

        # Confirma a ação, se necessário (dependendo do sistema/diálogo)
        pyautogui.press('enter')

        # Mensagem de sucesso
        print("Limpeza de temporários concluída com sucesso.")
    except Exception as e:
        # Tratamento de exceção: exibe a mensagem de erro encontrada durante a execução
        print(f"Erro ao limpar os arquivos temporários: {e}")

# Execução do script apenas quando executado diretamente (não quando importado)
if __name__ == "__main__":

    limpar_temp()