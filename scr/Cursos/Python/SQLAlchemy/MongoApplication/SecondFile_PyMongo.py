from pprint import pprint
import pymongo
import pymongo as pyM

uri = "mongodb+srv://Walmir11:Ginecas10@wcluster.hlrtn.mongodb.net/?retryWrites=true&w=majority&appName=WCluster"
# crianção do cliente
client = pyM.MongoClient(uri)
db = client.test
posts = db.posts
# inserção de um documento
print(db.posts)

for post in posts.find():
    pprint(post)

# Toda vez que é executado o código, um novo documento é inserido
print('*'*50)
print('Total de documentos na coleção posts')
print(posts.count_documents({}))

print('*'*50)
print('Total de documentos na coleção posts com o autor Mike')
print(posts.count_documents({'author' : 'Mike'}))

print('*'*50)
print('Total de documentos na coleção posts com a tag insert')
print(posts.count_documents({'tags' : 'insert'}))

print('*'*50)
print('Recuperação de um documento com a tag insert')
pprint(posts.find_one({'tags' : 'insert'}))

print('*'*50)
print('Recuperando infos da coleção de forma ordenada pela data')
for post in posts.find().sort('date'):
    pprint(post)

print('*'*50)
# Cria um índice na coleção posts para o campo author de forma ascendente
result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print('Informações sobre os índices da coleção profiles')
pprint(sorted(list(db.profiles.index_information())))

user_profile = [
    {'user_id' : 211, 'name' : 'Luke'},
    {'user_id' : 212, 'name' : 'Solo'}]

# Inserção de vários documentos
result = db.profiles_user.insert_many(user_profile)

print('*'*50)
print('Coleções armazenadas no mongoDB\n')
for x in db.list_collection_names():
    print(x)

# Exemplo de delete_one
print('*'*50)
print('Deletando um documento com o autor Mike')
result = posts.delete_one({'author': 'Mike'})
print(f'Documentos deletados: {result.deleted_count}')

# Exemplo de delete_many
print('*'*50)
print('Deletando todos os documentos com a tag insert')
result = posts.delete_many({'tags': 'insert'})
print(f'Documentos deletados: {result.deleted_count}')

# Exemplo de drop
print('*'*50)
print('Deletando a coleção posts')
db['posts'].drop()

# Deletando o banco de dados
client.drop_database('test')
