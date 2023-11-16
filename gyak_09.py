
class Jelszo:
    jelszo = "valami"
    def __init__(self, jelszo):
        self.jelszo = jelszo

    def jelszo_kerese(self):
        pass

    def jelszo_ellemorzese(self, jelszo):
        ok_jelszo = True
        while ok_jelszo:
            van = 0
            if len(jelszo) < 8:
                ok_jelszo = False

            for i in range(len(jelszo)):
                if jelszo[i].isnumeric():
                    van += 1
            if van == 0:
                ok_jelszo = False

            van = 0
            for i in range(len(jelszo)):
                if jelszo[i].isupper():
                    van += 1
            if van == 0:
                ok_jelszo = False

            van = 0
            for i in range(len(jelszo)):
                if jelszo[i].islower():
                    van += 1
            if van == 0:
                ok_jelszo = False

            if not ok_jelszo:
                #jelszo = input("Nem megfelelő a jelszó!!!\nKérek egy jelszót (1,a,A, min 8 karakter): ")
                ok_jelszo = True
            else:
                ok_jelszo = False
        return ok_jelszo

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
