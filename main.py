import psycopg2
from config import host, dbname, user, password

class pythongre:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
    
    def createTable(self, table_name):
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname,
            )
            
            with connection.cursor() as cursor:
                cursor.execute(
                    f'CREATE TABLE {table_name} ( id BIGSERIAL NOT NULL PRIMARY KEY )'

                )
            
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            if connection:
                connection.close()
                print('Соединение закрыто')
                
test = pythongre(host, dbname, user, password)

test.createTable(input('Какое название таблице Вы хотите задать?'))