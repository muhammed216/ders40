from tkinter import*
from tkcalendar import DateEntry



master = Tk()

canvas = Canvas(master, height=450, width=750)
canvas.pack()

frame_ust = Frame(master, bg ='#add8e6')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol = Frame(master, bg ='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)


frame_alt_sag = Frame(master, bg ='#add8e6')
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg ='#add8e6', text="Hatırlatma tipi:", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")


hatirlatma_tipi_acilir_menu = OptionMenu(
     frame_ust,
     hatirlatma_tipi_opsiyon,
     "Dogum Günü",
     "Alisveris",
     "Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)


hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background='orange', foreground='black', borderwidth=1, locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)




hatirlatma_tarihi_etiket = Label(frame_ust, bg ='#add8e6', text="Hatırlatma tarihi:", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)



master.mainloop()


