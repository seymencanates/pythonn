
import DatabaseConnection as conn

def reading():
    cursor, cnxn = conn.create_connection()
    squery = 'SELECT * FROM testAndEducationalPurpose'
    cursor.execute(squery)
    
    # Sonuçları yazdırma
    row =cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    
    # Bağlantıyı kapama
    cursor.close()
    cnxn.close()


reading()


def listingForMatchIdNumber(chosenId):

    cursor, cnxn = conn.create_connection()
    squery2 = f'SELECT * FROM testAndEducationalPurpose where ogr_no = {chosenId}'
    cursor.execute(squery2)
    row2 = cursor.fetchone()
    print(row2)
    cursor.close()
    cnxn.close()