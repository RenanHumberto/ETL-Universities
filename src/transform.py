import pandas as pd

class Transform:
    def __init__(self):
        pass

    def transform_data(self, data):
        if not data:
            return pd.DataFrame()  # Retorna DF vazio se não houver dados
        
        df = pd.DataFrame(data)
        
        # Renomear colunas para combinar com o schema do banco
        df = df.rename(columns={'state-province': 'state_province'})
        
        # Converter listas para strings separadas por vírgula
        df['web_pages'] = df['web_pages'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
        df['domains'] = df['domains'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
        
        # Tratar nulos
        df['state_province'] = df['state_province'].fillna('Desconhecido')
        
        # Selecionar apenas colunas necessárias (e descartar extras como 'alpha_two_code')
        columns = ['name', 'country', 'state_province', 'web_pages', 'domains']
        df = df[columns]
        
        return df