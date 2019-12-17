def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db

def add_country(db):
    db.countries.insert({"name" : "India"})
    
def get_country(db):
    #return db.countries.find_one()
    return db.countries.find_all({})	

if __name__ == "__main__":

    db = get_db() 
    add_country(db)
    print get_country(db)
