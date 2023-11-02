class Felhasznalo:
    pass

class Jelszo:
    jelszo = "valami"
    def __init__(self):
        #self.jelszo_generalasa()
        pass
    def jelszo_kerese(self):
        pass

    def jelszo_ellemorzese(self):
        pass

    def jelszo_generalasa(self, hossz=10, kisbetu=True, nagybetu=True, szam=True):
        import string
        import random
        jelszo = ""
        karaktersor = ""
        if kisbetu:
            karaktersor = karaktersor + string.ascii_lowercase
        if nagybetu:
            karaktersor = karaktersor + string.ascii_uppercase
        if szam:
            karaktersor = karaktersor + string.digits
        for _ in range(hossz):
            jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor) - 1)]
        self.jelszo = jelszo


