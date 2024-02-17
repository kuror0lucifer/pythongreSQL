import psycopg2
from config import host, dbname, user, password

class pythongre:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
    
    def createTable(self):
        table_name=input('Какое название Вы хотите дать таблице? ')
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname,
            )
            connection.autocommit = True
            
            with connection.cursor() as cursor:
                cursor.execute(
                    f'CREATE TABLE {table_name} ( id BIGSERIAL NOT NULL PRIMARY KEY );'
                )
            
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            if connection:
                connection.close()
                print('Соединение закрыто')
                
    def addingColumn(self):
        table_name=input('В какую таблицу Вы хотите добавить столбец? ')
        column_name=input('Какое название столбца Вы хотите задать? ')
        data_type=input('Какой тип данных Вы хотите задать? ')
        not_null=input('Он обязателен  к заполнению? Y/N ')
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname,
            )
            connection.autocommit = True
            
            with connection.cursor() as cursor:
                
                not_null = 'NOT NULL' if not_null.upper() == 'Y' else ''
                cursor.execute(
                    f'ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type} {not_null};')
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            if connection:
                connection.close()
                print('Соединение закрыто')

    def deleteTable(self):
        table_name=input('Какую таблицу Вы хотите удалить? ')
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname,
            )
            connection.autocommit = True
            
            with connection.cursor() as cursor:
                cursor.execute(
                    f'DROP TABLE {table_name};'
                )
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            if connection:
                connection.close()
                print('Соединение закрыто')
                    
test = pythongre(host, dbname, user, password)

test.deleteTable()