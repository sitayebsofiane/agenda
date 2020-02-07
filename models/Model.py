import psycopg2
import hashlib
import calendar
from datetime import datetime

class Model:

    """ connect to bdd in postgreSQL """
    def __init__(self,bdd,user,password,host,port):
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

    """ method which returns the role_name according to id_role """
    def role_name(self,id_role):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("SELECT role_name FROM roles WHERE id_role= %s;",(id_role,))
            role_name = self.curseur.fetchone()[0]
            self.curseur.close()
            return role_name
        except(Exception ,psycopg2.Error):
            print("role has not exist")

    """ create count user_agenda """
    def creation_count_user(self,name,firstname,password):
        try:
            password = password.encode()
            password = hashlib.sha1(password).hexdigest()
            self.curseur = self.con.cursor()
            self.curseur.execute("INSERT INTO user_agenda(name,first_name,password) VALUES (%s,%s,%s);",(name,firstname,password))
            self.con.commit()
            self.curseur.close()
            return True
        except(Exception ,psycopg2.Error):
            return False

    """ add role X for user Y """
    def add_role_user(self,name,first_name,role_name):
        #i select user by his id and affecte hime role 
        self.curseur = self.con.cursor()
        self.curseur.execute("SELECT id_user FROM user_agenda where name= %s AND first_name= %s;",(name,first_name))
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
        try:
            self.curseur=self.con.cursor()
            self.curseur.execute("""SELECT e.title,e.date,e.description,r.role_name,r.role_description,u.name,u.first_name
                                    FROM events AS e JOIN user_agenda AS u
                                    ON u.id_user=e.id_user JOIN user_role AS ur ON ur.id_user=u.id_user JOIN
                                    roles AS r ON ur.id_role=r.id_role;""")
            rows=self.curseur.fetchall()
            self.curseur.close()
            liste = list()
            for row in rows:
                liste.append({'title':row[0],'date': row[1], 'description':row[2],'role':row[3], 'role_description': row[4]
                ,'name':row[5],'firstName': row[6]})
            return liste
        except(Exception ,psycopg2.Error):
            print("erreur while  while selecting")

    
    """ get all events with restreint information """
    def get_all_events_by_user(self):
        try:
            self.curseur=self.con.cursor()
            self.curseur.execute("""SELECT e.title,e.date,r.role_name,u.name FROM events AS e JOIN user_agenda AS u
                                        ON u.id_user=e.id_user JOIN user_role AS ur ON ur.id_user=u.id_user JOIN
                                        roles AS r ON ur.id_role=r.id_role;""")
            rows=self.curseur.fetchall()
            self.curseur.close()
            liste = list()
            for row in rows:
                liste.append({'title':row[0],'date': row[1],'role':row[2],'name':row[3]})
            return liste
        except(Exception ,psycopg2.Error):
            print("erreur while selecting")

    
    """ post one event by admin """ 
    def post_event(self,id_user,title,date,description):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("INSERT INTO events(id_user, title, date, description)VALUES (%s,%s,%s,%s);",(id_user,title,date,description))
            self.con.commit()
            self.curseur.close()
            return True
        except:
            return False

    """ update event ,this method allows to update,
     admin has the right on everything, the user has the right just on what entered """
    def update_event_admin(self,new_title,date,description,title):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("UPDATE events SET title=%s,date=%s,description=%s WHERE title=%s;",
            (new_title,date,description,title))
            self.con.commit()
            self.curseur.close()
            return True
        except(Exception ,psycopg2.Error):
            return False


    """ event update, this method allows,the user to update just on what came in"""
    def update_event_user(self,new_title,date,title,id_user):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("UPDATE events SET title=%s,date=%s WHERE title=%s AND id_user=%s;",
            (new_title,date,title,id_user))
            self.con.commit()
            self.curseur.close()
            return True
        except(Exception ,psycopg2.Error):
            return False

    """ delete event by admin """
    def delete_event_admin(self,title):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("DELETE FROM events WHERE title=%s",(title,))
            self.con.commit()
            self.curseur.close()
            return True
        except(Exception ,psycopg2.Error):
            return False


    """ delete event by user """
    def delete_event_user(self,title,id_user):
        try:
            self.curseur = self.con.cursor()
            self.curseur.execute("DELETE FROM events  WHERE title=%s AND id_user=%s;",(title,id_user))
            self.con.commit()
            self.curseur.close()
            return True
        except(Exception ,psycopg2.Error):
            return False