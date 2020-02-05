import psycopg2
import hashlib
import calendar
from datetime import datetime

class Model:

    """ connect to bdd in postgreSQL """
    def __init__(self,bdd="ecole",user="postgres",password="as122014",host="localhost",port="5432"):
        try:
            self.con=psycopg2.connect(database=bdd,user=user,password=password,host=host,port=port)
            self.curseur=None
        except(Exception ,psycopg2.Error):
            print("erreur while connecting to postgresSQL")


    """ if user has authentificat this method return id_user and id_role """
    def authentification(self,name,first_name,password):
       autorised = False
       id_role=None
       password = hashlib.sha1(password.encode()).hexdigest()
       self.curseur=self.con.cursor()
       self.curseur.execute("SELECT id_user,name,first_name,password FROM user_agenda;")
       rows=self.curseur.fetchall()
       for row in rows:
           if row[1]==name and row[2]==first_name and row[3]==password:
               autorised = True
               id_user=row[0]
               self.curseur.execute("SELECT id_role FROM user_role where id_user=%s;",(id_user,))
               id_role=self.curseur.fetchone()
               break
       self.curseur.close()
       if id_role is not None:
           return autorised,id_user,id_role[0]
       return False,

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
        id_user=self.curseur.fetchone()
        self.curseur.execute("SELECT id_role FROM roles where role_name= %s;",(role_name,))
        id_role = self.curseur.fetchone()
        if id_user is not None and id_role is not None:
            self.curseur.execute("INSERT INTO user_role(id_user,id_role) VALUES (%s,%s);",(id_user,id_role))
            self.con.commit()
            self.curseur.close()
            return True
        return False
        
    """ add new role in table roles """
    def add_new_role(self,role_name,role_description):
        self.curseur = self.con.cursor()
        self.curseur.execute("INSERT INTO roles(role_name,role_description) VALUES (%s,%s);",(role_name,role_description))
        self.con.commit()
        self.curseur.close()

    """ update role X for user Y """
    def update_user_role(self,id_user,new_role_name):
        #i select user by his id and affecte hime role
        self.curseur = self.con.cursor()
        self.curseur.execute("SELECT id_user FROM user_agenda WHERE id_user= %s;",(id_user,))
        id_user=self.curseur.fetchone()
        self.curseur.execute("SELECT id_role FROM roles WHERE role_name= %s;",(new_role_name,))
        id_role = self.curseur.fetchone()
        if id_user is not None and id_role is not None:
            self.curseur.execute("UPDATE user_role set id_role=%s WHERE id_user=%s;",(id_role,id_user))
            self.con.commit()
            self.curseur.close()
            return True
        return False



    """ get all events with all informations """
    def get_all_events_by_admin(self):
      self.curseur=self.con.cursor()
      self.curseur.execute("""SELECT e.title,e.date,e.description,r.role_name,r.role_description,u.name FROM events AS e JOIN user_agenda AS u
                                ON u.id_user=e.id_user JOIN user_role AS ur ON ur.id_user=u.id_user JOIN
								roles AS r ON ur.id_role=r.id_role;""")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows
    
    """ get all events with restreint information """
    def get_all_events(self):
      self.curseur=self.con.cursor()
      self.curseur.execute("""SELECT e.title,e.date,r.role_name,u.name FROM events AS e JOIN user_agenda AS u
                                ON u.id_user=e.id_user JOIN user_role AS ur ON ur.id_user=u.id_user JOIN
								roles AS r ON ur.id_role=r.id_role;""")
      rows=self.curseur.fetchall()
      self.curseur.close()
      return rows
    
    """ post one event """ 
    def post_event(self,id_user,id_role,title,date,description):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("SELECT role_name FROM roles WHERE id_role= %s;",(id_role,))
            role_name = self.curseur.fetchone()[0]
            print(role_name)
            if role_name == 'ADMIN':
                self.curseur.execute("INSERT INTO events(id_user, title, date, description)VALUES (%s,%s,%s,%s);",(id_user,title,date,description))
                self.con.commit()
            elif role_name == 'USER':
                self.curseur.execute("INSERT INTO events(id_user, title, date)VALUES (%s,%s,%s);",(id_user,title,date))
                self.con.commit()

            self.curseur.close()
            return True
        except:
            return False

    


