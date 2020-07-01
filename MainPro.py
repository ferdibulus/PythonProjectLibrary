from LibraryPro import *

print("""*****************************************************

Welcome To RBF library

Operations:

1. Show Books

2. Query Book

3. Add Book

4. Delete Book

5. Improve Baski

For EXIT press "q"
******************************************************""")

kutuphane = Kutuphane()
while True:
    islem = input("Select an operation: ")

    if(islem == "q"):
        print("Program will be helted..")
        print("Come Again")
    elif(islem == "1"):
        kutuphane.kitaplari_goster()
    elif(islem == "2"):
        isim = input("Which book are you want? :")
        print("The book is searching.. Please Wait a Minute")
        time.sleep(1)
        kutuphane.kitap_sorgula(isim)
    elif(islem == "3"):
        isim= input("Book Name: ")
        yazar= input(" Author Name: ")
        yayinevi= input("Publisher: ")
        tur = input("Type: ")
        baski = int(input("Edition: "))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("New book is adding..")
        time.sleep(1)

        kutuphane.kitap_ekle(yeni_kitap)

    elif(islem == "4"):
        isim = input("Which book will deleted?:")
        cevap = input("Are you sure?(Y/N)")
        if(cevap=="Y"):
            print("Deleting book")
            time.sleep(1)
            kutuphane.kitap_sil(isim)
            print("The book was deleted")
        else:
            print("The delete operation was not run.")

    elif(islem == "5"):
        isim = input("Which book'edition will update?:")
        print("Updating book edition")
        time.sleep(1)
        kutuphane.baski_yukselt(isim)
    else:
        print("Wrong Operation Please select a correct operation")