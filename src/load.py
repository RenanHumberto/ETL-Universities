import sqlite3
import pandas as pd

class Load:
    def __init__(self):
        pass

    def create_sqlite_table(self, df, db_name, table_name):
        if df.empty:
            print("Nenhum dado para carregar.")
            return

        con = sqlite3.connect(f"{db_name}.db")
        # Cria a tabela (if_exists='replace' para substituir se existir, ou 'append' para adicionar)
        df.to_sql(table_name, con, if_exists='replace', index=True, index_label='id')
        con.close()
        print(f"Dados carregados com sucesso na tabela '{table_name}' do banco '{db_name}.db'.")

    # Nova consulta: Total de universidades por país
    def count_universities_by_country(self, db_name, table_name):
        con = sqlite3.connect(f"{db_name}.db")
        query = f"SELECT state_province, COUNT(*) as total FROM {table_name} GROUP BY state_province;"
        df_result = pd.read_sql_query(query, con)
        con.close()
        return df_result

    # Nova consulta: Listagem de universidades de um país específico
    def list_universities_by_country(self, db_name, table_name, country):
        con = sqlite3.connect(f"{db_name}.db")
        query = f"SELECT * FROM {table_name} WHERE state_province = ?;"
        df_result = pd.read_sql_query(query, con, params=(country,))
        con.close()
        return df_result

    # Nova consulta: Busca por nomes que contenham um termo definido
    def search_universities_by_name(self, db_name, table_name, search_term):
        con = sqlite3.connect(f"{db_name}.db")
        query = f"SELECT * FROM {table_name} WHERE name LIKE ?;"
        df_result = pd.read_sql_query(query, con, params=('%' + search_term + '%',))
        con.close()
        return df_result