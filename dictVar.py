#Cara Memanggil Variabel denga menggunakan Dictionary(Repository Program Python)

dictVar = {'PI': 3.14,
           25: "The Square of 5",
           "Weihan": "My Name"
           }
#Dengan memanggil Variabel PI pada Percobaan diatas Dapat Menggunakan 3 cara ini yaitu:

key = "PI"
print("The value corresponding to the key {0} is: {1}".format(key, dictVar[key]))        

print("The value corresponding to the key", "'PI'", "is:", dictVar['PI'])

print("The value corresponding to the key", "'PI'", "is:", dictVar[key])
