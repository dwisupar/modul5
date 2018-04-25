from hitung import perhitungan
class masukan (perhitungan) :
     
    print ("\n----------------------------------------------------")
    print ("List Boneka yang di jual :")
    print ("----------------------------------------------------")
    print ("1. Boneka Keropy Giant          Harga = Rp. 220.000")
    print ("2. Boneka Doraemon              Harga = Rp. 77.000")
    print ("3. Boneka Winnie The Pooh Besar Harga = Rp. 55.000")
    print ("4. Boneka Big Beruang           Harga = Rp. 110.000")
    print ("5. Boneka Little Pony Sedang    Harga = Rp. 38.500")
    print ("6. Exit")
    print ("----------------------------------------------------")

    menu = float(input("PILIH NOMOR BERAPA : "))
    hitung = perhitungan()
    if menu == 1:
        hitung.bonekapil1()
    elif menu == 2:
        hitung.bonekapil2()
    elif menu == 3:
        hitung.bonekapil3()
    elif menu == 4:
        hitung.bonekapil4()
    elif menu == 5:
        hitung.bonekapil5()
    elif menu == 6:
        exit()
    else:
        print ("Maaf angka yang anda masukan tidak terdaftar di list")


