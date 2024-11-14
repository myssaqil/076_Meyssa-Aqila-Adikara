class RangeNumberController:
    numberStart = 0
    numberEnd = 0

    def __init__(self, numberStart, numberEnd ):
        self.numberStart = numberStart
        self.numberEnd= numberEnd

    def showGanjil(self):
        datas = []
        num = self.numberStart

        while num <= self.numberEnd:
            if num %2 !=0:
                datas.append(num)
            num += 1 
        
        return datas
    