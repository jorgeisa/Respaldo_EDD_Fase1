from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def centrar_ventana(app, ancho, alto):
    app.config(width=ancho, height=alto)  # linen - light cyan - ghost white WhiteSmoke
    # Centrar ventana
    x_ventana = app.winfo_screenwidth() // 2 - ancho // 2
    y_ventana = app.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x_ventana) + "+" + str(y_ventana)
    app.geometry(posicion)
    app.configure(bg='#F0FFFF')


def configuracion_defecto(app):
    app.title("    TYTUS")
    app.resizable(0, 0)
    app.iconbitmap('./images/blockchain_.ico')


def ventana_principal():
    # Raíz de la aplicación
    app = Tk()
    color = "#F0FFFF"
    configuracion_defecto(app)
    centrar_ventana(app, 900, 700)

    bg_image = PhotoImage(file="./images/fondo.png")
    x = Label(app, image=bg_image, bg=color)
    x.place(x=0, y=0)
    x.pack()

    # Botones
    img_db = PhotoImage(file="./images/base-de-datos.png")
    db = Button(text="Bases de datos",  bg="#FFFFFF", image=img_db, compound="top", font=("Georgia", 16), command=ventana_db)
    db.place(x=500, y=200)

    img_subir = PhotoImage(file="./images/subir.png")
    db = Button(text="Cargar", bg="#FFFFFF", image=img_subir, compound="top", font=("Georgia", 16), command=abrir_archivo)
    db.place(x=600, y=400)

    # Selección del combobox
    def selection_changed( event):
        combo_bases_db(combo.get())

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(font=fuente)
    combo.place(x=680, y=200)

    combo["values"] = ["createDatabase", "showDatabases", "alterDatabase", "dropDatabase"]
    combo.bind("<<ComboboxSelected>>", selection_changed)
    etiqueta = Label(text="Funciones", bg=color, font=("Georgia", 16)).place(x=720, y=225)

    # ---------------------------------------------------- FUNCIONES ---------------------------------------------------
    # SELECCIÓN COMBOBOX
    def combo_bases_db(seleccion):
        if seleccion == 'createDatabase':
            print('create_database')
        elif seleccion == 'showDatabases':
            print('showDatabases')
        elif seleccion == 'alterDatabase':
            print('alterDatabase')
        elif seleccion == 'dropDatabase':
            print('dropDatabase')

    app.mainloop()


def ventana_db():
    app2 = Toplevel()
    configuracion_defecto(app2)
    centrar_ventana(app2, 500, 700)

    # Selección del combobox
    def selection_changed(event):
        ventana_lista_tablas(app2, combo.get())

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app2, font=fuente)
    combo.place(x=150, y=200)

    etiqueta = Label(app2, text="Seleccionar DB", bg="#F0FFFF", font=("Georgia", 13)).place(x=180, y=170)
    combo["values"] = ["lista de DB"]
    combo.bind("<<ComboboxSelected>>", selection_changed)


def ventana_lista_tablas(ventana, db):
    ventana.withdraw()  # Cerrar ventana anterior
    app = Toplevel()
    configuracion_defecto(app)
    centrar_ventana(app, 500, 700)

    # Selección del combobox
    def selection_changed(event):
        print(combo.get())

    # Combobox
    fuente = ("Georgia", 10)
    combo = ttk.Combobox(app, font=fuente)
    combo.place(x=150, y=200)

    etiqueta = Label(app, text="Tablas de DB: "+db, bg="#F0FFFF", font=("Georgia", 13)).place(x=150, y=170)
    combo["values"] = ["lista de tablas"]
    combo.bind("<<ComboboxSelected>>", selection_changed)

    # ---------------------------------------------------- FUNCIONES ---------------------------------------------------
    def cargar_tablas(combo_box):
        # Cargar datos
        array = []
        for i in range(0, 10):
            array.append(i)
        combo_box['values'] = array

    cargar_tablas(combo)


# CARGAR ARCHIVO
def abrir_archivo():
    nombre_archivo = filedialog.askopenfilename(title='Seleccione archivo')
    if nombre_archivo != '':
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        archivo.close()
        print(contenido)


ventana_principal()
