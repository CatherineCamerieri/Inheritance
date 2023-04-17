import a_PlantClass as pc

primrose = pc.Plant("Green") #instance of the superclass

sunflower = pc.Flower("Yellow",12) #istance of the subclass

print(primrose.get_color())

print(sunflower.get_color()) #can call a method from the superclass 
print(sunflower.get_petals())


print(primrose.get_petals()) #instance of a plant superclass, so cannot call a method from a subclass
