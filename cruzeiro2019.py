import pandas as pd

# URL da página da Série A 2019 – Cruzeiro (FBref)
url = "https://fbref.com/en/squads/03ff5eeb/2019/c24/Cruzeiro-Stats-Serie-A"

# Extrai todas as tabelas da página
tabelas = pd.read_html(url)

# A tabela de jogos geralmente está nas posições 0 ou 1
for idx, tabela in enumerate(tabelas):
    print(f"Tabela {idx} – colunas:", list(tabela.columns))

# Supondo que a tabela correta seja a segunda (índice 1), ajuste conforme necessário:
df = tabelas[1]

# Renomear colunas
df = df.rename(columns={
    'Date': 'Data',
    'Venue': 'Local',
    'Opponent': 'Adversário',
    'Result': 'Resultado',
    'GF': 'Gols Cruzeiro',
    'GA': 'Gols Adversário',
    'Attendance': 'Público'
})

# Selecionar colunas essenciais (filtre NaNs, se aparecerem)
df_final = df[['Data', 'Local', 'Adversário', 'Resultado', 'Gols Cruzeiro', 'Gols Adversário', 'Público']].dropna()

# Corrigir formato de 'Local' (Home/Away)
df_final['Local'] = df_final['Local'].apply(lambda x: 'Casa' if x == 'Home' else 'Fora')

# Converter colunas numéricas
df_final['Público'] = df_final['Público'].str.replace(',', '').astype(int)
df_final['Data'] = pd.to_datetime(df_final['Data']).dt.date

# Salvar o CSV
arquivo = "cruzeiro_2019_real.csv"
df_final.to_csv(arquivo, index=False)

print(f"✔️ Arquivo salvo: {arquivo}")
print(df_final.head())
