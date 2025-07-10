
class ucus():
    tumUcuslar=[]

    def ucusEkle():
        kalkis=input("Lütfen kalkis ilini yaziniz: ")
        varis=input("Lütfen varis ilini yaziniz: ")
        ucusId=input("Lütfen 5 rakamdan olusan ucus id'si ekleyiniz: ")

        ucus.kalkis=kalkis
        ucus.varis=varis
        ucus.ucusId=ucusId
        
        print(f"{kalkis} - {varis} arasindaki {ucusId} id'li ucus eklendi")
        ucus.tumUcuslar.append([kalkis,varis,ucusId])
        



    def ucusGöster():
        if ucus.tumUcuslar==[]:
            print("Gosterilecek ucus yok!!")
        else:
            for x in ucus.tumUcuslar:
                print(f"Ucus: {x[0]}-{x[1]} Id:{x[2]} ") 
                for y in yolcu.tumYolcular:
                    print(f"Isim: {y[0]} {y[1]} Koltuk: {y[3]}")
              
    


    


class yolcu():
    tumYolcular=[]
    koltuklar=[]
    for x in range(1,41):
        koltuklar.append(x)

    def yolcuEkle():
        if ucus.tumUcuslar==[]:
            print("Ucus yok! Lütfen önce ucus ekleyin!")

        else: 
            print("Sirasi ile kalkis ve varis yerlerini giriniz: ")
            kal=input()
            var=input()
            for ucuss in ucus.tumUcuslar:
                if ucuss[0]==kal and ucuss[1]==var:

                    print("Ucus bulundu!")  
                    ad=input("Yolcu ismini giriniz: ")
                    soyad=input("Yolcu soyismini giriniz: ")
                    tc=input("Yolcu tc'sini giriniz: ")
                    yolcu.ad=ad
                    yolcu.soyad=soyad
                    yolcu.tc=tc
                    while True:
                        koltukNo=input("Lütfen 1-40 arasinda bir sayi yazarak koltuk numaranizi seçiniz: ")
                        if int(koltukNo)<1 or int(koltukNo)>40:
                            print("Aralik disinda veri girdiniz! ")
                            continue
                        
                        else:
                            for koltuk in yolcu.koltuklar:
                                if int(koltukNo)==koltuk:
                                    yolcu.koltuklar.remove(koltuk)
                                    print(f"İsim:{ad} {soyad} Tc:{tc} kullanicisi {ucuss[2]} ucusunda {koltukNo}. koltuğa eklenmiştir.")
                                    yolcu.tumYolcular.append([ad,soyad,tc,koltukNo])
                                    break
                                else:
                                    print("Koltuk dolu! Başka koltuk seçiniz")
                                    continue
                        break
                       

                else:
                    print("Istenilen ucus bulunamadi!") 

                  

    def yolcuSil():
        if yolcu.tumYolcular==[]:
            print("Hic yolcu yok!!Yolcu eklediğinizden emin olun.")
        else:
            silinecekTc=input("Lutfen silmek istediğiniz yolcunun tcsini giriniz: ")
            for yolcu1 in yolcu.tumYolcular:
                if silinecekTc== yolcu1[2]:
                    yolcu.tumYolcular.remove(yolcu1)
                    yolcu.koltuklar.append(yolcu1[3])
                    print(f"{silinecekTc} tc'li yolcu silindi! ")

                else:
                    print(f"{silinecekTc} tc'li yolcu bulunamadi!")







while True: 
    kullaniciAdi="azra"               
    sifre="simurg25"    
    
    kulAd=input("Lütfen kullanici adini giriniz: ")
    print("Cikis yapmak icin q tuşlayabilirsiniz.")
    if kulAd=="q":
        break

    elif kulAd!=kullaniciAdi:
        print("Kullanici adi eslesmedi!!!")

    else :
        print("Kullanici adi basarili!")
        while True:
            sif=input("Lütfen sifrenizi giriniz: ")
            print("Cikis yapmak icin q tuşlayabilirsiniz.")
            if sif=="q":
                break
            elif sif!=sifre:
                print("Sifre yanliş!!!")
            else:
                print("Giriş başarili :)")
                break
        break

while True:

    print(" 1-Ucus Ekle \n 2-Yolcu Ekle \n 3-Yolcu Sil \n 4-Ucuslari Göster\n 5-Cikis\n")
    menuSecim=input("Lütfen menüden seçtiğiniz sayiyi giriniz: ")
    if menuSecim=="1":
        ucus.ucusEkle()
    elif menuSecim=="2":
        yolcu.yolcuEkle()
    elif menuSecim=="3":
        yolcu.yolcuSil()
    elif menuSecim=="4":
        ucus.ucusGöster()
    elif menuSecim=="5":
        break
    else:
        print("Lutfen menude olan bir sayi seçimi yapiniz!!")