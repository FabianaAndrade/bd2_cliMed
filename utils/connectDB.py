
from utils.configs import *

class ConnectDB:
    def __init__(self, db, host, user, password, port):
        self.db = db
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        conexao = None
        try:
            conexao = psycopg2.connect(
                database=self.db,
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("Conexão estabelecida com sucesso")
            print("Status da Conexão:", conexao.status)
            print("Informações da Conexão:", conexao.info)
            return conexao
        except (Exception, psycopg2.DatabaseError) as error:
            print("Erro ao conectar ao banco de dados:", error)
            return None

    def close_connection(self, conexao):
        if conexao:
            conexao.close()
            print("Conexão fechada")