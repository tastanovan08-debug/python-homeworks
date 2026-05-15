import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1
df = pd.read_excel('catalog_products.xlsx')

# 2
for col in df.columns:
    converted_col = pd.to_numeric(df[col], errors='coerce')
    if converted_col.notnull().sum() > 0:
        df[col] = converted_col.astype(float)
        if not df[col].isnull().all():
            df[col] = df[col].fillna(df[col].mean())
df = df.fillna(0)

# 3
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log1p(df['col_2'])

# 4
electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == 'Electronics')].copy()

# 5.
category_group = df.groupby('col_7').agg({
    'col_2': ['mean', 'max'],
    'col_3': 'sum'
}).reset_index()
category_group.columns = ['category', 'mean_price', 'max_price', 'total_quantity']

# 6
cols_10 = [f'col_{i}' for i in range(2, 12)]
for col in cols_10:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

stats_df = df[cols_10].agg(['mean', 'median', 'std']).T.reset_index()
stats_df.columns = ['column', 'mean', 'median', 'std']
cols_10 = [f'col_{i}' for i in range(2, 12)]
stats_df = df[cols_10].agg(['mean', 'median', 'std']).T.reset_index()
stats_df.columns = ['column', 'mean', 'median', 'std']

# 7
mean_p = df['col_2'].mean()
std_p = df['col_2'].std()
anomalies = df[df['col_2'] > (mean_p + 3 * std_p)]

# 8
corr_matrix = df[cols_10].corr()

# 9
plt.figure(figsize=(10, 6))
sns.histplot(df['col_2'], bins=50, kde=True)
plt.title('Распределение цены товаров')
plt.show()

# 10
plt.figure(figsize=(10, 6))
sns.regplot(data=df.sample(min(len(df), 500)), x='col_2', y='col_3', scatter_kws={'alpha':0.5})
plt.title('Связь цены и количества на складе')
plt.show()

# 11
df_plot = df.dropna(subset=['col_7'])
plt.figure(figsize=(12, 6))
sns.boxplot(x='col_7', y='col_2', data=df_plot)
plt.title('Распределение цен по категориям')
plt.xticks(rotation=45)
plt.show()

# 12
selected_cols_pair = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']
sns.pairplot(df[selected_cols_pair].sample(min(len(df), 300)), hue='col_7')
plt.show()

# 13
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Тепловая карта корреляции')
plt.show()

# 15
category_summary = df.groupby('col_7').agg({
    'col_1': 'count',
    'col_2': 'mean',
    'col_3': 'sum',
    'log_price': 'mean'
}).rename(columns={'col_1': 'count', 'col_2': 'mean_price', 'col_3': 'total_quantity', 'log_price': 'mean_log_price'})

# 16
most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax(), ['col_1', 'col_2', 'col_7']]

# 17. Топ-10
top_10_value = df.sort_values(by='total_value', ascending=False).head(10)

# 18
bins = [0, 50, 200, 500, 1000, np.inf]
labels = ['до 50', '50–200', '200–500', '500–1000', 'больше 1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='price_range', palette='viridis')
plt.title('Количество товаров по ценовым диапазонам')
plt.show()

# 19
cat_capital = df.groupby('col_7')['total_value'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=cat_capital, x='total_value', y='col_7')
plt.title('Суммарная стоимость запасов по категориям')
plt.show()

# 20
cat_stats = df.groupby('col_7').agg({'col_2': 'mean', 'col_3': 'mean'}).reset_index()
plt.figure(figsize=(10, 6))
sns.scatterplot(data=cat_stats, x='col_2', y='col_3', hue='col_7', s=200)
plt.title('Средняя цена vs Средний запас')
plt.show()

# 21
cat_std = df.groupby('col_7')['col_2'].std().sort_values(ascending=False).reset_index()
plt.figure(figsize=(10, 8))
sns.barplot(data=cat_std, x='col_2', y='col_7', palette='magma')
plt.show()

# 22
print("Товары с нулевым запасом:")
print(df[df['col_3'] == 0][['col_1', 'col_7', 'col_2']].head(10))

# 23
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

# 25
pivot_table = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
plt.show()

# 42
plt.figure(figsize=(10, 6))
sns.regplot(data=df.sample(min(len(df), 500)), x='col_2', y='col_5', scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.show()

# 44
p_limit = df['col_2'].mean() + 3 * df['col_2'].std()
s_limit = df['col_3'].mean() + 3 * df['col_3'].std()
extreme_items = df[(df['col_2'] > p_limit) | (df['col_3'] > s_limit)].copy()

# 45 Excel
category_pivot = df.groupby('col_7').agg({
    'col_2': 'mean', 'col_3': 'sum', 'total_value': 'sum'
}).rename(columns={'col_2': 'Средняя цена', 'col_3': 'Запас на складе'})

with pd.ExcelWriter('catalog_final_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Данные анализа', index=False)
    category_pivot.to_excel(writer, sheet_name='Отчет по категориям')
    extreme_items.to_excel(writer, sheet_name='Аномалии', index=False)
    top_10_value.to_excel(writer, sheet_name='Топ-10 по стоимости', index=False)

print("Все задачи выполнены. Файл 'catalog_final_report.xlsx' сохранен.")