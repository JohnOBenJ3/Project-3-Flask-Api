import os ##NEW
import datetime
from peewee import *
from flask_login import UserMixin
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:    
    DATABASE = SqliteDatabase('shelters.sqlite')



# DATABASE = PostgresqlDatabase(
# 'shelter',
# user= 'orrinjohnson',
# password = 'password',
# host = 'localhost'
# )
#sqlite is good for development because they are easy to change
#when the app is ready you would move to postgres


class Shelter(Model):
    # id = PrimaryKeyField(null=False)
    address = CharField(null=True, default='')
    city = CharField(null=True, default='')
    name = CharField(null=True, default='')
    shelter_id = CharField(null=True, default='')
    phone = CharField(null=True, default='')
    class Meta:
        database_table = 'shelters'
        database = DATABASE



class Animal(Model):
    # id = PrimaryKeyField(null=False)
    name = CharField()
    shelter = ForeignKeyField(Shelter, backref='shelter_specs', null=True, default=1)
    breed = CharField()
    age = CharField()
    gender = CharField()
    photo = CharField()
    description = CharField()
    class Meta:
        database_table = 'animals'
        database = DATABASE

class Admin(UserMixin, Model):
    # id = PrimaryKeyField(null=False)
<<<<<<< HEAD
    
=======
>>>>>>> master
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database_table = 'admin'
        database = DATABASE


def initialize(): #just a method. can be named anything but if initialize makes sense, keep using it
    DATABASE.connect() #connect to db
    DATABASE.create_tables([Shelter, Animal, Admin], safe=True) #make sure the table is created. DON'T ERASE!!!!!<-- <--
    print("TABLES Created")

    if (Shelter.select().count() == 0):
        created_shelter = Shelter.create(
            name='Fake Shelter',
            city='Denver'
        )
        Animal.create(
            name='Otis',
            shelter=created_shelter,
            breed='horse',
            age=1,
            gender='Male',
            photo='photo',
            description='Good horse'
        )

    DATABASE.close() #after it works, close the connection so there are not threats to an open database

    # {
    #     "address":
    #     "city":
    #     "name":
    #     "shelter_id":
    #     "phone":
    # }

    # {
    #     "name":
    #     "shelter":
    #     "breed":
    #     "age":
    #     "gender":
    #     "photo":
    #     "description":
    # }