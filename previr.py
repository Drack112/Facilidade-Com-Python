import pandas as pd

df = pd.read_csv("/home/drack/Documentos/Automação/databases/advertising.csv")
display(df)

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df)
plt.show()
sns.heatmap(df.corr(), cmap="Wistia", annot=True)
plt.show()

from sklearn.model_selection import train_test_split

x = df.drop("Vendas", axis=1)
y = df["Vendas"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Modelos de AI

# - Regressão Linear
# - RandomForest (Árvore de Decisão)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

lin_reg = LinearRegression()
rf_reg = RandomForestRegressor()

rf_reg.fit(x_train, y_train)
lin_reg.fit(x_train, y_train)

from sklearn import metrics  # R² --> 0% --- 100%

test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

r2_lin = metrics.r2_score(y_test, test_pred_lin)
mse_lin = metrics.mean_squared_error(y_test, test_pred_lin)

print(f"R² da Regressão Linear: {r2_lin}")
print(f"MSE da Regressão Linear: {mse_lin}")

r2_rf = metrics.r2_score(y_test, test_pred_rf)
mse_rf = metrics.mean_squared_error(y_test, test_pred_rf)

print(f"R² do Random Forest: {r2_rf}")
print(f"MSE do Random Forest: {mse_rf}")

df_resultado = pd.DataFrame()
df_resultado["y_teste"] = y_test
df_resultado["y_previsao_rf"] = test_pred_rf
df_resultado["y_previsao_lin"] = test_pred_lin

df_resultado = df_resultado.reset_index(drop=True)
plt.figure(figsize=(15, 5))
sns.lineplot(data=df_resultado)

plt.show()
display(df_resultado)

plt.figure(figsize=(15, 5))
sns.barplot(x=x_train.columns, y=rf_reg.feature_importances_)
plt.show()

print(df[["Radio", "Jornal"]].sum())
