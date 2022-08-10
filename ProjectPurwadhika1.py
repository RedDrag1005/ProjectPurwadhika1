#create a dictionary with the key names to define the key names
#The key name is the same with the table header column names in the listTxt variable
studentRecord = {
    56781 : {
        'Name' : 'Michael Slade',
        'Physics' : '70',
        'Mathematics' : '95',
        'Language' : '100',
        'Biology' : '80'
    },
    57786 : {
        'Name' : 'Rose Smith',
        'Physics' : '60',
        'Mathematics' : '100',
        'Language' : '80',
        'Biology' : '88'
    }
}

#Create a variable to contain the table header so that if we want to change something we can change it quickly
listTxt = """
Student Score Record

\t\t\t\t\t\t Scores
|Student ID\t|Student Name\t|Physics|Mathematics\t|Language\t|Biology|"""
    
#This is the function to show the records
def showRecord():
    while(True):
        print("""
        Student Score Records
        
        1. Show all current students records
        2. Show Specific Student Score Records
        3. Go back to main menu
        """)
        menuConfirm = int(input('Enter the menu number: '))
        #This is the choice to show all the records
        if (menuConfirm == 1):
            if(len(studentRecord) == 0):
                print('No data in Student Score Record. Returning to Record Menu')
                continue
            else:
                print(listTxt)
                for key in studentRecord.keys():
                    print('|{}\t\t|{}\t|{}\t|{}\t\t|{}\t\t|{}\t|'.format(key, studentRecord[key]['Name'], studentRecord[key]['Physics'],studentRecord[key]['Mathematics'],studentRecord[key]['Language'],studentRecord[key]['Biology']))
        
        #This is the choice to show the specified record
        elif(menuConfirm == 2):
            keyData = int(input('Enter the student ID: '))
            if keyData in studentRecord.keys():
                print(listTxt)
                print('|{}\t\t|{}\t|{}\t|{}\t\t|{}\t\t|{}\t|'.format(str(keyData), studentRecord[keyData]['Name'], studentRecord[keyData]['Physics'],studentRecord[keyData]['Mathematics'],studentRecord[keyData]['Language'],studentRecord[keyData]['Biology']))
            else:
                print('No data in Student Score Record. Returning to Record Menu')
                continue
        else:
            print('Are you sure you want to exit:\n\n1.Yes\n2.No\n')
            menuConfirm = int(input('Enter the Menu Number: '))
            if(menuConfirm == 1):
                print('Returning to main menu')
                break
            else:
                print('Returning to Record Menu.')
                continue

#This is the function to add data to the records
def addRecord():
    while(True):
        print("""
        Student Score Record Data Creation
        
        1. Create a new Student Score Record
        2. Go back to main menu
        """)
        menuConfirm = int(input('Enter the menu number: '))
        if(menuConfirm == 1):
            newKeyData = int(input('Enter the new student ID: '))
            #We compare if the unique key data is contained in the dictionary keys, if yes we return the notification that it is a duplicate data
            if newKeyData in studentRecord.keys():
                print('Duplicate data. Returning to Data Creation Menu')
                continue
            else:
                #First, we put the new data in a variable since we need to confirm first whether we want to save the changes or not
                newName = input('Enter the Student Name: ')
                newPhysics = input('Enter the Student Score for Physics: ')
                newMath = input('Enter the Student Score for Mathematics: ')
                newLang = input('Enter the Student Score for Language: ')
                newBio = input('Enter the Student Score for Biology: ')
                print('\nAre you sure with the data entered\n1.Yes\n2.No\n')
                menuConfirm = int(input('Enter the Menu Number: '))
                if(menuConfirm == 1):
                    studentRecord[newKeyData] = dict(Name = newName, Physics = newPhysics, Mathematics = newMath, Language = newLang, Biology = newBio)
                    print('Data has been saved. Returning to Data Creation Menu')
                    continue
                else:
                    print('Saving Cancelled. Returning to Data Creation Menu')
                    continue
        else:
            print('Are you sure you want to exit:\n\n1.Yes\n2.No\n')
            menuConfirm = int(input('Enter the Menu Number: '))
            if(menuConfirm == 1):
                print('Returning to main menu')
                break
            else:
                print('Returning to Data Creation Menu.')
                continue

#This is the function to updata data that is contained in the records
def updateRecord():
    while(True):
        print("""
        Student Score Record Data Update
        
        1. Update Student Score Record
        2. Go back to main menu
        """)
        menuConfirm = int(input('Enter the menu number: '))
        if(menuConfirm == 1):
            keyData = int(input('Enter the student ID to be updated: '))
            if keyData in studentRecord.keys():
                print(listTxt)
                print('|{}\t\t|{}\t|{}\t|{}\t\t|{}\t\t|{}\t|'.format(keyData, studentRecord[keyData]['Name'], studentRecord[keyData]['Physics'],studentRecord[keyData]['Mathematics'],studentRecord[keyData]['Language'],studentRecord[keyData]['Biology']))
                print('Updating the Student Score Record with ID {} \n1.Yes\n2.No\n'.format(keyData))
                menuConfirm = int(input('Enter the menu number: '))
                if(menuConfirm == 1):
                    column = input('Enter which column to be updated: ')
                    val = input('Enter the new value for the column: ')
                    print('Is the data correct?\n\n1.Yes\n2.No\n')
                    menuConfirm = int(input('Enter the menu number: '))
                    if menuConfirm == 1:
                        studentRecord[keyData][column] = val
                        print('Data has been updated. Returning to Data Update Menu')
                        continue
                    else:
                        print('Data has not been updated. Returning to Data Update Menu')
                        continue
                else:
                    print('Updating Cancelled. Returning to Data Update Menu')
                    continue
            else:
                print('No data with that ID. Returning to Data Update Menu')
                continue       
        else:
            print('Are you sure you want to exit:\n\n1.Yes\n2.No\n\n')
            menuConfirm = int(input('Enter the Menu Number: '))
            if(menuConfirm == 1):
                print('Returning to main menu')
                break
            else:
                print('Returning to Data Update Menu.')
                continue

#This is the function to remove data from the records
def removeRecord():
    while(True):
        print("""
        Student Score Record Data Deletion
        
        1. Delete a new Student Score Record
        2. Go back to main menu
        """)
        menuConfirm = int(input('Enter the menu number: '))
        if(menuConfirm == 1):
            keyData = int(input('Enter the student ID to be deleted: '))
            #confirm whether or not the key is in the dictionary
            if keyData in studentRecord.keys():
                print('Are you sure you are deleting the Student Score Record with ID {} \n1.Yes\n2.No\n'.format(keyData))
                menuConfirm = int(input('Enter the menu number: '))
                if(menuConfirm == 1):
                    del studentRecord[keyData]
                    print('Data has been deleted. Returning to Data Deletion Menu')
                    break
                else:
                    print('Deletion Cancelled. Returning to Data Deletion Menu')
                    continue
            else:
                print('No data with that ID. Returning to Data Deletion Menu')
                continue       
        else:
            print('Are you sure you want to exit:\n\n1.Yes\n2.No\n')
            menuConfirm = int(input('Enter the Menu Number: '))
            if(menuConfirm == 1):
                print('Returning to main menu')
                break
            else:
                print('Returning to Data Deletion Menu.')
                continue

#we use the while true loop so that it will loop indefinitely until we break the loop when we input exit program
while(True):
    print("""
        Student Score Records Main Menu

        Menu List:
        1. Show students records
        2. Create a Student Score Record
        3. Update a Student Score Record
        4. Delete a Student Score Record
        5. Exit Program
        """
    )
    listMenu = int(input('\tEnter the menu number: '))

    # List the Record
    if(listMenu == 1):
        showRecord()
    
    # addding data to the record 
    elif(listMenu == 2):
        addRecord()

    # update a data that is contained in the record 
    elif(listMenu == 3):
        updateRecord()
    
    #remove data from the record
    elif(listMenu == 4):
        removeRecord()

    #program exit
    elif(listMenu == 5):
        print('''
        Are you sure you want to exit?

        1. Go back to main menu
        2. Exit the Program

        ''')
        #confirmation to exit, we use continue if we don't want to exit so that it will continue to the beginning of the loop else, it will break the loop and finish the program
        exitConfirmation = int(input('Enter the menu number: '))
        if(exitConfirmation == 1):
            continue
        else:
            break

    #if the program receive any other input, it will print out an error message
    else:
        print('Wrong option has been chosen.')
