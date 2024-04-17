class pet():
    allowed =["cat","dog","fish","bird"]

    def __init__(self,name,species):
        
        if species not in pet.allowed:
            return print(f"You cant have {species} as a pet ***********")
        self.name=name
        self.species=species
    def set_species(self,species):
        if species not in pet.allowed:
            return print(f"You cannot have {species} as a pet !!!!!!!!")
        self.species=species

cat=pet("chaki","cat")
dog=pet("jack","dog")
ele=pet("unni","elephent")


dog.set_species("cat") # will set to new species
print(cat.name, cat.species)
print(dog.name, dog.species)

dog.set_species("tiger") #shold print not allowed
print(dog.species, dog.name)
