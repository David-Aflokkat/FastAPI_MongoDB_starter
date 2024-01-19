from pymongo import MongoClient

client = MongoClient("mongodb+srv://<user>:<password>@clustertest.egpmhqq.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]