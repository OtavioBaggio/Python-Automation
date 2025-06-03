import pyautogui    # Biblioteca de Automação em Python
import time
import pandas

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

# PASSO 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome:
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
# digitar o site:
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# espera 3 segundos:
time.sleep(3)

# PASSO 2: Fazer o login
# preencher email:
pyautogui.click(x=603, y=448)
pyautogui.write("pythomloko@gmail.com")

# preencher senha:
pyautogui.press("tab")
pyautogui.write("123456789")

# logando:
pyautogui.press("tab")  # nessa etapa, com o tab vai mais rápido do que com o click;
pyautogui.press("enter")

# espera de 3s de precaução, caso o site demore para carregar:
time.sleep(3)


# PASSO 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)


# PASSO 4: Cadastrar 1 produto

for linha in tabela.index:  # Para cada linha da tabela
    pyautogui.click(x=597, y=304)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab")  #Passou para o próximo campo
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan": 
        pyautogui.write(obs)

    pyautogui.press("tab")  # Foi para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(5000)


# PASSO 5: Repetir para todos os produtos