from daftarfilm import film, bioskop, jum_tiket
from jualtiket import Pesanan, Harga


def main():
	pesanan = Harga(film, bioskop, jum_tiket)
	print("\n=== DETAIL PESANAN ===")
	print(pesanan.getFilm())
	print(pesanan.getBioskop())
	print(pesanan.detailHarga())

	# pembayaran dan kembalian
	bayar = int(input("Uang Pembayaran: Rp."))
	print("====================\n")

	print("Nama Film:", pesanan.getFilm())
	print("Nama Bioskop:", pesanan.getBioskop())
	print(pesanan.detailHarga())
	print(f"Uang Pembayaran: Rp.{bayar}")
	print(f"Kembalian: Rp.{pesanan.kembalian(bayar)}")




if __name__ == '__main__':
	main()