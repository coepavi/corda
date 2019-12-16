from pymongo import MongoClient
client = MongoClient()

client = MongoClient('mongodb://localhost:27017')

db = client.iotdb

iot = db.iot

a = "IoT"
# get input from user to store in mongodb
c = input("Enter numbers: ")		

post_data = {
    'title': a,
    'content': c
}

# insert record in mongodb
result = iot.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

# Query mongodb for single reocrd
get_data = iot.find_one({'title': 'IoT'})
print(get_data)

# Query mongodb for all records
for document in iot.find():
    print (document)
