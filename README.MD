###################  Estudo sobre ODM (Object-Document Mapping) em Python ###############

Introdução ao ODM
ODM, ou Object-Document Mapping, é um conceito que se assemelha ao ORM (Object-Relational Mapping), mas é aplicado a bancos de dados NoSQL, especialmente em contextos de banco de dados orientado a documentos. Enquanto o ORM mapeia objetos para tabelas em bancos de dados relacionais, o ODM mapeia objetos para documentos em bancos de dados orientados a documentos, como MongoDB.

Por que usar ODM?
Flexibilidade de Esquema:

Bancos de dados orientados a documentos, como o MongoDB, oferecem flexibilidade de esquema, o que significa que diferentes documentos na mesma coleção podem ter campos diferentes. Um ODM gerencia essa flexibilidade de forma eficaz.
Trabalhar com Objetos Python:

ODM permite que você trabalhe com objetos Python diretamente, sem a necessidade de tradução entre tipos de dados do banco de dados e tipos de dados da aplicação.
Integração com Frameworks Web:

Muitos ODMs são integrados a frameworks web populares, facilitando a construção de aplicativos web em Python com bancos de dados NoSQL.
Principais Conceitos em ODM
1. Documentos:
Em ODM, os documentos correspondem aos objetos Python que são armazenados no banco de dados orientado a documentos. Cada documento representa uma entidade no sistema.
2. Coleções:
Uma coleção é um grupo lógico de documentos no banco de dados. Cada tipo de documento é armazenado em sua própria coleção.
3. Campos:
Campos em um documento correspondem a atributos ou propriedades do objeto Python. Cada campo pode ter um tipo específico.
4. Querying (Consultas):
ODMs oferecem maneiras de realizar consultas no banco de dados usando uma sintaxe que é mais próxima da linguagem de programação utilizada (Python).
Exemplos de ODM em Python
MongoEngine:

MongoEngine é um ODM popular para MongoDB em Python. Ele fornece uma API rica e flexível para trabalhar com documentos.
Exemplo de uso do MongoEngine:

#########################################
from mongoengine import Document, StringField

class Pessoa(Document):
    nome = StringField(required=True, max_length=50)
    idade = StringField()

##########################################

PyMODM:

PyMODM é um ODM oficial do MongoDB para Python. Ele oferece uma camada de abstração simples e poderosa para interagir com o MongoDB.
Exemplo de uso do PyMODM:

##########################################

from pymodm import MongoModel, fields

class Pessoa(MongoModel):
    nome = fields.CharField(required=True)
    idade = fields.IntegerField()

##########################################

Próximos Passos
Escolha um ODM baseado nas necessidades específicas do seu projeto.
Explore a documentação oficial do ODM escolhido para aprender mais sobre suas características e funcionalidades.
Pratique a criação de modelos de documentos, a realização de consultas e outras operações comuns.
Integre o ODM escolhido em um projeto real para ganhar experiência prática.
Este codigo rodou no python 3.11

Consulte: https://www.mongodb.com/docs/


ESTE GIT SÓ TEM EFEITO DIDATICO 2024;