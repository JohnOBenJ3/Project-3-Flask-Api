import datetime
from peewee import *
from flask_login import UserMixin

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
    id = PrimaryKeyField(null=False)
    address = CharField(null=True, default='')
    city = CharField(null=True, default='')
    name = CharField(null=True, default='')
    shelter_id = CharField(null=True, default='')
    phone = CharField(null=True, default='')
    class Meta:
        database_table = 'shelters'
        database = DATABASE



class Animal(Model):
    id = PrimaryKeyField(null=False)
    name = CharField()
    shelter = ForeignKeyField(Shelter, backref='shelter_specs')
    breed = CharField()
    age = CharField()
    gender = CharField()
    photo = CharField()
    description = CharField()
    class Meta:
        database_table = 'animals'
        database = DATABASE

class Admin(UserMixin, Model):
    id = PrimaryKeyField(null=False)
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database_table = 'admin'
        database = DATABASE


def initialize(): #just a method. can be named anything but if initialize makes sense, keep using it
    DATABASE.connect() #connect to db
    DATABASE.create_tables([Shelter, Animal, Admin], safe=True) #make sure the table is created. DON'T ERASE!!!!!<-- <--
    print("TABLES Created")
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