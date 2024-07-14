import pandas as pd
from funcoes import extrair_metodo
from funcoes import extrair_detalhe
from funcoes import extrair_win_or_loss_do_texto

# Caminho do arquivo Parquet
caminho_do_arquivo = "C:/Users/rafad/Documents/Repositorios_Git/projeto_mma/src/dados_df.parquet"

# Leitura do arquivo Parquet
df = pd.read_parquet(caminho_do_arquivo)

# Remover linhas completamente nulas
df = df.dropna(how="all")
df = df.dropna(subset='Evento')
df['resultado'] = df['resultado'].replace({None: 'Loss'})

# Aplicar as funções ao DataFrame para criar as novas colunas
df['metodo'] = df['round'].apply(extrair_metodo)
df['detalhe'] = df['round'].apply(extrair_detalhe)
df['resultado'] = df['resultado'].apply(extrair_win_or_loss_do_texto)

# Remover a coluna original 'round'
df = df.drop(columns=['round'])

df.to_parquet('C:/Users/rafad/Documents/Repositorios_Git/projeto_mma/Data/Dados_tratados.parquet')

