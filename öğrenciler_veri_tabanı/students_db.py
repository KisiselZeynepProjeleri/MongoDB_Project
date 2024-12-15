from mongodb_connect import MongoDBConnection

class StudentsDB(MongoDBConnection):
    def __init__(self, db_name):
        super().__init__()
        self.collection=self.database_getir(db_name)['ögrenciSkorları']

    def ögrenci_skorları_ekleme(self,data:dict):
        self.collection.insert_many(data)
    
    def toplam_puan_sorgulama(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':"$user",
                    "Toplam_Puanlar":{'$sum':'$score'}
                }
            }
        ])
    #öğrencilere göre gruplama yap ve her öğrencinin kaç tane ders aldığını topla

    def toplam_ders_sorgulama(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':"$user",
                    "Toplam_Dersler":{'$sum': 1}
                }
            }
        ])
    
    #öğrencileri _id olarak tanımlayın ve öğrencilere göre gruplayın. buna karşılık olarak her öğrencinin toplam derslerden aldığı ortalama notu hesapla
    #-->avg ortalama alıyor

    def ortalama_hesapla(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':"$user",
                    "ortalama_notlar":{'$avg': '$score'}
                }
            }
        ])
    
    