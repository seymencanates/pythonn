

import DatabaseConnection as connection
import reading as read



#list all rows in the database


def update():

    
    cursor, cnxn = connection.create_connection()
    read.reading()
    chosenData = input('Which one u have chosen?(Please enter id only): ')
    chosenData = int(chosenData)
    read.listingForMatchIdNumber(int(chosenData))
    name = input('Please enter your name for update: ')
    secondName = input('Please enter your second name (if there is) for update:')
    surname = input('Please enter your surname for update: ')
    query1 = 'UPDATE testAndEducationalPurpose SET ogr_no = ? , names = ? , secondNames = ? , surnames = ? WHERE ogr_no = ? '
    cursor.execute(query1,(chosenData,name,secondName,surname,chosenData))
    cnxn.commit()
    cursor.close()
    cnxn.close()

update()




