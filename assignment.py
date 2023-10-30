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
        connection = sqlite3.connect(file)
        cursor = connection.cursor()
        query = """
        create table if not exists customers (
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
        cursor.execute(query)
        self.decision()

    def decision(self):
        choice = int(input("would you like to do: 1)insert new record, 2)retrieve record by id, 3)retrieve record by email, 4) retrieve record by phone number"))
        if choice == 1:
            self.insert()
        elif choice == 2:
            self.RetrieveID()
        elif choice == 3:
            self.RetrieveEmail()
        elif choice == 4:
            self.RetrievePH()

    def insert(self):
        petname = input("enter pets name:   ")
        species = input("enter pets species:    ")
        breed = input("eneter pets breed:   ")
        name = input("enter owners name:    ")
        phone_number = int(input("enter phone number:   "))
        email = input("enter email:     ")
        balance = int(input("enter what owner owes:     "))
        date = input("enter the date of first visit:    ")
        query = f"insert into customers (petname,species,breed,name,phone,email,balance,date) values ('{petname}','{species}','{breed}','{name}','{phone_number}','{}','{}','{}','{}',)"

main()