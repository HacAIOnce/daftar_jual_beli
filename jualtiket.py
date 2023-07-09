class Pesanan:
	def __init__(self, film, bioskop, jum_tiket):
		self.film = film
		self.bioskop = bioskop
		self.jum_tiket = jum_tiket

	def getFilm(self):
		if self.film == "1":
			return 'Susi Susanti'
		elif self.film == "2":
			return 'Dilan 1990'
		elif self.film == "3":
			return 'Spider-Man'

	def getBioskop(self):
		if self.bioskop == "1":
			return "Cinepolix"
		elif self.bioskop == "2":
			return "XXI"
		elif self.bioskop == "3":
			return "E Plaza"


class Harga(Pesanan):
	def hargaTiketBioskop(self):
		# cek film susi susanti
		if self.film == '1' and self.bioskop == '1':
			return 40000
		elif self.film == '1' and self.bioskop == '2':
			return 25000
		elif self.film == '1' and self.bioskop == '3':
			return 35000
		# cek film dilan
		elif self.film == '2' and self.bioskop == '1':
			return 50000
		elif self.film == '2' and self.bioskop == '2':
			return 35000
		elif self.film == '2' and self.bioskop == '3':
			return 40000
		# cek film spider-man
		elif self.film == '3' and self.bioskop == '1':
			return 35000
		elif self.film == '3' and self.bioskop == '2':
			return 35000
		elif self.film == '3' and self.bioskop == '3':
			return 30000

	def detailHarga(self):	 
		harga = self.jum_tiket * Harga.hargaTiketBioskop(self)
		if self.jum_tiket < 0:
			exit() 
		else: 
			print(f"Sebelum di diskon = Rp.{int(harga)}")
			if harga < 100000:
				return f"diskon 0% = Rp.{int(harga)}"
			elif harga <= 200000:
				return f"diskon 5% = Rp.{int(harga - (0.05 * harga))}"
			elif harga > 200000:
				return f"diskon 10% = Rp.{int(harga - (0.1  * harga))}"

	def kembalian(self, bayar):
		harga = self.jum_tiket * Harga.hargaTiketBioskop(self)
		if harga < 100000:
			return bayar - int(harga)
		elif harga <= 200000:
			return bayar - int(harga - (0.05 * harga))
		elif harga > 200000:
			return bayar - int(harga - (0.1  * harga))