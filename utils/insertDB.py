from utils.configs import *

class InsertDB:
    def __init__(self, conn):
        self.conn = conn


    def execute_query(self, sql, values):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, values)
                self.conn.commit()
                return cur.statusmessage
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None
    
    def insert(self, tabela, colunas, valores):
        sql = f"""
            INSERT INTO {tabela} ({colunas})
            VALUES ({valores});
        """
        return self.execute_query(sql, ())
