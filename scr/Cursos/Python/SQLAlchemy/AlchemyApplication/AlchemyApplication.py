from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()

class User(base):
    # Inicia uma tabela
    __tablename__ = 'user_account'
    # Atributos
    id = Column(Integer , primary_key=True)
    name = Column(String(10))
    fullname = Column(String(30))

    # Relacionamento, back_populates -> Faz a relação entre as tabelas
    # cascade='all, delete-orphan' -> Se o objeto for deletado, deleta o objeto relacionado
    address = relationship(
        'Adress', back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User (id = {self.id}, name = {self.name}, fullname = {self.fullname})'

class Address(base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nullable=False -> Não pode ser nulo
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    # Relacionamento
    user = relationship('User' , back_populates='adress')

    # Representação da classe
    def __repr__(self):
        return f'Adress (id = {self.id}, email = {self.email_address} )'

print(User.__tablename__)
