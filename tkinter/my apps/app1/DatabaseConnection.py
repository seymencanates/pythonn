

import pyodbc as connect
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

server = 'localhost\\GHOSTRIDER262'
database = 'dataOfMinee'
user = 'conn'
password = 'seymenSeymen'

def create_connection():
    try:
        connection = connect.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}')
        cursor = connection.cursor()
        return connection , cursor
    except Exception as e:
        print('Something went wrong:', e)
        return e
        exit()
