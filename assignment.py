#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""
import sqlite3
class main():
    def __init__(self) -> None:
        
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists petstore (
            id integer primary key autoincrement,
            petname tinytext,
            species tinytext,
            breed tinytext,
            name tinytext,
            phone int,
            email tinytext,
            balance int,
            date tinytext);
        """
        self.cursor.execute(query)
        self.decision()

    def decision(self):
        choice = int(input("would you like to do: 1)insert new record, 2)retrieve record by id, 3)retrieve record by email, 4) retrieve record by phone number: "))
        if choice == 1:
            self.insert()
        elif choice == 2:
            self.RetrieveID()
        elif choice == 3:
            self.RetrieveEmail()
        elif choice == 4:
            self.RetrievePH()
        elif choice == 5:
            self.getall()

    def insert(self):
        petname = input("enter pets name:   ")
        species = input("enter pets species:    ")
        breed = input("eneter pets breed:   ")
        name = input("enter owners name:    ")
        phone_number = int(input("enter phone number:   "))
        email = input("enter email:     ")
        balance = int(input("enter what owner owes:     "))
        date = input("enter the date of first visit:    ")
        query = f"insert into petstore (petname,species,breed,name,phone,email,balance,date) values ('{petname}','{species}','{breed}','{name}','{phone_number}','{email}','{balance}','{date}');"
        self.cursor.execute(query)
        self.connection.commit()
    def RetrieveID(self):
        ID = int(input("enter in the ID of the person you are searching:    "))
        query = f"select * from petstore where id=={ID}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
        
    def RetrieveEmail(self):
        email = str(input("enter in the email of the person you are searching:  "))
        query = f"select * from petstore where email=='{email}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()#Too scary cant look. Please help me it is ansons fac
        print(result)
    def RetrievePH(self):
        PH = int(input("enter in the phone number of the person you are searching:    "))
        query = f"select * from petstore where phone=={PH}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
    def getall(self):
        query = "select * from petstore"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)

main()