# Penulisan list nama teman
list_teman = ['Fajri', 'Anisa', 'Erika', 'Karsa', 'Sekar', 'Vizal', 'Bonang', 'Moris', 'Yola', 'Dhea']

# Menampilkan isi list nomor 4,6,7
print("Nama Teman pada index nomor 4,6,7 : ",list_teman[4],list_teman[6],list_teman[7])

Merubah nama teman pada index 3,5,9
list_teman[3] = 'Narista'
list_teman[5] = 'Attar'
list_teman[9] = 'Rafly'

#Menambahkan nama teman
list_teman.append('Gea')
list_teman.append('Rara')

#Menampilkan semua nama teman beserta perulangan
print('Perulangan list nama teman : ', (list_teman*3))

#Menampilkan panjang list
print('Panjang list nama teman : ', len(list_teman))