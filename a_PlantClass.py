
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant): #name of superclass in () to inherit
    def __init__(self,color, petals):
        Plant.__init__(self,color) #always call the init function of the superclass

        self.__petals = petals #additional attribute applies to flowers

    def get_petals(self):
        return self.__petals
