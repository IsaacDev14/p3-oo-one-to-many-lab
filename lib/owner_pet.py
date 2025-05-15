PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

class Pet:
    all = []
    def __init__(self, pet_type ):
        self.pet_type = pet_type

class Owner:
    def __init__(self, name):
        self.name = name