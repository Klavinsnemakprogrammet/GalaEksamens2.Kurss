#atsauce: skolo.lv Programmēšana (Python) Inta Znotiņa
# atsauce: liela daļa no jautājumiem ņemti no https://www.w3schools.com/python/python_functions.asp
import tkinter as tk
import random

#---------------------------------- viktorīnas dati --------------------------------#
jautajumi = [
    "KĀ PAREIZI IZVEIDOT FUNKCIJU PYTHON VALODĀ?",
    "KĀ VAR IZSAUKT ŠO FUNKCIJU?\n \n def function():\n print(""'Hello World!'"")",
    "KO IZVADĪS PROGRAMMA? \n\n def reizreikins(x): \n return x * 2\n print(reizreikins(5))",
    "KO IZDOS ŠĪ PROGRAMMA? \n\n def funkcija(x):""\n print(x)""\n my_function(x = 1)",
    "KAS IR JĀIEVADA LAI FUNKCIJAS REZULTĀTS BŪTU 6?""\n\n def reizrekins(a, b):\nreturn a * b",
    "KAS TIKS IZDOTS PĒC ŠI KODA IZPILDES? \n\n def majas(valsts = ""'Norvēģja'""):\n  print(""Manas mājas ir "" + valsts)\n majas(""'Latvija'"")",
    "KĀ VAR IZSAUKT ŠO FUNKVIJU \n \n def HelloWorld():\n print(""'Hello World!'"")",
    "KO DARA COMMANDA 'PASS' ŠAJĀ KODĀ? \n\n def mana_funkcija():\n pass",
    "KO IZVADĪS ŠIS KODS? def funkcija(ediens):\n  for x in ediens:\n augli = ['ābols', 'banāns', 'apelsīns']\n funkcija(augli)",
    "KO IZVADĪS ŠIS KODS? \n\n def matematika(a, b, /, *, c, d):\n print(a + b + c + d)\n matematika(5, 6, c = 7, d = 8)",
   
]
atbildes1 = [
    "def mana_funkcija():",
    "print(funkcija())",
    "10",
    "x",
    "reizrekins(2, 2)",
    "Error",
    "call HelloWorld()",
    "padod vērtības nākamai funkcijai",
    "apelsīns",
    "8",
   
]
atbildes2 = [
    "static void mana_funkcija() {",
    "print(""Hello World!"")",
    "5",
    "1",
    "reizrekins(3, 2)",
    "Ķengarags",
    "Hello World()",
    "veic loop",
    "ābols banāns apelsīns",
    "26",
    
]
atbildes3 = [
    "void mana_funkcija() {",
    "nevar",
    "Error",
    "1x",
    "reizreikins(3 2)",
    "Norvēģija",
    "HelloWorld()",
    "Neko",
    "apelsīns banāns ābols",
    "20",
   
]
atbildes4 = [
    "define mana_funkcija():",
    "funkcija()",
    "2",
    "Error",
    "reizreikins(x * y = 6)",
    "Latvija",
    "HelloWorld[]",
    "Error",
    "ābols",
    "15",
   
]
atbildes = [
    "def mana_funkcija():",
    "funkcija()",
    "10",
    "1",
    "reizrekins(3, 2)",
    "Latvija",
    "HelloWorld()",
    "Neko",
    "ābols banāns apelsīns",
    "26",
    
]
seciba = [0,1,2,3,4,5,6,7,8,9,10]
piemers = 0
punkti = 0

#------------------------------------ notikumi ----------------------------------#
# funkcija, lai aizvērtu visus logus
def close_all_windows():
    root.destroy()

# funkcija, lai parādītu jautājumu skatu
def funkSAKT():
    sakuma_skats.pack_forget()  # Aizver sākuma skatu
    jautajumu_skats.pack(fill='both', expand=True)  # Atver jautājumu skatu

# funkcija 1. atbildes pogai
def funkATBILDE1():
    global punkti
    global piemers
    if atbildes1[seciba[piemers]] == atbildes[seciba[piemers]]:
        punkti += 2
    elif punkti > 0:
        punkti -= 1
    funkJAUTAJUMS()

# funkcija 2. atbildes pogai    
def funkATBILDE2():
    global punkti
    global piemers
    if atbildes2[seciba[piemers]] == atbildes[seciba[piemers]]:
        punkti += 2
    elif punkti > 0:
        punkti -= 1
    funkJAUTAJUMS()

# funkcija 3. atbildes pogai
def funkATBILDE3():
    global punkti
    global piemers
    if atbildes3[seciba[piemers]] == atbildes[seciba[piemers]]:
        punkti += 2
    elif punkti > 0:
        punkti -= 1
    funkJAUTAJUMS() 
    
def funkATBILDE4():
    global punkti
    global piemers
    if atbildes4[seciba[piemers]] == atbildes[seciba[piemers]]:
        punkti += 2
    elif punkti > 0:
        punkti -= 1
    funkJAUTAJUMS()     

# funkcija nākošā jautājuma ielādei
def funkJAUTAJUMS():
    global punkti
    global piemers
    if punkti == 1:
        rezultats.config(text=f"{punkti} punkts")
    else:
        rezultats.config(text=f"{punkti} punkti")
    piemers += 1
    if piemers < 10:
        jautNr.config(text=f'{piemers}. no 10 jautājumiem')
        jautajums.config(text=jautajumi[seciba[piemers]])
        atbilde1.config(text=atbildes1[seciba[piemers]])
        atbilde2.config(text=atbildes2[seciba[piemers]])
        atbilde3.config(text=atbildes3[seciba[piemers]])
        atbilde4.config(text=atbildes4[seciba[piemers]])
    else:
        jautajumu_skats.pack_forget()
        rezultata_skats.pack(fill='both', expand=True)
        if punkti==20:
            txt = f"Cerams čatiņš tev nepalīdzēja!\nApsveicu tu atbildēji pareizi uz visiem jautājumiem! ({punkti} punkti)"
        elif punkti>15:
            txt = f"Lieliski! Gandrīz perfektas atbildes!\n({punkti} punkti)"
        elif punkti>10:
            txt = f"Malacis vairāk par 10 punktiem, bet ir vel ko mācīties!\n({punkti} punkti)" 
        elif punkti>5:
            txt = f"Ir vel ko mācīties \n({punkti} punkti)"       
        elif punkti>1:
            txt = f"Nu līdz 2niekam daudz nevajag!\nDiemžēl liela daļa tavu atbilžu bija nepareizas. ({punkti} punkti)"
        elif punkti>0:
            txt = f"Nu līdz 2niekam daudz nevajag!\nKā var pat 1 punktu neiegūt? ({punkti} punkts)"
        else:
            txt = f"Nu līdz 2niekam daudz nevajag!\nDiemžēl tavas atbildes bija nepareizas. ({punkti} punkti)"
        rezult.config(pady = 20, text=txt, font=('Verdana', 14), fg="#FFFFFF", bg="#3F3F3F")

def restart():
    global piemers, punkti
    piemers = 0
    punkti = 0
    rezult.config(text="rezultats", font=('Verdana', 14), fg="white", bg="#3F3F3F")
    rezultata_skats.pack_forget()
    jautNr.config(text=f'{piemers+1}. no 10 jautājumiem')
    rezultats.config(text='0 punkti')
    jautajums.config(text=jautajumi[seciba[piemers]])
    atbilde1.config(text=atbildes1[seciba[piemers]])
    atbilde2.config(text=atbildes2[seciba[piemers]])
    atbilde3.config(text=atbildes3[seciba[piemers]])
    atbilde4.config(text=atbildes4[seciba[piemers]])
    jautajumu_skats.pack(fill='both', expand=True)

#--------------------------------- programmas logs ------------------------------#
root = tk.Tk()
root.title("Python Funkciju Tests")
root.geometry("1000x1000")  
root.resizable(True, True) #var mainit logu izmērus
root.configure(bg="#3F3F3F")

#--------------------------------- sākuma skats ---------------------------------#
sakuma_skats = tk.Frame(root, bg="#3F3F3F")
# sakuma_skats.pack(fill='both', expand=True)
# izveido uzrakstu
uzraksts_sakums = tk.Label(sakuma_skats, text="Python Funkciju Tests", font=('Verdana', 24, 'bold'), fg="#005994", bg="#3F3F3F")
uzraksts_sakums.pack(pady=20)
# ielādē attēlu
image = tk.PhotoImage(file="pythonlogo.png")  
# izveido Label, lai parādītu attēlu
attels_sakums = tk.Label(sakuma_skats, image=image, bg="#3F3F3F")
attels_sakums.pack(pady=10)
# izveido pogu
poga = tk.Button(sakuma_skats, text="Sākt", command=funkSAKT, width=20, height=3, bg = 'lightgrey', fg = '#005994', font = ('Verdana', 20, 'bold'))

poga.pack(pady=150)

#------------------------------- jautājumu skats -------------------------------#
jautajumu_skats = tk.Frame(root, bg="#3F3F3F")
# jautajumu_skats.pack(fill='both', expand=True)
# izveido 2 vienlīdz palatas kolonnas elementu izkārtojumam
jautajumu_skats.grid_columnconfigure(0, weight=1)
jautajumu_skats.grid_columnconfigure(1, weight=1)
# izvieto 2 elementus (jautājuma numurs un punkti) vienu otram blakus, katru savā kolonnā
jautNr = tk.Label(jautajumu_skats,text=f'{piemers+1}. no 10 jautājumiem',font=('Verdana', 12, 'bold'),bg="#3F3F3F",fg="white"  )
jautNr.grid(row=0, column=0, padx=25, pady=25, sticky="w")

rezultats = tk.Label(jautajumu_skats,text='0 punkti',font=('Verdana', 12, 'bold'),bg="#3F3F3F",fg="white"  )
rezultats.grid(row=0, column=1, padx=25, pady=25, sticky="e")
jautajums = tk.Label(jautajumu_skats, text = jautajumi[seciba[piemers]], font = ('Verdana', 15, 'bold'), fg = "#005994", bg="#3F3F3F")
jautajums.grid(row=1, column=0, columnspan=2, pady=70)
atbilde1 = tk.Button(jautajumu_skats, text = atbildes1[seciba[piemers]], command=funkATBILDE1, width=70, height = 3, bg = 'lightgrey', font = ('Verdana', 12, 'bold'))
atbilde1.grid(row=2, column=0, columnspan=2, pady=10)
atbilde2 = tk.Button(jautajumu_skats, text = atbildes2[seciba[piemers]], command=funkATBILDE2, width=70, height = 3, bg = 'lightgrey', font = ('Verdana', 12, 'bold'))
atbilde2.grid(row=3, column=0, columnspan=2, pady=10)
atbilde3 = tk.Button(jautajumu_skats, text = atbildes3[seciba[piemers]], command=funkATBILDE3, width=70, height = 3, bg = 'lightgrey', font = ('Verdana', 12, 'bold'))
atbilde3.grid(row=4, column=0, columnspan=2, pady=10)
atbilde4 = tk.Button(jautajumu_skats, text = atbildes4[seciba[piemers]], command=funkATBILDE4, width=70, height = 3, bg = 'lightgrey', font = ('Verdana', 12, 'bold'))
atbilde4.grid(row=5, column=0, columnspan=2, pady=10)

#--------------------------------- rezultāta skats ---------------------------------#
rezultata_skats = tk.Frame(root, bg="#3F3F3F")
# rezultata_skats.pack(fill='both', expand=True)
# izveido uzrakstu
uzraksts_rezultats = tk.Label(rezultata_skats, text="Python Funkciju Tests", font=('Verdana', 24, 'bold'), fg='#005994', bg="#3F3F3F")
uzraksts_rezultats.pack(pady=20)
# ielādē attēlu
attels_rezultats = tk.Label(rezultata_skats, image=image, bg="#3F3F3F")
attels_rezultats.pack(pady=10)
# izveido rezultāta logu
rezult = tk.Label(rezultata_skats, text="rezultats", font=('Verdana', 14), bg="#3F3F3F")
rezult.pack(pady=20)

restart_btn = tk.Button(rezultata_skats,text="Sākt no jauna", command=restart,width=20,height=2,bg='lightgrey',fg='#005994',font=('Verdana', 14, 'bold'))
restart_btn.pack(pady=10)


# Sākuma skata rādīšana
sakuma_skats.pack(fill='both', expand=True)

root.mainloop()