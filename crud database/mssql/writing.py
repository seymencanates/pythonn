
import DatabaseConnection as conn
import reading

def writing(name,secondName,surname,cnxn,cursor):

    cursor.execute("SELECT ogr_no FROM testAndEducationalPurpose ORDER BY ogr_no")
    used_ids = [row[0] for row in cursor.fetchall()]
    
    # 0'dan başlayarak kullanılmayan ilk ID'yi bul
    current_id = 0
    while current_id in used_ids:
        current_id += 1
    
    query = 'INSERT INTO testAndEducationalPurpose (ogr_no, names, secondNames, surnames) VALUES (?, ?, ?, ?)'
    cursor.execute(query, (current_id, name, secondName, surname))
    cnxn.commit()  # Değişiklikleri kaydet
    cursor.close()
    cnxn.close()
    reading.reading()
# Bağlantıyı kapatma (işiniz bitince)

cursor , cnxn = conn.create_connection()
name = input('Please enter your name: ')
secondName = input('Please enter your second name (if there is):')
surname = input('Please enter your surname: ')


writing(name,secondName,surname,cnxn,cursor)