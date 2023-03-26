class Indian(object):
    @staticmethod
    def printNationality():
        print("Indian")

class Chennai(Indian):
    pass

anIndian = Indian()
subClass = Chennai()
anIndian.printNationality()
Chennai.printNationality()