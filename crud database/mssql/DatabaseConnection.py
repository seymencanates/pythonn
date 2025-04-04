import pyodbc as connection
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Bağlantı bilgileri
server = 'localhost\\GHOSTRIDER262'
database = 'dataOfMinee'
user = 'conn'
password = 'seymenSeymen'

def create_connection():
    try:
        # Veritabanına bağlantı
        cnxn = connection.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}')
        print('Connected successfully')
        cursor = cnxn.cursor()
        #cursor object is necessary for create queries above database
        return cursor, cnxn  # Bağlantıyı ve cursor'ı döndürüyoruz
    except Exception as e:
        print('Something went wrong:', e)
        return e
        exit()

# Fonksiyonu çağırmak

# Bağlantıyı ve cursor'ı kullanmaya devam edebilirsiniz
# Örnek: Veritabanına sorgu gönderme
# cursor.execute("SELECT * FROM your_table")
# rows = cursor.fetchall()
# for row in rows:
# print(row)


