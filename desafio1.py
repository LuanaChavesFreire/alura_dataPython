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

#fazer um gráfico q mostre a relação entre média salarial por país no cargo de Data Analyst

#print(df.value_counts('cargo'))

ordenating =  df.groupby('senioridade')['salario_usd'].mean().sort_values(ascending=False).index
"""Vai servindo como referencia"""

data_analyst_df = df[df['cargo'] == 'Data Analyst'][['residencia', 'salario_usd']]
# Filtrar apenas os registros de Data Analyst

dA_df = pd.DataFrame({
    'residencia': data_analyst_df['residencia'],
    'salario_usd': data_analyst_df['salario_usd']
})
#organizar os dados de salario por residência dentro do universo Data Analyst

media_salario_residencia = dA_df.groupby('residencia', as_index=False)['salario_usd'].mean()
# Agrupar por residência e calcular a média salarial

media_salario_por_residencia = media_salario_residencia.sort_values('salario_usd', ascending=True)
# Ordenar pelo valor médio do salário

fig = px.bar(
    media_salario_por_residencia,
    x='residencia',
    y='salario_usd',
    title='Média Salarial por Residência (Data Analyst)',
    labels={'residencia': 'Residência', 'salario_usd': 'Média Salarial (USD)'},
    color='residencia'
)
fig.show()