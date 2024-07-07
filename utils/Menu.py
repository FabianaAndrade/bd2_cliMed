from utils.configs import *
from utils.returnDB import ReturnDB
from utils.insertDB import InsertDB
from utils.updateDB import UpdateDB


class MenuCliMed:
    def __init__(self, conn):
        self.conn = conn
        self.insertDB = InsertDB(conn)
        self.returnDB = ReturnDB(conn)
        self.updateDB = UpdateDB(conn)
        self.tables =  self.returnDB.nomes_tabelas_da_base()
        self.menu_tb = self.gera_tbs()
        self.show_menu()
    
    def show_menu(self):
        print("\n-------Bem vindo ao Sistema de Gerenciamento de Clínicas Médicas-----")
        print("\n----Menu de Opções----")
        while True:
            print('1: Inserções\n2: Consultas\n3: Atualizações\n4: Sair \n')
            op = int(input("Digite a opção desejada: "))
            if op == 1:
                self.show_menu_insert()
            elif op == 2:
                self.show_menu_consult()
            elif op == 3:
                self.show_menu_update()
            elif op == 4:
                print("Saindo...")
                sys.exit()
            else:
                print("Opção inválida")
        
    
    
    def show_menu_consult(self):
        print("\n----Menu de Consultas----")
        print('1: Consultar uma das tabelas\n2: QUERY PROPRIA\n3: Voltar\n')

        while True:
            op = int(input("Digite a opção desejada: "))
            if op == 1:
                self.show_menu_consult_table()
            elif op == 2:
                self.show_menu_consult_query()
            elif op == 3:
                self.show_menu()
            else:
                print("Opção inválida")
    
    def show_menu_consult_table(self):
        os.system('cls' if os.name == 'nt' else 'clear') #(TALVEZ SEJA BOM COLOCAR em todos)

        print("\n----Menu de Consultas de Tabelas---")
       
        while True:
            self.lista_tbs()
            op = int(input("\nDigite a opção desejada: \n"))
            if op in range(1, len(self.tables) + 1):
                self.returnDB.select_tb(self.tables[op - 1])
            elif op == len(self.tables) + 1:
                self.show_menu_consult()
            else:
                print("\nOpção inválida")
            
    def show_menu_consult_query(self):
        print("\n----Menu de Consultas de Query----")
      
        while True:
            print("1: Executar Query\n2: Voltar\n")
            op = int(input("Digite a opção desejada: "))
            if op == 1:
                 query = input("\nDigite a query (SQL PADRAO): ")
                 self.returnDB.select(query)
            elif op == 2:
                self.show_menu_consult()
            else:
                print("Opção inválida")

    def show_menu_update(self):
        '''Update de informações na base de dados'''
        print("\n----Menu de Atualizações----")
    
        while True:
            self.lista_tbs()
            op = int(input("\nDigite a opção desejada: "))
            get_op = self.menu_tb.get(op)
            if get_op:
                if  get_op == "Voltar":
                    self.show_menu()
                else:
                    print(f"\nAtualização em '{get_op}'")
                    columns = self.lista_colunas(get_op)
                    while True:
                        column = input("Digite o nome da coluna a ser atualizada: ")
                        col_names = [col[0] for col in columns]
                        if column in col_names:
                            pos = col_names.index(column)
                            value = input(f"Digite o novo valor para {columns[pos][0].upper()} ({columns[pos][1].upper()}) : ")
                            condition = input("Digite a condição: ")
                            self.updateDB.update_value(get_op, column, value, condition)
                            break
                        else:
                            print("Coluna inválida. Tente novamente.")
                   
            else:
                print("\nOpção inválida")
    
    def show_menu_insert(self):
        '''Funcao para insercao de dados na base'''
        print("\n----Menu de Inserções----")
        while True:
            self.lista_tbs()
            op = int(input("\nDigite a opção desejada: "))
            get_op = self.menu_tb.get(op)
            if get_op:
                if  get_op == "Voltar":
                    self.show_menu()
                else:
                    print(f"\nInserção em {get_op}")
                    params = self.returnDB.nomes_colunas_da_tabela(get_op)
                    values = ()
                    for param in params:
                        print(f"Digite o valor para {param[0].upper()} ({param[1].upper()}): ", end="")
                        values += (input(),)
                    colunas = [param[0] for param in params]
                    self.insertDB.insert(get_op, ', '.join(colunas), ', '.join(values))
            else:
                print("\nOpção inválida")

    def lista_tbs(self):
        '''Funcao para listar as tabelas da base'''
        print("\n----Opções Disponiveis----")
        for op in self.menu_tb:
            print(f"{op}: {self.menu_tb[op]}")
        print("\n")

    def lista_colunas(self, table):
        '''Funcao para listar as colunas de uma tabela'''
        print("\n----Colunas da Tabela----")
        colunas = self.returnDB.nomes_colunas_da_tabela(table)
        for col in colunas:
            print(f"{col[0]} ({col[1]})")
        print("\n")
        return colunas
    
    def gera_tbs(self):
        '''Funcao para gerar as tabelas da base em um dicionario'''
        menu = {}
        for tb in self.tables:
            menu[self.tables.index(tb) + 1] = f"{tb}"
        menu[len(self.tables) + 1] = "Voltar"
        return menu