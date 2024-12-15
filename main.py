from öğrenciler_veri_tabanı.books_db import BooksDB
from öğrenciler_veri_tabanı.students_db import StudentsDB
from şirket_veri_tabanı.employee_db import EmployeeDB
from şirket_veri_tabanı.inventory_db import InventoryDB
def main():
    # booksdb = BooksDB('Students')
    # books_data = [
    #     {
    #         "_id": 1,
    #         "title": "abc123",
    #         "isbn": "0001122223334",
    #         "author": {"last": "zzz", "first": "aaa"},
    #         "copies": 5
    #     },
    #     {
    #         "_id": 2,
    #         "title": "Baked Goods",
    #         "isbn": "9999999999999",
    #         "author": {"last": "xyz", "first": "abc", "middle": ""},
    #         "copies": 2
    #     }
    # ]
    # booksdb.kitaplar_ekleme(books_data)

    # for veri in booksdb.kitap_id_ve_isim_sorgulama():
    #     print(veri)
    
    # students_db = StudentsDB('Students')
    # students_data = [
    #     {"user":'Emre','subject':'Database','score':80},
    #     {"user":'Zeynep','subject':'JavaScript','score':90},
    #     {"user":'Zeynep','subject':'Database','score':85},
    #     {"user":'Emre','subject':'JavaScript','score':75},
    #     {"user":'Zeynep','subject':'Data Science','score':60},
    #     {"user":'Emre','subject':'Data Science','score':95},
    # ]
    # students_db.ogrenci_skorlarını_ekleme(students_data)

    # for dersler in students_db.toplam_ders_sorgulama():
    #     print(dersler)
    
    # for toplam_puanlar in students_db.toplam_puan_sorgulama():
    #     print(toplam_puanlar)

    # for ortalama_puanlar in students_db.ogrenci_ortalama_puan_hesaplama():
    #     print(ortalama_puanlar)
    # employee_db = EmployeeDB('Employee')
    # data = {
    #     'firstname':'Emre',
    #     'lastname':'kayis',
    #     'department':'Analytics',
    #     'qualification':'BE',
    #     'age':23
    # }
    # employee_db.calisan_ekleme(data)
    # for emp in employee_db.calisanlari_gosterme():
    #     print(emp)
    # for emp in employee_db.isimlerine_gore_calisan_bulma('Emre'):
    #     print(emp)
    # for emp in employee_db.kalitesine_calisan_bulma(['BE']):
    #     print(emp)

    inventory_db=InventoryDB('Employee')
    inventory_data = [
                        {"item": "canvas", "qty": 100, "size": {"h": 28, "w": 35.5, "uom": "cm"}, "status": "A"},
                        {"item": "journal", "qty": 25, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
                        {"item": "mat", "qty": 85, "size": {"h": 27.9, "w": 35.5, "uom": "cm"}, "status": "A"},
                        {"item": "mousepad", "qty": 25, "size": {"h": 19, "w": 22.85, "uom": "cm"}, "status": "P"},
                        {"item": "notebook", "qty": 50, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "P"},
                        {"item": "paper", "qty": 100, "size": {"h": 8.5, "w": 11, "uom": "in"}, "status": "D"},
                        {"item": "planner", "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"}, "status": "D"},
                        {"item": "postcard", "qty": 45, "size": {"h": 10, "w": 15.25, "uom": "cm"}, "status": "A"},
                        {"item": "sketchbook", "qty": 80, "size": {"h": 14, "w": 21, "uom": "cm"}, "status": "A"},
                        {"item": "sketch pad", "qty": 95, "size": {"h": 22.85, "w": 30.5, "uom": "cm"}, "status": "A"}
                    ]
    inventory_db.insert_inventory_data(inventory_data)
    inventory_db.update_inventory_data('sketch pad',{'size.uom':'m','status':'P'})
    inventory_db.update_inventory_bulk({'qty':{'$lt':50}},{'size.uom':'inch','status':'P'})
if __name__ == '__main__':
    main()