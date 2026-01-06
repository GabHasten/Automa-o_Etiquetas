import pyautogui
import time

# Para obter a posição atual uma vez (e imprimir no terminal)
print("Posicione o mouse onde deseja e aguarde...")
time.sleep(3) # Dá tempo para você mover o mouse
x, y = pyautogui.position()
print(f"Coordenada atual: X={x}, Y={y}")

# Ou para ver em tempo real (aperte Ctrl+C para sair)
print("\n--- Modo Interativo: Mova o mouse e veja as coordenadas ---")
print("Aperte Ctrl-C para sair.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição: X={x}, Y={y}", end='\r') # \r atualiza a linha
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nScript encerrado.")
