from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class User(Base):
    # Inicia uma tabela
    __tablename__ = 'user_account'
    # Atributos
    id = Column(Integer , primary_key=True)
    name = Column(String(10))
    fullname = Column(String(30))

    # Relacionamento, back_populates -> Faz a relação entre as tabelas
    # cascade='all, delete-orphan' -> Se o objeto for deletado, deleta o objeto relacionado
    address = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User (id = {self.id}, name = {self.name}, fullname = {self.fullname})'

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    # nullable=False -> Não pode ser nulo
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    # Relacionamento, back_populates -> Faz a relação entre as tabelas
    user = relationship('User' , back_populates='address')

    # Representação da classe
    def __repr__(self):
        return f'Address (id = {self.id}, email = {self.email_address} )'

print(User.__tablename__)
print(Address.__tablename__)

# Conexão com o banco de dados
engine = create_engine('sqlite://')

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Inspeção do banco de dados, posso recuperar informações sobre o banco de dados
inspetor_engine = inspect(engine)

# Verificar se a tabela existe
print(inspetor_engine.has_table('user_account'))

# Recuperar o nome das tabelas
print(inspetor_engine.get_table_names())

# Recuperar o nome do schema
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    walmir = User(
        name='Walmir',
        fullname='Walmir Neto',
        address=[Address(email_address='walmirneto@email.com')]
    )

    ana = User(
        name='Ana',
        fullname='Ana Luiza',
        address=[Address(email_address='anaolimene@email.com'),
                 Address(email_address='anamenezes@email.com')]
    )

    patrick = User(
        name='Patrick',
        fullname='Patrick Neto'
    )

    # Adicionando os objetos ao banco de dados(persistencia de dados)
    session.add_all([walmir, ana, patrick])

    # Commitando as alterações
    session.commit()

# Consulta de nomes
stmt = select(User).where(User.name.in_(["Walmir", 'Ana']))
print('~'*60)
print('Imprimindo nomes')
for user in session.scalars(stmt):
    print(user)

# Consulta de endereços
stmt_address = select(Address).where(Address.id.in_([1]))
print('~'*60)
print('Imprimindo 1 email')
# Retorna um email
print(session.scalar(stmt_address))

stmt_address2 = select(Address).where(Address.user_id.in_([2]))
print('~'*60)
print('Imprimindo emails')
# Retorna todos os emails
for address in session.scalars(stmt_address2):
    print(address)

# Printa a função sql de uma consulta
print('~'*60)
print(select(User).order_by(User.fullname.desc()))

# Ordenando os nomes
stmt_order = select(User).order_by(User.fullname.desc())
print('~'*60)
print('Imprimindo nomes em ordem')
for i in session.scalars(stmt_order):
    print(i)

stmt_join = select(User.fullname, Address.email_address).join_from(User, Address)
print('~'*60)
print('Imprimindo join')
for i in session.scalars(stmt_join):
    print(i)

print('~'*60)
# Printa a função sql de uma consulta
print(select(User.fullname, Address.email_address).join_from(User, Address))

print('~'*60)
print('Outra forma de imprimir o join')
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for i in results:
    print(i)

stmt_count = select(func.count('*')).select_from(User)
print('~'*60)
print('Contando o número de usuários')
for i in session.scalars(stmt_count):
    print(i)

session.close()
