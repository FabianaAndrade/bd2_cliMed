from utils.configs import *

class ReturnDB:
    def __init__(self, conn):
        self.conn = conn

    def execute_query(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall(), [desc[0] for desc in cur.description]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None
        
    def select(self, sql):
        """Executa uma query SQL passada pelo usuario e retorna o resultado"""
        result = self.execute_query(sql)
        self.exibe_df(result)
        

    def select_tb(self, table):
        """Seleciona todos os registros de uma tabela com nome recebido como parâmetro"""
        sql = f"""
            SELECT * FROM {table};
            """
        result = self.execute_query(sql)
        self.exibe_df(result)
        

    def nomes_tabelas_da_base(self):
        """Funcao para bater na conexao e pegar os nomes das tabelas da base"""
        sql = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """
        result = self.execute_query(sql)
        tuplas = result[0]
        lista = [item[0] for item in tuplas]
        return lista
    
    def nomes_colunas_da_tabela(self, table):
        """Funcao para bater na conexao e pegar os nomes das colunas de uma tabela"""
        sql = f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = '{table}';
        """
        result = self.execute_query(sql)        
        tuplas = result[0]
        lista = [[item[0], item[1]] for item in tuplas]

        return lista


    def exibe_df(self, resultado_query):
        """Exibe o resultado da query em um DataFrame"""
        if resultado_query:
            tuplas = resultado_query[0]
            colunas = resultado_query[1]
            df = pd.DataFrame(tuplas, columns=colunas)
            print("\nRESULTADO DA CONSULTA\n")
            print(df)
            print("\n")
        else:
            print("Nenhum registro encontrado")