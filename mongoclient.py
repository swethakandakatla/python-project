import datetime
from pymongo import MongoClient

client=MongoClient('localhost' ,27017)
#another way to create a Mongo DB connection
# client = MongoClient(“mongodb://localhost:27017/”)
mydb=client[name of the database]
#another way 
client.nameofthedatabase
post = {"author": "Mike" ,    
        "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
posts = mydb.posts
post_id = posts.insert_one(post)
# we usual use insert_one
post_id = posts.insert_many(post)
#another way of inserting data
REC = nameofthedatabase.insert_one(post)
#querying the document
for i in mydb.nameofthedatabase.find({title: 'MongoDB and Python'}) 
    print(i)
    #to find the number of documents, count
for i in mydb.nameofthedatabase.count({title: 'MongoDB and Python'}) 
    print(i)
print(mydb.nameofthedatabase.find({title: 'MongoDB and Python'}).count()) 

result=mydb.nameofthedatabase.delete_many({"category":"food"})

result = mydb.nameofthedatabase.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})