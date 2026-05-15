import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("catalog_products.xlsx")
for col in df.columns:
    converted_col = pd.to_numeric(df[col], errors="coerce")
    if converted_col.notnull().sum() > 0:
        df[col] = converted_col.astype(float)
        if not df[col].isnull().all():
            df[col] = df[col].fillna(df[col].mean())
df = df.fillna(0)
df["total_value"] = df["col_2"] * df["col_3"]
#20
cat_average = df.groupby("col_7").agg({"col_2": "mean", "col_3": "mean"}).reset_index()
plt.figure(figsize=(10, 5))
sns.scatterplot(data=cat_average, x="col_2", y="col_3", hue="col_7", s=200)
plt.title("Средняя цена и средний запас по категории")
plt.show()


#21
std_sns = df.groupby("col_7")["col_2"].std().sort_values(ascending=False).reset_index()
plt.figure(figsize=(10, 7))
sns.barplot(data=std_sns, x = "col_2", y="col_7", palette="magma")
plt.show()

#22
no_stock = df[df['col_3'] == 0][['col_1', 'col_7', 'col_2']].head(10)
print("Товары с нулевым запасом: ", no_stock)

#23
top_5_cat = df['col_7'].value_counts().head(5).reset_index()
top_5_cat.columns = ['category', 'count']
plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_cat, x='count', y='category')
plt.show()

#24
top_10_stock_items = df.sort_values(by='col_3', ascending=False).head(10)
plt.figure(figsize=(10, 8))
sns.barplot(data=top_10_stock_items, x='col_3', y='col_1', palette='Blues_r')
plt.title('Топ-10 товаров с наибольшим запасом')
plt.xlabel('Количество на складе')
plt.ylabel('Название товара')
plt.show()

#25
bins = [0, 50, 200, 500, 1000, np.inf]
labels = ['до 50', '50–200', '200–500', '500–1000', 'больше 1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
pivot_table = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
plt.show()