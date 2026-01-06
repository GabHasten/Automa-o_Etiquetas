import pyautogui
import time

time.sleep(2) # Dá 2 segundos para você posicionar o mouse
x, y = pyautogui.position()
print(f"Posição do mouse: x={x}, y={y}")