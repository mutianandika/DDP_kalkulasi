print("SLIP GAJI PT.XYZ")
print("===========================================")
nama  = "Aldy Maldini"
agama = "Islam"
gajih_pokok = 4000000
tunjangan_jabatan = 20/100*gajih_pokok
jumlah_anak = 2

if(jumlah_anak <= 2):
    tunjangan_keluarga = 10/100*gajih_pokok
elif(jumlah_anak < 2):
    tunjangan_keluarga = 20/100*gajih_pokok
else:
    tunjangan_keluarga = 0
gaji_kotor = gajih_pokok + tunjangan_jabatan + tunjangan_keluarga

zakat_profesi = (0,0.025)[agama == "islam" and gaji_kotor >= 6000000]*gaji_kotor
gaji_bersih = gaji_kotor - zakat_profesi

print("Nama                        :",nama)
print("Agama                       :",agama)
print("Jumlah_anak                 :",jumlah_anak)
print("Gaji_pokok Rp.              :",gajih_pokok)
print("Tunjangan_jabatan Rp.       :",tunjangan_jabatan)
print("Tunjangan_keluarga Rp.      :",tunjangan_keluarga)
print("Gaji_kotor Rp               :",gaji_kotor)
print("Zakat_profesi Rp.           :",zakat_profesi)
print("Gaji_bersih Rp.             :",gaji_bersih)





print("SPIL GAJI PT.XYZ")
print("==============================================")
nama  = "Marcell"
agama = "Kristen"
gajih_pokok = 6000000
tunjangan_jabatan = 20/100*gajih_pokok
jumlah_anak = 5

if(jumlah_anak <= 2):
    tunjangan_keluarga = 10/100*gajih_pokok
elif(jumlah_anak > 2):
    tunjangan_keluarga = 20/100*gajih_pokok
else:
    tunjangan_keluarga = 0
gaji_kotor = gajih_pokok + tunjangan_jabatan + tunjangan_keluarga

zakat_profesi = (0,0.025)[agama == "Islam" and gaji_kotor >= 6000000]*gaji_kotor
gaji_bersih = gaji_kotor - zakat_profesi

print("Nama                        :",nama)
print("Agama                       :",agama)
print("Jumlah_anak                 :",jumlah_anak)
print("Gaji_pokok Rp.              :",gajih_pokok)
print("Tunjangan_jabatan Rp.       :",tunjangan_jabatan)
print("Tunjangan_keluarga Rp.      :",tunjangan_keluarga)
print("Gaji_kotor Rp               :",gaji_kotor)
print("Zakat_profesi Rp.           :",zakat_profesi)
print("Gaji_bersih Rp.             :",gaji_bersih)
