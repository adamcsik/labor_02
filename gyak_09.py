
class Jelszo:
    jelszo = "valami"
    def __init__(self, jelszo):
        self.jelszo = jelszo

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

class Felhasznalo(Jelszo):
    email = "alhf"
    def __init__(self, email, jelszo):
        super().__init__(jelszo)
        self.email = email


if __name__ == "__main__":
    fhsz = Felhasznalo("asdf@aew.hu", "valami jelszó")
    print(fhsz.email)
    print(fhsz.jelszo)
    fhsz.jelszo_generalasa()
    print(fhsz.jelszo)
