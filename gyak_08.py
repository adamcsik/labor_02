from tkinter import *

def belepes_ablak():
    def ok_gomb_kezelese():
        belepes.destroy()

    def reg_gomb_kezelese():
        belepes.destroy()

    belepes = Tk()
    belepes.title("Felhasználó beléptetése")

    felh_nev_cimke = Label(belepes, text="Felhaszmnáló neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    felh_nev = Entry(belepes, width=30)
    felh_jelszo = Entry(belepes, width=20)

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_kezelese, width=10)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0, padx=10, pady=20, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, sticky=E, padx=10)
    felh_nev.grid(row=0, column=1, padx=10, sticky=W)
    felh_jelszo.grid(row=1, column=1, sticky=W, padx=10)
    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_reg.grid(row=2, column=1)

    belepes.mainloop()

def reg_ablak():
    def ok_gomb_kezelese():
        regisztracio.destroy()

    def jelszo_gomb_kezelese():
        regisztracio.destroy()

    regisztracio = Tk()
    regisztracio.title("Regisztráció")

    felh_nev_cimke = Label(regisztracio, text="Felhasználó neve (email):")
    felh_jelszo_cimke =Label(regisztracio, text="Jelszó:")
    felh_jelszo2_cimke = Label(regisztracio, text="A jelszó ismét:")

    felh_nev = Entry(regisztracio, width=30)
    felh_jelszo = Entry(regisztracio, width=20)
    felh_jelszo2 = Entry(regisztracio, width=20)

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese)
    gomb_jelszo = Button(regisztracio, text="Jelszó generálása!", command=jelszo_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0)
    felh_jelszo_cimke.grid(row=1, column=0)
    felh_jelszo2_cimke.grid(row=2, column=0)
    felh_nev.grid(row=0, column=1)
    felh_jelszo.grid(row=1, column=1)
    felh_jelszo2.grid(row=2, column=1)
    gomb_ok.grid(row=3, column=0)
    gomb_jelszo.grid(row=1, column=2)

    regisztracio.mainloop()

#belepes_ablak()
reg_ablak()