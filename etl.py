import pandas as pd
import os
import glob

# Funçaõ Extract, que lê e consolida dados do arquivo JSON

pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
print(arquivos_json)
#pd.read_json('')

# Função Transfortm, que transforma os dados em um DataFrame

# Função Load, que carrega os dados em CSV ou Parquet