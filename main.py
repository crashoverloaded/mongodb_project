import pymongo

# Connecting to mongodb
client = pymongo.MongoClient("mongodb+srv://crashoverload:password@priyank.quin4el.mongodb.net/?retryWrites=true&w=majority")

# testing connection
db = client.test
print(db)

d = {
    "name":"priyank",
      "surname":"agarwal",
      "email_id": "priyank@gmail.com"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
