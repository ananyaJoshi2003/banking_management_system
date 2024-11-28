import pymysql

con = pymysql.connect(host='localhost', user = 'root', password = 'root', db = 'pydatabase')
curser = con.cursor()

print("connction sucessfull")

class DbConnection():

    def connection(self):
        con = pymysql.connect(host='localhost', user = 'root', password = 'root', db = 'pydatabase')
        curser = con.cursor()

        return con, curser