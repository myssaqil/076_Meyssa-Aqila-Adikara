from src.controller import number_controller
from src.controller import darah_controller
from src.controller import nilai_controller

print("================== Number ==================")
num = int(input('Masukkan Bilangan : '))
numCtrl = number_controller.NumberController(num)

if(numCtrl.checkGanjilGenap()):
    print('Termasuk Genap')
else:
    print('Termasuk Ganjil')


print("================== Nilai ==================")
nilai = int(input('Masukkan Nilai : '))
nilaiCtrl = nilai_controller.NilaiController(nilai)

validateNilai = nilaiCtrl.validateNilai()
if(not validateNilai['status']):
    print(validateNilai['message'])
else:
    print(nilaiCtrl.checkNilai())


print("================== Darah ==================")
usia = int(input('Usia : '))
tekananDarah = int(input('Tekanan Darah : '))
darahCtrl = darah_controller.DarahController(usia, tekananDarah)

print(darahCtrl.checkTekananDarah())
