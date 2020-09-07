class Waiter:

	def __init__(self,name,health,servePower,defenseNumber):
		self.name = name
		self.health = health
		self.servePower = servePower
		self.defenseNumber = defenseNumber

	def siapkan(self, pengunjung):
		print(self.name + ' menyiapkan makanan untuk ' + pengunjung.name )
		pengunjung.menunggu(self, self.servePower)

	def menunggu(self, pengunjung, servePower_pengunjung):
		print(self.name + ' menunggu ' + pengunjung.name)
		serve_diterima = servePower_pengunjung/self.defenseNumber
		print("makanan datang")
		print('makanan didapur berkurang : ' + str(serve_diterima))
		self.health -= serve_diterima
		print('makanan di dapur tersisa ' + str(self.health))

sniper = Waiter('sniper',100,10,5)
rikimaru = Waiter('rikimaru',100,20,10)

sniper.siapkan(rikimaru)
print("\n")
sniper.siapkan(rikimaru)
print("\n")
sniper.siapkan(rikimaru)
print("\n")
sniper.siapkan(rikimaru)
print("\n")
