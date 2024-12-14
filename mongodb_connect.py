from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self,url='mongodb+srv://zeynepcolakbozkurt:4791613Ev.@deneme1.86go0.mongodb.net/'):
        self.client=MongoClient(url)


    def database_getir(self,db_name):
        return self.client[db_name]