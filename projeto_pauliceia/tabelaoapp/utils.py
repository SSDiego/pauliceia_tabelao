from numpy import NaN
from pandas import DataFrame, read_csv


class BigTable():

  
    def mapear_nomes(variaveis):
        mapeamento = {
            'id_da rua': 'id_street', 'Id_ponto': 'id_point', 'metragem': 'metre',
            'logradouro': 'address', 'numero': 'number', 'numero original': 'original_n',
            'Data inicial': 'initial_date', 'Data_final': 'final_date',
            'fonte': 'source', 'autor_da_alimentação': 'author', 'Data': 'date'
        }
        variaveis_mapeadas = {mapeamento.get(chave, chave): valor for chave, valor in variaveis.items()}
        return variaveis_mapeadas

        

    def correcao_pontual(df):
        df['metre'] = df['metre'].str.replace(',', '.').astype(float)
        df['number'] = df['number'].str.replace(',', '.').astype(float)
        df['initial_date'] = df['initial_date'].str.replace(' ', '')
        df['final_date'] = df['final_date'].str.replace(' ', '')






