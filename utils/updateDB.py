from utils.configs import *

class UpdateDB:
    def __init__(self, conn):
        self.conn = conn

    def execute_query_update(self, sql, values):
        try:
            with self.conn.cursor() as cur:
                if values:
                    cur.execute(sql, values) #
                else:
                    cur.execute(sql)
                return cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None
        
    def update_value(self, table, column, value, condition):
        sql = f"""
            UPDATE {table}
            SET {column} = %s
            WHERE {condition};
        """
        return self.execute_query_update(sql, (value,))