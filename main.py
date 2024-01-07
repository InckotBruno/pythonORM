from database import db, Pacientes, Consultas


#faz conexao
db.connect()
db.create_tables([Pacientes, Consultas])

# Teste para criar um usuário
# usuario = Pacientes.create(nome="carlos", email='teste@teste.com', senha='123')

#usuario.create(nome="Bruno", email="teste1@teste.com", senha="123")


# Criando alguns usuários para teste

# usuario1 = Pacientes.create(nome="Sergio", email='teste0@teste.com', senha='123')
# usuario2 = Pacientes.create(nome="Santana", email="teste2@teste.com", senha="123")
# usuario3 = Pacientes.create(nome="Exemplo", email="exemplo@teste.com", senha="456")

# Imprimir informações sobre os usuários
# print("Novo usuário 1:", usuario1.id, usuario1.nome, usuario1.email)
# print("Novo usuário 2:", usuario2.id, usuario2.nome, usuario2.email)
# print("Novo usuário 3:", usuario3.id, usuario3.nome, usuario3.email)

# Verificando o usuario na tabela
# usuario1 = Pacientes.get(Pacientes.id == 2)
# print("Usuário encontrado:", usuario1.id, usuario1.nome, usuario1.email)

# Santana = Pacientes.get(Pacientes.email == "teste2@teste.com")
# Santana.nome = "Santana Shaolyn Matador de porco"
# Santana.save()
# print("Santana atualizado", Santana.nome)

# Criando consultas para os usuários existentes
# Consultas.create(usuario=Pacientes.get(Pacientes.id == 1), titulo="Consulta 1", descricao="Descrição da consulta 1")
# Consultas.create(usuario=Pacientes.get(Pacientes.id == 2), titulo="Consulta 2", descricao="Descrição da consulta 2")
# Consultas.create(usuario=Pacientes.get(Pacientes.id == 3), titulo="Consulta 3", descricao="Descrição da consulta 3")
# Consultas.create(usuario=Pacientes.get(Pacientes.id == 4), titulo="Consulta 4", descricao="Descrição da consulta 4")
# Consultas.create(usuario=Pacientes.get(Pacientes.id == 3), titulo="Consulta 5", descricao="Descrição da consulta 5")


# Modificar o título da consulta 
# consulta_para_modificar = Consultas.get(Consultas.id == 5)
# consulta_para_modificar.titulo = "Psiquiatra"
# consulta_para_modificar.save()

# excluir duplicado
# Consultas.delete().where(Consultas.id >= 6).execute()



# Atualizar descrição para o que foi atendido
# Consultas.update(descricao='Paciente biluteteia').where(Consultas.titulo == 'Psiquiatra').execute()

# Imprimir todos os registros da tabela Pacientes
print("Registros da tabela Pacientes:")
for paciente in Pacientes.select():
    print(f"ID: {paciente.id}, Nome: {paciente.nome}, Email: {paciente.email}, Senha: {paciente.senha}")

# Imprimir todos os registros da tabela Consultas
print("\nRegistros da tabela Consultas:")
for consulta in Consultas.select():
    print(f"ID: {consulta.id}, Paciente: {consulta.usuario.nome}, Especialidade: {consulta.titulo}, Descrição: {consulta.descricao}")

    