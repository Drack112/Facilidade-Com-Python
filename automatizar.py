from selenium import webdriver
from selenium.webdriver.common.keys import Keys

nav = webdriver.Chrome()

# pyautogui -> Automatizar mouse e teclado
# Selenium -> Automatizar a Web

nav.get("https://www.google.com/")

nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys("cotação dólar")
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys(Keys.ENTER)
cotacao_dolar = nav.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

print(cotacao_dolar)

nav.get("https://www.google.com/")
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys("cotação euro")
nav.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys(Keys.ENTER)
cotacao_euro = nav.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

print(cotacao_euro)

nav.get("https://www.melhorcambio.com/")
nav.find_element_by_xpath('//*[@id="commodity-hoje"]/tbody/tr[2]/td[2]/a/img').click()

aba_nova = nav.window_handles[1]
nav.switch_to.window(aba_nova)

cotacao_ouro = nav.find_element_by_id("comercial").get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

nav.quit()

import pandas as pd

produtos_df = pd.read_excel("/home/drack/Documentos/Automação/databases/Produtos.xlsx")
display(produtos_df)

produtos_df.loc[produtos_df["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
produtos_df.loc[produtos_df["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
produtos_df.loc[produtos_df["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

produtos_df["Preço Base Reais"] = (
    produtos_df["Cotação"] * produtos_df["Preço Base Original"]
)
produtos_df["Preço Final"] = produtos_df["Ajuste"] * produtos_df["Preço Base Reais"]
produtos_df["Preço Final"] = produtos_df["Preço Final"].map("{:.2f}".format)

display(produtos_df)

# Atualizar a base de dados
produtos_df.to_excel(
    "/home/drack/Documentos/Automação/databases/Produtos Atualizado.xlsx", index=False
)
