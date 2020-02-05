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
      autorised=False
      password = password.encode()
      self.curseur=self.con.cursor()
      self.curseur.execute("SELECT name,first_name,password FROM user_agenda;")
      rows=self.curseur.fetchall()
      for row in rows:
         if row[0]==name and row[1]==first_name and row[2]==password:
            emira=True
            break
      self.curseur.close()
      return autorised


    def get_all_events(self):
      self.curseur=self.con.cursor()
      self.curseur.execute("""SELECT e.title,e.date,e.description,r.role_name,r.role_description,u.name FROM events AS e JOIN user_agenda AS u
                                ON u.id_user=e.id_user JOIN roles AS r ON r.id_role=e.id_role;""")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows

