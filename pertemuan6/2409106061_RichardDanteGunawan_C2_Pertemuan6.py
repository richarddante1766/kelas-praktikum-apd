# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848",
#         "email" : "iniemail@gmail.com"
#     }
# }

# print (Biodata ["KRS"] [0])
# print (Biodata ["Social Media"] ["Discord"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"} })

# print(games ['Valorant']['nama'] [123])

# games = {
#     "Game1" : "Pubg Mobile",
#     "Game2" : "Mobile Legend",
#     "Game3" : {
#         "Nama" : "Coc",
#         "Genre" : "Strategi"
#     }
# }

# print ((games.get("Game3")).get("Genre"))

# print ()

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# for i in Nilai:
#     print(i)
    
# print("")

# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")
    
# print ()

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hours": "comedy", "oblivition": "Science"})
# # #Setelah Ditambah
# print(Film)

# # del Film ["Avenger Endgame"]
# # print (Film)

# # Simpan = Film.pop ("Hours")
# # # Film.clear ()
# # print (Film)
# # Film ["Hours"] = Simpan
# # print (Simpan)
# # print ("Jumlah film", len (Film))

# movies = Film.copy ()
# print (movies)
# print (len (movies))

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
# for key_a, value_a in value.items():
#     print (key_a, " : ", value_a)
# print("")






