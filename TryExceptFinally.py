
def final(connection=False):
    if connection:
        connection.close()
        print('Операция успешно выполнена!')
