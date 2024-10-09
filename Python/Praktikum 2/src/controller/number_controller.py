class NumberController:
    num = 0


    def __init__(self, num):
        self.num = num
        print(f'Bilangan : {num}')

    def checkGanjilGenap(self):
        isGenap = None
        if(self.num % 2 == 0):
            isGenap = True
        else:
            isGenap = False

        return isGenap