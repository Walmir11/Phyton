from datetime import datetime
from pprint import pprint
import pymongo as pyM

uri = "mongodb+srv://Walmir11:Ginecas10@wcluster.hlrtn.mongodb.net/?retryWrites=true&w=majority&appName=WCluster"

# crianção do cliente
client = pyM.MongoClient(uri)

# criação do banco de dados
db = client.test

# criação da coleção
collection = db.test_collection

# inserção de um documento
print(db.test_collection)

# Definição de um documento
post = {
    'author' : 'Mike',
    'text' : 'My first mongodb application based on python',
    'tags' : ['mongodb', 'python3', 'pymongo'],
    'date' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Preparação para inserção do documento
posts = db.posts
post_id = posts.insert_one(post).inserted_id
# impressão do id do documento
print(post_id)

# Listagem de coleções
print(db.list_collection_names())

# Mostra o primeiro documento
#print(db.posts.find_one())

print('*'*50)
# Mostra todos os documentos de maneira mais organizada
pprint(posts.find_one())

# bulk inserts
new_posts = [{'author' : 'Mike',
              'text' : 'Another post',
              'tags' : ['bulk', 'insert'],
              'date' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
             {
                 'author' : 'Eliot',
                 'title' : 'MongoDB is fun',
                 'text' : 'and pretty easy too!',
                 'date' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

result = posts.insert_many(new_posts)
print('*'*50)
# Mostra os ids dos documentos inseridos
print(result.inserted_ids)
print('Recuperação final')
pprint(db.posts.find_one({'author' : 'Eliot'}))

print('*'*50)
print('Documentos recuperados na coleção posts')
# Mostra todos os documentos de maneira mais organizada
for post in posts.find():
    pprint(post)
