import psycopg2
from psycopg2 import extensions
import time


class DBCalls:

    def __init__(self):
        self.conn = None
        self.cursor=None

    def set_dbconn(self, conn):
        self.conn = conn

    def connect_to_db(self):
        #establishing the connection.
        # Enter the database name:
        dbname = "Office Hours"
        # Enter your password for postgres:
        pwd= "Gr@fton2003!"
        # the default host IP and port are included. Probably don't need to change.
        # you can see the port when you log in to psql. 
        self.conn = psycopg2.connect('dbname=' + dbname + ' user=postgres password='+pwd+' host=127.0.0.1 port= 5432')


def add_student(self,email, password):
    # make the parameters all of the things I need, can pass them in from the object later
    result = get_emails();
    try: 
        if(result.count(email) == 0):
        # Maybe set isolation level
            query = ("insert into Students values (%s,%s)") #IDK what the name of the actual table was

            self.cursor = self.conn.cursor()

            self.cursor.execute(query,[email,password])

            self.conn.commit()

    except psycopg2.Error as e:
            print('Error while adding claim, try again.\n' + str(e))

    def close_db(self):
        self.conn.close()


def login(self, email, password):#Maybe for logging in??? Have something that checks if an email is in the database, then if it is check against the pasword entered
    result = []
    try:
        query = ("select student, password from LOGIN where email = %s and password = %s")
        self.cursor = self.conn.cursor()

        self.cursor.execute(query,[email,password])
        result.append(self.cursor.fetchall())

        return (result.length >0) #Double check this
        


    except psycopg2.Error as e:
            print('Error while adding claim, try again.\n' + str(e))


def set_rankings(self, email, first, second, third):
     
    try: 
        # Maybe set isolation level
        query = ("insert into Student_Rankings values (%s,%s,%s,%s)") #IDK what the name of the actual table was

        self.cursor = self.conn.cursor()

        self.cursor.execute(query,[email, first, second, third])

        self.conn.commit()

    except psycopg2.Error as e:
            print('Error while adding claim, try again.\n' + str(e))

    def close_db(self):
        self.conn.close()


def get_rankings(self, email):
    result = []
    try:
        query = ("select first, second, third from Studnt_Rankings where email = %s");

        self.cursor = self.conn.cursor()
        self.cursor.execute(query,[email])

        self.conn.commit()

        result.append(self.cursor.fetchall())
    except psycopg2.Error as e:
            print('Error while adding claim, try again.\n' + str(e))

    return result;




def get_emails(self):
    result = []
    try:
        query = ("select email from students???");#figure out table name for student name and password

        self.cursor = self.conn.cursor()
        self.cursor.execute(query)

        self.conn.commit()

        result.append(self.cursor.fetchall())
    except psycopg2.Error as e:
            print('Error while adding claim, try again.\n' + str(e))

    return result;
     


