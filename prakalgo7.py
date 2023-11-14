# elkom 1
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

def faktorial (x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * faktorial (x - 1)

bilangan = int(input("Nilai: "))
hasil_faktorial = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil_faktorial}")


# elkom 2
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

def hitung_vokal_dan_konsonan(kalimat):
    vokal = 0
    konsonan = 0

    # Mengubah kalimat menjadi huruf kecil untuk memudahkan penghitungan
    kalimat = kalimat.lower()

    # Mengumpulkan kumpulan huruf vokal
    huruf_vokal = "aiueo"
    
    for huruf in kalimat:
        if huruf.isalpha():
            if huruf in huruf_vokal:
                vokal += 1
            else:
                konsonan += 1

    return vokal, konsonan

kalimat = input("Masukkan sesuatu: ")

jumlah_vokal, jumlah_konsonan = hitung_vokal_dan_konsonan(kalimat)

print(f"Jumlah huruf vokal: {jumlah_vokal}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")


# elkom 3
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

# Fungsi pertama untuk mengembalikan nilai kubik dari suatu angka
def nilai_kubik(angka):
    return angka ** 3

# Fungsi kedua untuk mengecek apakah angka habis dibagi 3
def cek_habis_dibagi_tiga(angka):
    if angka % 3 == 0:
        return nilai_kubik(angka)  # Memanggil fungsi nilai_kubik jika habis dibagi 3
    else:
        return False

# Contoh penggunaan:
angka_input = int(input("Masukkan nilai: "))

hasil_cek = cek_habis_dibagi_tiga(angka_input)
if hasil_cek is False:
    print("False")
else:
    print(f"Hasilnya adalah {hasil_cek}")