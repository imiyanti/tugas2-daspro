print("==APLIKASI PERHITUNGAN GAJI KARYAWAN===")

hari_kerja          = int(input("Masukkan jumlah hari kerja karyawan     :"))
hari_kerja_perbulan = 30    # Jumlah hari kerja per bulan
gaji_pokok          = 10000000
tarif_lebur_per_jam = 50000  # Misalnya tarif lebur per jam adalah Rp.50.000
jam_lembur          = int(input("Masukkan jumlah jam lembur yang dilakukan :"))  # Jumlah jam lembur yang dilakukan karyawan

# Menghitung total gaji pokok
total_gaji_pokok = (hari_kerja_perbulan) * gaji_pokok

# Menghitung total gaji lembur
total_gaji_lembur = jam_lembur * tarif_lebur_per_jam

# Menghitung total gaji keseluruhan
total_gaji = total_gaji_pokok + total_gaji_lembur

# Mengonversi total gaji menjadi string dengan tanda pemisah
total_gaji_string = "{:,.2f}".format(total_gaji)

print("Total Gaji Keseluruhan: Rp", total_gaji_string)


#menampilkan total gaji dengan tanda pemisah
print("Total Gaji Keseluruhan  : Rp.", total_gaji_string)
