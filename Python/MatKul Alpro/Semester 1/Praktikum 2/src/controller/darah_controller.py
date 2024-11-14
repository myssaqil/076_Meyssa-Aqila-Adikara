class DarahController:
    usia = 0
    tekananDarah = 0

    def __init__(self, usia, tekananDarah):
        self.usia = usia
        self.tekananDarah = tekananDarah
    
    def checkTekananDarah(self): 
        message = None

        if(self.usia >= 60 and self.tekananDarah > 140):
            message = "Tinggi"
        elif(self.usia >= 60 and self.tekananDarah <= 140):
            message = "Normal"
        elif(self.usia < 60 and self.tekananDarah > 130):
            message = "Tinggi"
        elif(self.usia < 60 and self.tekananDarah <= 130):
            message = "Normal"

        return message