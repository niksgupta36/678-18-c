import pymongo

def connectDatabase():
    url = 'mongodb+srv://admin:admin@cluster0-v0u4h.mongodb.net/test?retryWrites=true'
    client = pymongo.MongoClient(url)
    db = client.test
    return db