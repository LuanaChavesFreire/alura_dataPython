import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

translated_columns = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "salario_usd",
    "employee_residence": "residencia",
    "remote_ratio": "taxa_remoto",
    "company_location": "local_empresa",
    "company_size": "tamanho_empresa"
}
traducao_senioridade = {
    "EN": "júnior",
    "MI": "pleno",
    "SE": "Sênior",
    "EX": "Executivo"
}
traducao_contrato = {
    "FT": "Tempo Integral",
    "PT": "Meio Período",
    "CT": "Contrato",
    "FL": "Freela"
}
traducao_taxa_remoto = {
    0: "Presencial",
    50: "Híbrido",
    100: "Remoto"
}
df.rename(columns=translated_columns, inplace=True)
df["taxa_remoto"] = df["taxa_remoto"].map(traducao_taxa_remoto)
df["contrato"] = df["contrato"].map(traducao_contrato)
df['senioridade'] = df["senioridade"].map(traducao_senioridade)

df_cleanned = df.dropna()
"""Removes rows with any missing values from the DataFrame."""

#df_cleanned['senioridade'].value_counts().plot(kind='bar', title='seniority distribution')
"""Plots the distribution of seniority levels in the DataFrame."""

#plt.show()


#plt.figure(figsize=(8,5))
#sns.barplot(data=df_cleanned, x='senioridade', y='salario_usd')
#plt.title('wage distribution by seniority level')
#plt.xlabel('Seniority')
#plt.ylabel('Avarage anual wage')
""" Creates a bar plot showing the average annual wage by seniority level."""
#plt.show()

ordenating =  df_cleanned.groupby('senioridade')['salario_usd'].mean().sort_values(ascending=False).index
""" Creates an ordered index based on the average salary by seniority level for better visualization. If u change the True to False, it will be ordered from lowest to highest salary."""

#print(ordenating)

#plt.figure(figsize=(8,5))
#sns.barplot(data=df_cleanned, x='senioridade', y='salario_usd', order=ordenating)
#plt.title('wage distribution by seniority level')
#plt.xlabel('Seniority')
#plt.ylabel('Avarage anual wage')
"""Same as above, but uses the ordered index for better visualization."""
#plt.show()

#plt.figure(figsize=(8,5))
#sns.histplot(df_cleanned['salario_usd'], bins=50, kde=True)
#plt.title('Salary distribution')
#plt.xlabel('Salary in USD')
#plt.ylabel('Frequency(people amount)')
"""Creates a histogram with a kernel density estimate (KDE) overlay to visualize the distribution of salaries in USD."""
#plt.show()

#plt.figure(figsize=(8,6))
#sns.boxplot(x=df_cleanned['salario_usd'])
#plt.title('Salary distribution')
#plt.xlabel('Salary in USD')
"""Creates a box plot to visualize the distribution of salaries in USD, highlighting the median, quartiles, and potential outliers."""
#plt.show()


#ordem_senioridade = ['júnior', 'pleno', 'Sênior', 'Executivo']
#plt.figure(figsize=(8,6))
#sns.boxplot(x='senioridade', y='salario_usd', data = df_cleanned, order=ordem_senioridade, palette='Set2', hue='senioridade')
#plt.title('Salary distribution by seniority level')
#plt.xlabel('Seniority level')
#plt.ylabel('Salary in USD')
"""same shit but with colors representing different seniority levels."""
#plt.show()

media_salarial = df_cleanned.groupby('senioridade')['salario_usd'].mean().reset_index()

#fig = px.bar(
#    media_salarial,
#    x='senioridade',
#    y='salario_usd',
#    title='Média Salarial por Senioridade',
#    labels={'senioridade': 'Senioridade', 'salario_usd': #    'Média Salarial (USD)'},
#    color='senioridade',
#    text_auto='.2s'
#)
#fig.show()

remote_count = df_cleanned['taxa_remoto'].value_counts().reset_index()
remote_count.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remote_count,
    names='tipo_trabalho',
    values='quantidade',
    title='Work type proportion',
    hole= 0.5,
    color='tipo_trabalho',
)
fig.update_traces(textinfo='percent+label')
fig.show()