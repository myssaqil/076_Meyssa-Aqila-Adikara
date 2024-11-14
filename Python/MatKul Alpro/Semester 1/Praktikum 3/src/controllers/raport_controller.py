class RaportController:
    def createGet(self, dataCount):
        datas = []

        for studentCollageIndex in range(dataCount):
            print('=====================================================')
            print(f"Data Mahasiswa ke {studentCollageIndex +1}")
            name = input('Nama mahasiswa : ')
            matkuls = []
            for matkulIndex in range(int(input('Jumlah Matakuliah : '))):
                print('===============================')
                print(f"Data matakuliah ke {matkulIndex+1}")
                matkuls.append({
                    'name': input('Nama MataKuliah : '),
                    'score': int(input('Nilai MataKuliah : ')),
                })
            datas.append({
                'name': name,
                'matkuls':matkuls,
            })

        return datas
    
    
    def GetAvg(self, student): 
        scoreTotal = 0
        for matkul in student['matkuls']:
           scoreTotal += matkul['score']
        avg = scoreTotal /len(student['matkuls'])
        
        return avg