#latihan1
# cuaca = "mendung"

# if cuaca == "mendung":
#     print ("diam di rumah")
# else:
#     print ("hari ini mendung")

#latihan2
# umur = int (input ("masukkan umur anda:"))
# if umur >= 0:
#     if umur <= 10:
#         print ("umur anda termasuk kategori anak-anak")
#     elif umur <=18:
#         print ("umur anda termasuk kategori remaja")
#     elif umur <=35:
#         print ("umur anda termasuk katgeori dewasa")
#     elif umur <= 65:
#         print ("umur anda termasuk kategori parubaya")
#     else:
#         print ("umur anda termasuk kategori tua")
# else:
#     print ("input umur anda harus bilangan positif")

# LATIHAN3
# NIM = int(input ("masukkan nim:"))
# if NIM >= 1 and NIM <= 50:
#    if NIM >= 1 and NIM <= 25: 
#         print("kelas A'1")
#    else:
#         print("kelas A'2")
# elif NIM >= 51 and NIM <= 100:
#     if NIM == 51 and NIM == 75: 
#         print("kelas B'1")
#     else:
#         print ("kelas B'2")
# elif NIM >= 101 and NIM <= 120:
#     if NIM >= 101 and NIM <= 110:
#         print("kelas C'1")
#     else:
#         print("kelas C'2")
# else: 
#     print("anda bukan mahasiswa informatika 24")

#latihan4

nim = int (input("masukkan nama anda :"))
hasil = "kelas A" if nim >= 1 and nim <= 50 else "kelas b" if nim >= 51 and nim <= 100 else "kelas c" if nim == 101 and nim == 120 else "mahasiswa siluman"
print (hasil)