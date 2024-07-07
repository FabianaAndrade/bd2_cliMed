from utils.connectDB import *
from utils.Menu import MenuCliMed

if __name__ == '__main__':

    #conexao com o DB
    connect_db = ConnectDB('cliMed', 'localhost', 'postgres', 'admin', 5432 )
    conn = connect_db.connect()

    menu = MenuCliMed(conn=conn)