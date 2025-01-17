from utils.configs import *

class UpdateDB:
    def __init__(self, conn):
        self.conn = conn

    def execute_query_update(self, sql, values):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, values)
                self.conn.commit()
                return cur.statusmessage
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
        