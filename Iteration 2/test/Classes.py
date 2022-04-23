class Bruger:
    def __init__(self, navn, fakultet, id):
        self.navn = navn
        self.fakultet = fakultet
        self.id = id

class Admininstration(Bruger):
    pass

class Underviser(Bruger):
    pass

class Kurser:
    def __init__(self, fakultet, underviser, semester, lokation):
        self.fakultet = fakultet
        self.underviesr = underviser
        self.semester = semester
        self.lokation = lokation

class Skema:
    pass

class Lokaler:
    pass

class Anmodninger:
    pass

