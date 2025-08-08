import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head())
"""Shows the first 5 rows of the DataFrame, if you want to see more rows, you can pass a parameter like df.head(10)"""

df.describe()
"""Provides a statistical summary of the DataFrame, including count, mean, standard deviation, minimum, and maximum values for each numeric column."""

print(df.info())
"""Displays information about the DataFrame, including the number of entries, column names, and data types."""

row, column = df.shape[0], df.shape[1]
print(f'this DataFrame owns {row} rows and {column} columns.')
"""the method shape returns a tuple with the number of rows and c
olumns in the DataFrame, I just turnned it fancier"""

print(df.columns)
"""Returns the names of the columns in the DataFrame."""

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
"""the method replace can be also used in maps place"""
"""Renames the columns and rows of the DataFrame to Portuguese for my better understanding."""

print(df["senioridade"].value_counts())
print(df["contrato"].value_counts())
print(df["taxa_remoto"].value_counts())
print(df["tamanho_empresa"].value_counts())
"""Counts the occurrences of each unique value in the cited columns"""

print(df.describe(include='object'))
"""the regular describe just shows the numeric columns, but this one shows the object columns"""