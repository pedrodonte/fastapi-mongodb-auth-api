from pymongo import MongoClient

MONGODB_URI = "..."

BD_PRODUCCION = 'test'


def coleccion_conexion(collection):
    client = MongoClient(MONGODB_URI)
    db = client[BD_PRODUCCION]
    coleccion = db[collection]
    return coleccion


client = MongoClient()
conn = client.test
print(type(conn))

# insert a document
#conn.user.insert_one({"name": "Saitama", "age": "23"})
