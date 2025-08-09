import pandas as pd
import numpy as np

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

print(df.isnull())
"""Checks for missing values in the DataFrame and returns a DataFrame of the same shape with boolean values indicating the presence of nulls."""

print(df.isnull().sum())
"""Returns the count of missing values for each column in the DataFrame."""

print(df['ano'].unique())
"""Returns the unique values present in the 'ano' column."""

print(df[df.isnull().any(axis=1)])
"""Returns all rows that contain at least one missing value."""

df_wage = pd.DataFrame({
    'name':['Camila', 'Luana', 'João', 'Denilson', 'Valery'],
    'wage':[4000, np.nan, 5000, np.nan, 10000]
})
"""Creates a new DataFrame with names and wages, where some wages are NaN (missing values) for practice pourpose."""

df_wage['wage_avarage'] = df_wage['wage'].fillna(df_wage['wage'].mean().round(2))
"""fills the NaN values with the average of the column, rounded to 2 decimal places"""

df_wage['wage_median'] = df_wage['wage'].fillna(df_wage['wage'].median().round(2))
"""fills the NaN values with the median of the column, rounded to 2 decimal places"""

print(df_wage)

df_temperature = pd.DataFrame({
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'temperature': [np.nan, 30, np.nan, 28, 27]
})

df_temperature['fillded_ffill'] = df_temperature['temperature'].ffill()
print(df_temperature)
"""Fills NaN values using forward fill method, which propagates the last valid observation forward. Clearly dont work for the first row."""

df_temperature['fillded_ffill'] = df_temperature['temperature'].bfill()
"""Fills NaN values using backward fill method, which uses the next valid observation to fill the gap."""

print(df_temperature)

df_characters = pd.DataFrame({
    'name': ['Luana', 'Bob', 'Charlie', 'David'],
    'city': ['Recife', np.nan, 'Peixinhos', 'Águas Cmpridas']
})

df_characters['city_fill'] = df_characters['city'].fillna('Unknown')
"""Fills NaN values in the 'city' column with the string 'Unknown'"""

print(df_characters)

#cmming back to the original dataframe

df_cleanned = df.dropna()
print(df_cleanned.isnull().sum())

print(df_cleanned.info())

df_cleanned= df_cleanned.assign(ano = df_cleanned['ano'].astype('int64'))
""" Changes the data type of the 'ano' column to integer."""

print(df_cleanned.info())
print(df_cleanned.head())