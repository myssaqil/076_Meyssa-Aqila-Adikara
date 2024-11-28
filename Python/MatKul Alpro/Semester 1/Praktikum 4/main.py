

selectPrograms = input('Pilih Program (tuliskan idnya): ')

if selectPrograms=='1':
    from src.controllers import rectangle_controller

    widthRectangle = int(input('Masukkan Panjang Persegi Panjang : '))
    heightRectangle = int(input('Masukkan Lebar Persegi Panjang : '))
    rectangle = rectangle_controller.RectangleController(height=heightRectangle, width=widthRectangle)

    print("================= Result =================")
    print(f"Luas Persegi Panjang = {rectangle.calculateLuas()}")
elif selectPrograms == '2':
    itemStock = 100

    def transaction(quantity):
        res = True
        global itemStock
        if(itemStock < quantity):
            res = False
        else:
            itemStock = itemStock - quantity
        return res

    isNext = True
    while isNext:
        print('================= Welcome To Transaction =================')
        quantity = int(input("Masukkan jumlah Barang : "))
        res = transaction(quantity)
        if(res == False):
            print(f"Jumlah Barang Tidak Cukup, sisa stok : {itemStock}")
        print(f"sisa stok : {itemStock}")
        if(input("apakah ingin lanjut (y/n): ") == 'n'):
            isNext = False
# elif selectPrograms == '3':
   


#      print('================= Aqil Store =================')

# elif selectPrograms == '4':

else: 
    print('Invalid Program')
