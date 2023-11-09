from tkinter import *
from tkinter import messagebox
import gyak_09

def belepes_ablak():
    def ok_gomb_kezelese():
        if fNev.get() == "" or fJelszo.get() == "":
            messagebox.showerror("Hiba", "Nem lehet üres egyik adatmező sem!")
        elif " " in fNev.get() or "@" not in fNev.get() or "." not in fNev.get():
            messagebox.showerror("Hiba", "Nem megfelelő az email formátuma!")
        else:
            print(fNev.get())
            print(fJelszo.get())
            belepes.destroy()

    def reg_gomb_kezelese():
        belepes.destroy()
        reg_ablak()

    belepes = Toplevel()
    belepes.title("Felhasználó beléptetése")

    felh_nev_cimke = Label(belepes, text="Felhaszmnáló neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    fNev = StringVar()
    fNev.set("")
    felh_nev = Entry(belepes, textvariable=fNev, width=30)
    fJelszo = StringVar()
    fJelszo.set("")
    felh_jelszo = Entry(belepes, textvariable=fJelszo, width=20)

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
        if jsz.get() != jsz2.get():
            messagebox.showerror("Hiba", "Nem egyezik a két jelszó")
        elif " " in fhEmail.get() or "@" not in fhEmail.get() or "." not in fhEmail.get():
            messagebox.showerror("Hiba", "Nem megfelelő az email formátuma!")
        else:
            fhsz.email = fhEmail.get()
            fhsz.jelszo = jsz.get()
            print(fhsz.email)
            print(fhsz.jelszo)
            regisztracio.destroy()

    def jelszo_gomb_kezelese():
        fhsz.jelszo_generalasa()
        jsz.set(fhsz.jelszo)
        jsz2.set(fhsz.jelszo)


    fhsz = gyak_09.Felhasznalo("", "")

    regisztracio = Toplevel()
    regisztracio.title("Regisztráció")

    felh_nev_cimke = Label(regisztracio, text="Felhasználó neve (email):")
    felh_jelszo_cimke =Label(regisztracio, text="Jelszó:")
    felh_jelszo2_cimke = Label(regisztracio, text="A jelszó ismét:")

    fhEmail = StringVar()
    fhEmail.set("")
    felh_nev = Entry(regisztracio, textvariable=fhEmail, width=30)
    jsz = StringVar()
    jsz.set("")
    felh_jelszo = Entry(regisztracio, textvariable=jsz, width=20)
    jsz2 = StringVar()
    jsz2.set("")
    felh_jelszo2 = Entry(regisztracio, textvariable=jsz2, width=20)

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese, width=15)
    gomb_jelszo = Button(regisztracio, text="Jelszó generálása!", command=jelszo_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0)
    felh_jelszo_cimke.grid(row=1, column=0)
    felh_jelszo2_cimke.grid(row=2, column=0)
    felh_nev.grid(row=0, column=1)
    felh_jelszo.grid(row=1, column=1)
    felh_jelszo2.grid(row=2, column=1)
    gomb_ok.grid(row=3, column=0, columnspan=3, pady=10)
    gomb_jelszo.grid(row=1, column=2)

    regisztracio.mainloop()

def lista():
    pass

def nevjegy():
    messagebox.showinfo("Névjegy", "Dolgozói nyilvántartás\nKészült: 2023\nKészítette: UNIDUNA")

app = Tk()
app.title("Dolgozók nyilvántartása")
app.minsize(300, 300)

menusor = Menu(app)

hozzaferes = Menu(menusor)
hozzaferes.add_command(label="Belépés", command=belepes_ablak)
hozzaferes.add_command(label="Regisztráció", command=reg_ablak)
hozzaferes.add_command(label="Kilépés", command=app.destroy)
menusor.add_cascade(label="Hozzáférés", menu=hozzaferes)

dolgozok = Menu(menusor)
dolgozok.add_command(label="Lista", command=lista)
dolgozok.add_command(label="Névjegy", command=nevjegy)
menusor.add_cascade(label="Dolgozók", menu=dolgozok)

app.config(menu=menusor)
app.mainloop()
