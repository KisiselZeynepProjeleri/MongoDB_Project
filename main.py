from books_db import BooksDB

def main():
    booksdb=BooksDB('Students')
    books_data=[
        {
            "_id": 1,
            "title": "abc123",
            "isbn": "0001122223334",
            "author": {"last": "zzz", "first": "aaa"},
            "copies": 5
        },
        {
            "_id": 2,
            "title": "Baked Goods",
            "isbn": "9999999999999",
            "author": {"last": "xyz", "first": "abc", "middle": ""},
            "copies": 2
        }
    ]
    booksdb.kitap_ekleme(books_data)

    for veri in booksdb.kitap_id_ve_isim_sorgulama():
        print(veri)
    
if __name__=='__main__':
    main()