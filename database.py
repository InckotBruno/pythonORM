from peewee import *

db = SqliteDatabase('consultas.db')

class Pacientes(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    
    class Meta:
        database = db

class Consultas(Model):
    usuario = ForeignKeyField(Pacientes, backref='usuarios') # criei errado como usuário n fica didatico
    titulo = CharField()
    descricao = TextField()

    class Meta:
        database = db
