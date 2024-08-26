from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, ForeignKey, text

# Criando o engine
engine = create_engine('sqlite:///:memory:')

# Criando um objeto de metadados sem schema
metadata_obj = MetaData()

# Criando a tabela 'user'
user = Table(
    'user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(30), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False),
)

# Criando a tabela 'user_prefs'
user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
)

# Criando todas as tabelas no engine
metadata_obj.create_all(engine)

# Verificando as informações da tabela 'user_prefs'
print('\nInfo da tabela user_prefs:', user_prefs)
print(user_prefs.primary_key)
print(user_prefs.constraints)

# Imprimindo as tabelas
print('\nImprimindo as tabelas:')
for table in metadata_obj.sorted_tables:
    print(table)

metadata_obj.create_all(engine)

# Criando um novo objeto de metadados
metadata_bd_obj = MetaData()

# Criando a tabela 'financial_info'
financial_info = Table(
    'financial_info', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

# Verificando as informações da tabela 'financial_info'
print('\nInfo da tabela financial_info:', financial_info)
print(financial_info.primary_key)
print(financial_info.constraints)

# Inserindo dados na tabela 'user'
with engine.connect() as connection:
    connection.execute(user.insert(), [
        {'user_name': 'John Doe', 'email_address': 'john@example.com', 'nickname': 'johnny'},
        {'user_name': 'Jane Doe', 'email_address': 'jane@example.com', 'nickname': 'jane'}
    ])

# Executando uma consulta SQL
sql = text('select * from user')
with engine.connect() as connection:
    result = connection.execute(sql)
    rows = result.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Nenhum dado encontrado na tabela 'user'")
