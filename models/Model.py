from models import Connect
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

    def all_events(self):
      self.curseur=self.con.cursor()
      self.curseur.execute("""SELECT e.title,e.date,e.description FROM events AS e JOIN messages AS m ON u.id=m.id_auteur;""")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows


