
print("\t=== Tiket Film ===")
	
# daftar film 
print("=== DAFTAR FILM ===")
print("1. Susi Susanti")
print("2. Dilan 1990")
print("3. Spider-Man")
print("4. exit")
print("====================")
film = input("Ingin film nomor berapa: ")
if film == '4':
	print('\n"Terimakasih Sudah Berkunjung"')
	exit()	

# lokasi bioskop
print("\n=== LOKASI BIOSKOP ===")
print("1. Cinepolix")
print("2. XXI")
print("3. E Plaza")
print("4. exit")
bioskop = input("Ingin menonton dimana: ")
if bioskop == '4':
	print('\n"Terimakasih Sudah Berkunjung"')
	exit()

# jumlah tiket
print("\n====================")
jum_tiket = int(input("Beli berapa tiket: "))
print("====================")
