import pyautogu.isprintable()
import time
import pyperclip
import pandas as pd


pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, aperte OK e não mexa em nada")

# pyautogui.press("winleft")
# pyautogui.write("chrome")
# pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")

link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(935, 694, clicks=2)
pyautogui.click(2028, 895)
pyautogui.click(3306, 406)
pyautogui.click(2880, 1489)
time.sleep(10)

df = pd.read_excel("./databases/Vendas - Dez.xlsx")
display(df)
faturamento = df["Valor Final"].sum()
qtde_produtos = df["Quantidade"].sum()

pyautogui.hotkey("ctrl", "t")
pyautogui.write("mail.google.com")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(307, 506)

pyautogui.write("mhyeddd@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
assunto = "Relatório de Vendas de Ontem"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}

Abs
Drack"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
pyautogui.alert("Fim da Automação. Seu computador já voltou a ser seu")
