import psycopg2
from config import host, dbname, user, password
from TryExceptFinally import final
class pythongre:
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
    
    def createDB(self):
        db_name = input('Введите название базы данных, которую хотите создать: ')
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
                    f'CREATE DATABASE {db_name}'
                )
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            final(connection)
            
    def dropDB(self):
        dbname = input('Какую базу данных Вы хотите удалить? ') 
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
                    f'DROP DATABASE {dbname}'
                )
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            final(connection)
    
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
            
            columns = []
            isPrimaryKeySet = False
            while True:
                column_name = input('Введите название столбца (или "готово", чтобы закончить): ')
                if column_name.lower() == 'готово':
                    break
                
                data_type = input(f'Введите тип данных для столбца {column_name} ')
                not_null = input(f'Столбец {column_name} обязательно должен быть заполненным? Y/N ')
                
                if not_null.lower() == 'y':
                    not_null = 'NOT NULL'
                else:
                    not_null = '' 
                    
                key = input(f'Столбец {column_name} должен иметь первичный ключ? Y/N ')
                if key.lower() == 'y' and isPrimaryKeySet == False:
                    key = 'PRIMARY KEY'
                    isPrimaryKeySet = True
                elif key.lower() == 'y' and isPrimaryKeySet == True:
                    key = ''
                    print('Первичный ключ уже был задан ')
                elif key.lower() == 'n':
                    key = ''

                columns.append(f'{column_name} {data_type} {not_null} {key}')
                
            columns_str = ', '.join(columns)
            
            with connection.cursor() as cursor:
                cursor.execute(
                    f'CREATE TABLE {table_name} ({columns_str});'
                )
            print(f'Таблица {table_name} успешно создана с столбацми: {columns_str}')
            
        except Exception as ex:
            print('Ошибка работы с PostgreSQL', ex)
        finally:
            final(connection)
                
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
            final(connection)

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
            final(connection)
                           
test = pythongre(host, dbname, user, password)

test.createTable()