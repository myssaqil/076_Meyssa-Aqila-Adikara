from src.controllers import range_number_controller

numStart = int(input('Masukkan Nilai Awal : '))
numEnd = int(input('Masukkan Nilai Akhir : '))
rangeNumCtrl = range_number_controller.RangeNumberController(numStart, numEnd)


for i, num in enumerate(rangeNumCtrl.showGanjil()) :
    print(f"Angka ganjil ke {i} : {num}")



print("====================== Data Mahasiswa ======================")

from src.controllers import raport_controller

# Nilai
numCtrl = raport_controller.RaportController()

mhsCount = int(input('Jumlah mahasiswa : '))
collegeStudents = numCtrl.createGet(mhsCount)

print("====================== Final Data ======================")
for collegeStdnt in collegeStudents:
    print('=====================================================')
    print(f"Nama : {collegeStdnt['name']}")
    print(f"Jumlah Mata Kuliah : {len(collegeStdnt['matkuls'])}")
    for matkul in collegeStdnt['matkuls']:
        print('===============================')
        print(f"Nama MataKuliah : {matkul['name']}")
        print(f"Nilai MataKuliah : {matkul['score']}")
    print(f"Rata - Rata : {numCtrl.GetAvg(collegeStdnt)}")