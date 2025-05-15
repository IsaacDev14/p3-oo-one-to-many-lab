PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

class Pet:
    all = []
    def __init__(self, name, pet_type, owner = None ):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name