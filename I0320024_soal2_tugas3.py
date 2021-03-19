#Dictionary
dict = {'Nama':['Denny Surya Pratama'],
        'Hobi' : ['Main game','Editing','Jogging'],
        'Sosial media': ['Instagram : @densur_pr','Line : densurpra', 'Whatsapp : 083144630394'],
        'Lagu kesukaan' : ['To the bone', 'Bertaut', 'Sesuatu di jogja'],
        'Makanan favorit' : ['Dimsum', 'Capcay', 'Nila Bakar']}
print(dict)

#Mengubah Hobi dan akun sosial media
dict['Hobi'][1] = ('Makan')
dict['Sosial media'][2] = ('Twitter =Suruu')

#Menghapus dua makanan favorit
del dict['Makanan favorit'][0:2]

#Menambahkan satu Hobi
dict['Hobi'].append('Desain')

#Menampilkan dictionary
print(dict)