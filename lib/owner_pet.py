class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if self.pet_type not in (Pet.PET_TYPES):
           raise Exception(f'{self.pet_type} is not in {Pet.PET_TYPES}')

class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
         
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
           raise Exception(f'{pet} is not in {Pet} type')
        pet.owner = self
            
            
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet:pet.name)
            
        
        
    
    
        