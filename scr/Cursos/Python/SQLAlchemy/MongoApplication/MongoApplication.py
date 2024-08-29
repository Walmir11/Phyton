from datetime import datetime

import pymongo as pyM

uri = "mongodb+srv://Walmir11:<db_password>@wcluster.hlrtn.mongodb.net/?retryWrites=true&w=majority&appName=WCluster"
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
