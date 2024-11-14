class NilaiController:
    nilai = 0


    def __init__(self, nilai):
        self.nilai = nilai
        print(f'Nilai : {self.nilai}')

    def validateNilai(self):
        status = True
        message = ""
       
        if(self.nilai >= 0 and self.nilai <= 100):
            status = True
            message = 'Valid'
        else:
            status = False
            message = 'Invalid nilai'

        return {
            'status': status,
            'message': message
        }

    def checkNilai(self):
        nilai = self.nilai
        message = None
        if(nilai >=90 and nilai <=100):
            message = "Sangat Baik"
        elif(nilai >= 80 and nilai <=89):
            message = "Baik"
        elif(nilai >= 70 and nilai <=79):
            message = "Cukup"
        elif(nilai >= 60 and nilai <=69):
            message = "kurang"
        else:
            message = "Sangat kurang"

        return message