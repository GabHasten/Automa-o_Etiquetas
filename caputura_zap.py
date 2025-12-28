import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ARQUIVO_SAIDA = "dados_cliente.txt"

# ======================================================
# EXTRAÇÃO + VALIDAÇÃO
# ======================================================
def extrair_dados(texto_original: str):
    texto = texto_original.lower()

    # -------- CEP --------
    cep_match = re.findall(r"\b\d{8}\b", texto)
    cep = cep_match[0] if cep_match else None

    # -------- TELEFONE --------
    tel_match = re.findall(r"\b\d{10,11}\b", texto)
    telefone = tel_match[0] if tel_match else None

    # -------- ENDEREÇO --------
    endereco = None
    palavras_rua = ["rua", "avenida", "av", "travessa", "tv", "alameda", "estrada"]
    for linha in texto.split("\n"):
        if any(p in linha for p in palavras_rua):
            endereco = linha.strip()
            break

    # -------- NÚMERO --------
    numero = None
    nums = re.findall(r"\b\d{1,5}\b", texto)
    for n in nums:
        if cep and n != cep:
            numero = n
            break

    # -------- NOME (heurística simples) --------
    nome = None
    palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", texto_original)
    if len(palavras) >= 2:
        nome = f"{palavras[0]} {palavras[1]}".title()

    # -------- VALIDAÇÃO FINAL --------
    if cep and endereco and numero:
        return {
            "nome": nome,
            "cep": cep,
            "endereco": endereco,
            "numero": numero,
            "telefone": telefone
        }

    return None

# ======================================================
# SALVAR DADOS
# ======================================================
def salvar_dados(dados: dict):
    linha = f"{dados['cep']}|{dados['endereco']}|{dados['numero']}|{dados.get('telefone','')}\n"
    with open(ARQUIVO_SAIDA, "a", encoding="utf8") as f:
        f.write(linha)
    print("✔ Dados salvos:", linha.strip())

# ======================================================
# WHATSAPP LISTENER
# ======================================================
def iniciar_whatsapp():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com")

    print("📱 Escaneie o QR Code...")
    time.sleep(20)

    mensagens_processadas = set()

    while True:
        mensagens = driver.find_elements(By.CLASS_NAME, "_akbu")

        for msg in mensagens:
            texto = msg.text.strip()

            if texto in mensagens_processadas:
                continue

            mensagens_processadas.add(texto)

            dados = extrair_dados(texto)
            if dados:
                salvar_dados(dados)

        time.sleep(5)

# ======================================================
# EXECUÇÃO
# ======================================================
if __name__ == "__main__":
    iniciar_whatsapp()
    