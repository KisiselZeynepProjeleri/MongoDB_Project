from mongodb_connect import MongoDBConnection

class BooksDB(MongoDBConnection):
    def __init__(self, db_name):
        super().__init__()
        self.collection=self.database_getir(db_name)['Books']

    def kitap_ekleme(self,data:dict):
        self.collection.insert_many(data)

    def kitap_id_ve_isim_sorgulama(self):
        return self.collection.aggregate([
            {'$project':{'title':1,'isbn':1}} #pandastaki count() methodu ile aynı işi yapar
        ])