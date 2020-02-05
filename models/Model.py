import psycopg2
import hashlib
import calendar
from getpass import getpass
from datetime import datetime

class Model:

    """ connect to bdd in postgreSQL """
    def __init__(self,bdd="ecole",user="postgres",password="as122014",host="localhost",port="5432"):
        try:
            self.con=psycopg2.connect(database=bdd,user=user,password=password,host=host,port=port)
            self.curseur=None
        except(Exception ,psycopg2.Error):
            print("erreur while connecting to postgresSQL")


    """ authentification of user """
    def authentification(self,name,first_name,password):
       autorised = False
       password = hashlib.sha1(password.encode()).hexdigest()
       self.curseur=self.con.cursor()
       self.curseur.execute("SELECT name,first_name,password FROM user_agenda;")
       rows=self.curseur.fetchall()
       for row in rows:
           if row[0]==name and row[1]==first_name and row[2]==password:
               autorised = True
               break
       self.curseur.close()
       return autorised

    """ create count user_agenda """
    def creation_count_user(self,name,firstname,password):
        password = password.encode()
        password = hashlib.sha1(password).hexdigest()
        self.curseur = self.con.cursor()
        self.curseur.execute("INSERT INTO user_agenda(name,first_name,password) VALUES (%s,%s,%s);",(name,firstname,password))
        self.con.commit()
        self.curseur.close()

    """ add role X for user Y """
    def add_role_user(self,id_user,role_name):
        #i select user by his id and affecte hime role 
        self.curseur = self.con.cursor()
        self.curseur.execute("SELECT id_user FROM user_agenda where id_user= %s;",(id_user,))
        user=self.curseur.fetchone()
        self.curseur.execute("SELECT id_role FROM roles where role_name= %s;",(role_name,))
        id_role = self.curseur.fetchone()
        if user is not None and id_role is not None:
            self.curseur.execute("INSERT INTO user_role(id_user,id_role) VALUES (%s,%s);",(id_user,id_role))
            self.con.commit()
            self.curseur.close()
            return True
        return False
        
        


    """ get all events """
    def get_all_events(self):
      self.curseur=self.con.cursor()
      self.curseur.execute("""SELECT e.title,e.date,e.description,r.role_name,r.role_description,u.name FROM events AS e JOIN user_agenda AS u
                                ON u.id_user=e.id_user JOIN roles AS r ON r.id_role=e.id_role;""")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows


