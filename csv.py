import pandas as pd

df = pd.read_csv("/home/drack/Documentos/Automação/databases/telecom_users.csv")
df = df.drop(["Unnamed: 0"], axis=1)
display(df)

df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
df = df.dropna(how="all", axis=1)
df = df.dropna()

print(df.info())

display(df["Churn"].value_counts())
display(df["Churn"].value_counts(normalize=True).map("{:.1%}".format))

import plotly.express as px

# Para edições nos gráficos: https://plotly.com/python/histograms/
for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color="Churn")
        fig.show()
        display(
            df.pivot_table(index="Churn", columns=coluna, aggfunc="count")["IDCliente"]
        )
