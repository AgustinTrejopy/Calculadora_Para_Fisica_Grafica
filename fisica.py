from tkinter import *

root = Tk()
root.title("Convertidor Fisica")
root.geometry("447x100")
root.config(bg="light green")

texto_vacio = Label(root, 
                    text="",
                    bg="light green").grid(row=1, column=0)

texto_2 = Label(root, 
                text="A que unidad de medicion quiere pasarlo?",
                bg="purple",
                fg="white").grid(row=2, column=1)


def envia_boton_1():
    ventana_UDL = Toplevel()
    ventana_UDL.title("Unidad de longitud")
    ventana_UDL.geometry("460x400")
    ventana_UDL.config(background="gray")

    titulo_ventana = Label(ventana_UDL, 
                           text="UNIDAD DE LONGITUD",
                           bg="purple",
                           fg="white",
                           borderwidth=3,
                           border=3,
                           font=("Courier", 12)).grid(row=0, column=1)

    relleno_1 = Label(ventana_UDL, 
                      text="",
                      bg="gray").grid(row=0, column=0)
    relleno_2 = Label(ventana_UDL, 
                      text="",
                      bg="gray").grid(row=0, column=2)
    
    subtitulo_1 = Label(ventana_UDL,
                      text="Ingrese datos numericos: ",
                      bg="purple",
                      fg="white",
                      borderwidth=3,
                      border=3,
                      underline=True).grid(row=1, column=0)
    entrada_UDL = Entry(ventana_UDL)
    entrada_UDL.grid(row=1, column=1)
    
    subtitulo_2 = Label(ventana_UDL, 
                        text="Que Unidad es su dato numerico?",
                        bg="purple",
                        fg="white",
                        borderwidth=3,
                        border=3,
                        underline=True).grid(row=2, column=1)

    def resultado_km():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_km = float(obtencion_R)
            valor_hm = valor_km * 10
            valor_decam = valor_km * 10 * 10
            valor_m = valor_km * 10 * 10 * 10
            valor_decim = valor_km * 10 * 10 * 10 * 10
            valor_cm = valor_km * 10 * 10 * 10 * 10 * 10
            valor_mm = valor_km * 10 * 10 * 10 * 10 * 10 * 10

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!")

    def resultado_hm():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_hm = float(obtencion_R)
            valor_km = valor_hm / 10
            valor_decam = valor_hm * 10 
            valor_m = valor_hm * 10 * 10 
            valor_decim = valor_hm * 10 * 10 * 10 
            valor_cm = valor_hm * 10 * 10 * 10 * 10 
            valor_mm = valor_hm * 10 * 10 * 10 * 10 * 10 

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!")
        
    def resultado_decam():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_decam = float(obtencion_R)
            valor_km = valor_decam / 10 / 10
            valor_hm = valor_decam / 10 
            valor_m = valor_decam * 10  
            valor_decim = valor_decam * 10 * 10 
            valor_cm = valor_decam * 10 * 10 * 10 
            valor_mm = valor_decam * 10 * 10 * 10 * 10  

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!")
    
    def resultado_m():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_m = float(obtencion_R)
            valor_km = valor_m / 10 / 10 / 10   
            valor_hm = valor_m / 10 / 10
            valor_decam = valor_m / 10  
            valor_decim = valor_m * 10 
            valor_cm = valor_m * 10 * 10 
            valor_mm = valor_m * 10 * 10 * 10 

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!")
        
    def resultado_decim():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_decim = float(obtencion_R)
            valor_km = valor_decim / 10 / 10 / 10 / 10 
            valor_hm = valor_decim / 10 / 10 / 10 
            valor_decam = valor_decim / 10 / 10 
            valor_m = valor_decim / 10 
            valor_cm = valor_decim * 10 
            valor_mm = valor_decim * 10 * 10

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!")


    def resultado_cm():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_cm = float(obtencion_R)
            valor_km = valor_cm / 10 / 10 / 10 / 10 / 10 
            valor_hm = valor_cm / 10 / 10 / 10 / 10
            valor_decam = valor_cm / 10 / 10 / 10 
            valor_m = valor_cm / 10 / 10
            valor_decim = valor_cm / 10
            valor_mm = valor_cm * 10 

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!")    

    def resultado_mm():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDL.get()
        try:
            valor_mm = float(obtencion_R)
            valor_km = valor_mm / 10 / 10 / 10 / 10 / 10 / 10 
            valor_hm = valor_mm / 10 / 10 / 10 / 10 / 10
            valor_decam = valor_mm / 10 / 10 / 10 / 10
            valor_m = valor_mm / 10 / 10 / 10
            valor_decim = valor_mm / 10 / 10
            valor_cm = valor_mm / 10 

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KM= " + str(valor_km),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hm = Label(ventana_resultado,
                                    text="HM= " + str(valor_hm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAM= " + str(valor_decam),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="M= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decim = Label(ventana_resultado,
                                    text="DECIM= " + str(valor_decim),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cm = Label(ventana_resultado,
                                    text="CM= " + str(valor_cm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_mm = Label(ventana_resultado,
                                    text="MM= " + str(valor_mm),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDL.delete(0, END)
            entrada_UDL.insert(0, "ERROR!!!") 

    relleno_3 = Label(ventana_UDL,
                        text="",
                      bg="gray").grid(row=3, column=1)
    
    boton_km = Button(ventana_UDL, 
                        text="KM",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_km,
                        bg="light gray",
                        fg="black").grid(row=4, column=0)
    boton_hm = Button(ventana_UDL, 
                        text="HM",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_hm,
                        bg="light gray",
                        fg="black").grid(row=4, column=1)
    boton_decam = Button(ventana_UDL, 
                        text="DECAM",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_decam,
                        bg="light gray",
                        fg="black").grid(row=4, column=2)
    boton_m = Button(ventana_UDL, 
                        text="M",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_m,
                        bg="light gray",
                        fg="black").grid(row=5, column=0)
    boton_decim = Button(ventana_UDL, 
                        text="DECIM",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_decim,
                        bg="light gray",
                        fg="black").grid(row=5, column=1)
    boton_cm = Button(ventana_UDL, 
                        text="CM",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_cm,
                        bg="light gray",
                        fg="black").grid(row=5, column=2)
    boton_mm = Button(ventana_UDL, 
                        text="MM",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_mm,
                        bg="light gray",
                        fg="black").grid(row=6, column=1)
    
def envia_boton_2():
    ventana_UCM = Toplevel()
    ventana_UCM.title("Unidad de Medida de Capacidad")
    ventana_UCM.geometry("570x400")
    ventana_UCM.config(background="gray")

    titulo_ventana = Label(ventana_UCM, 
                           text="UNIDAD DE MEDIDA DE CAPACIDAD",
                           bg="purple",
                           fg="white",
                           borderwidth=3,
                           border=3,
                           font=("Courier", 12)).grid(row=0, column=1)

    relleno_1 = Label(ventana_UCM, 
                      text="",
                      bg="gray").grid(row=0, column=0)
    relleno_2 = Label(ventana_UCM, 
                      text="",
                      bg="gray").grid(row=0, column=2)
    
    subtitulo_1 = Label(ventana_UCM,
                      text="Ingrese datos numericos: ",
                      bg="purple",
                      fg="white",
                      borderwidth=3,
                      border=3,
                      underline=True).grid(row=1, column=0)
    entrada_UCM = Entry(ventana_UCM)
    entrada_UCM.grid(row=1, column=1)
    
    subtitulo_2 = Label(ventana_UCM, 
                        text="Que Unidad es su dato numerico?",
                        bg="purple",
                        fg="white",
                        borderwidth=3,
                        border=3,
                        underline=True).grid(row=2, column=1)

    def resultado_kl():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_kl = float(obtencion_R)
            valor_hl = valor_kl * 10
            valor_decal = valor_kl * 10 * 10
            valor_l = valor_kl * 10 * 10 * 10
            valor_decil = valor_kl * 10 * 10 * 10 * 10
            valor_cl = valor_kl * 10 * 10 * 10 * 10 * 10
            valor_ml = valor_kl * 10 * 10 * 10 * 10 * 10 * 10

            etiqueta_valor_kl = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decal = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_l = Label(ventana_resultado,
                                    text="L= " + str(valor_l),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!")

    def resultado_hl():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_hl = float(obtencion_R)
            valor_kl = valor_hl / 10
            valor_decal = valor_hl * 10 
            valor_l = valor_hl * 10 * 10 
            valor_decil = valor_hl * 10 * 10 * 10 
            valor_cl = valor_hl * 10 * 10 * 10 * 10 
            valor_ml = valor_hl * 10 * 10 * 10 * 10 * 10 

            etiqueta_valor_kl = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decal = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_l = Label(ventana_resultado,
                                    text="L= " + str(valor_l),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!")
        
    def resultado_decal():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_decal = float(obtencion_R)
            valor_kl = valor_decal / 10 / 10
            valor_hl = valor_decal / 10 
            valor_l = valor_decal * 10  
            valor_decil = valor_decal * 10 * 10 
            valor_cl = valor_decal * 10 * 10 * 10 
            valor_ml = valor_decal * 10 * 10 * 10 * 10  

            etiqueta_valor_km = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decam = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_l= Label(ventana_resultado,
                                    text="L= " + str(valor_l),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!")
    
    def resultado_l():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_l = float(obtencion_R)
            valor_kl = valor_l / 10 / 10 / 10   
            valor_hl = valor_l / 10 / 10
            valor_decal = valor_l / 10  
            valor_decil = valor_l * 10 
            valor_cl = valor_l * 10 * 10 
            valor_ml = valor_l * 10 * 10 * 10 

            etiqueta_valor_kl = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decal = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_ml= Label(ventana_resultado,
                                    text="L= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!")
        
    def resultado_decil():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_decil = float(obtencion_R)
            valor_kl = valor_decil / 10 / 10 / 10 / 10 
            valor_hl = valor_decil / 10 / 10 / 10 
            valor_decal = valor_decil / 10 / 10 
            valor_l= valor_decil / 10 
            valor_cl = valor_decil * 10 
            valor_ml = valor_decil * 10 * 10

            etiqueta_valor_kl = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decal = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_ml= Label(ventana_resultado,
                                    text="L= " + str(valor_l),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!")


    def resultado_cl():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")
        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_cl = float(obtencion_R)
            valor_kl = valor_cl / 10 / 10 / 10 / 10 / 10 
            valor_hl = valor_cl / 10 / 10 / 10 / 10
            valor_decal = valor_cl / 10 / 10 / 10 
            valor_l= valor_cl / 10 / 10
            valor_decil = valor_cl / 10
            valor_ml = valor_cl * 10 

            etiqueta_valor_kl = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decal = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_l= Label(ventana_resultado,
                                    text="L= " + str(valor_l),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!")    

    def resultado_ml():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UCM.get()
        try:
            valor_ml = float(obtencion_R)
            valor_kl = valor_ml / 10 / 10 / 10 / 10 / 10 / 10 
            valor_hl = valor_ml / 10 / 10 / 10 / 10 / 10
            valor_decal = valor_ml / 10 / 10 / 10 / 10
            valor_ml= valor_ml / 10 / 10 / 10
            valor_decil = valor_ml / 10 / 10
            valor_cl = valor_ml / 10 

            etiqueta_valor_kl = Label(ventana_resultado,
                                    text="KL= " + str(valor_kl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_hl = Label(ventana_resultado,
                                    text="HL= " + str(valor_hl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_decal = Label(ventana_resultado,
                                    text="DECAL= " + str(valor_decal),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            etiqueta_valor_ml= Label(ventana_resultado,
                                    text="L= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=0)
            etiqueta_valor_decil = Label(ventana_resultado,
                                    text="DECIL= " + str(valor_decil),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=1)
            etiqueta_valor_cl = Label(ventana_resultado,
                                    text="CL= " + str(valor_cl),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=2, column=2)
            etiqueta_valor_ml = Label(ventana_resultado,
                                    text="ML= " + str(valor_ml),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=3, column=1)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UCM.delete(0, END)
            entrada_UCM.insert(0, "ERROR!!!") 

    relleno_3 = Label(ventana_UCM,
                        text="",
                      bg="gray").grid(row=3, column=1)
    
    boton_kl = Button(ventana_UCM, 
                        text="KL",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_kl,
                        bg="light gray",
                        fg="black").grid(row=4, column=0)
    boton_hl = Button(ventana_UCM, 
                        text="HL",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_hl,
                        bg="light gray",
                        fg="black").grid(row=4, column=1)
    boton_decal = Button(ventana_UCM, 
                        text="DECAL",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_decal,
                        bg="light gray",
                        fg="black").grid(row=4, column=2)
    boton_l= Button(ventana_UCM, 
                        text="L",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_l,
                        bg="light gray",
                        fg="black").grid(row=5, column=0)
    boton_decil = Button(ventana_UCM, 
                        text="DECIL",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_decil,
                        bg="light gray",
                        fg="black").grid(row=5, column=1)
    boton_cl = Button(ventana_UCM, 
                        text="CL",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_cl,
                        bg="light gray",
                        fg="black").grid(row=5, column=2)
    boton_ml = Button(ventana_UCM, 
                        text="ML",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_ml,
                        bg="light gray",
                        fg="black").grid(row=6, column=1)
    
def envia_boton_3():
    ventana_UDT = Toplevel()
    ventana_UDT.title("Unidad de Tiempo")
    ventana_UDT.geometry("455x165")
    ventana_UDT.config(background="gray")
    titulo_ventana = Label(ventana_UDT, 
                           text="UNIDAD DE TIEMPO",
                           bg="purple",
                           fg="white",
                           borderwidth=3,
                           border=3,
                           font=("Courier", 12)).grid(row=0, column=1)

    relleno_1 = Label(ventana_UDT, 
                      text="",
                      bg="gray").grid(row=0, column=0)
    relleno_2 = Label(ventana_UDT, 
                      text="",
                      bg="gray").grid(row=0, column=2)
    
    subtitulo_1 = Label(ventana_UDT,
                      text="Ingrese datos numericos: ",
                      bg="purple",
                      fg="white",
                      borderwidth=3,
                      border=3,
                      underline=True).grid(row=1, column=0)
    entrada_UDT = Entry(ventana_UDT)
    entrada_UDT.grid(row=1, column=1)
    
    subtitulo_2 = Label(ventana_UDT, 
                        text="Que Unidad es su dato numerico?",
                        bg="purple",
                        fg="white",
                        borderwidth=3,
                        border=3,
                        underline=True).grid(row=2, column=1)
    
    def resultado_h():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)
        
        obtencion_R = entrada_UDT.get()

        try:
            valor_h = float(obtencion_R)
            valor_m = valor_h * 60
            valor_s = valor_h * 60 * 60
            
            etiqueta_valor_h = Label(ventana_resultado,
                                    text="HORAS= " + str(valor_h),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="MINUTOS= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_s = Label(ventana_resultado,
                                    text="SEGUNDOS= " + str(valor_s),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
            
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDT.delete(0, END)
            entrada_UDT.insert(0, "ERROR!!!")

    def resultado_m():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDT.get()

        try:
            valor_m = float(obtencion_R)
            valor_h = valor_m / 60
            valor_s = valor_m * 60 
            
            etiqueta_valor_h = Label(ventana_resultado,
                                    text="HORAS= " + str(valor_h),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="MINUTOS= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_s = Label(ventana_resultado,
                                    text="SEGUNDOS= " + str(valor_s),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
            
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDT.delete(0, END)
            entrada_UDT.insert(0, "ERROR!!!")

    
    def resultado_s():
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="light green")

        titulo_resultado = Label(ventana_resultado,
                                 text="RESULTADO",
                                 bg="purple",
                                 font=("Courier"),
                                 fg="White").grid(row=0, column=1)

        obtencion_R = entrada_UDT.get()

        try:
            valor_s = float(obtencion_R)
            valor_h = valor_s / 60 / 60
            valor_m = valor_s / 60
            
            etiqueta_valor_h = Label(ventana_resultado,
                                    text="HORAS= " + str(valor_h),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=0)
            etiqueta_valor_m = Label(ventana_resultado,
                                    text="MINUTOS= " + str(valor_m),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=1)
            etiqueta_valor_s = Label(ventana_resultado,
                                    text="SEGUNDOS= " + str(valor_s),
                                    bg="green",
                                    fg="white",
                                    border=2).grid(row=1, column=2)
            boton_despejar = Button(ventana_resultado,
                                    text="DESPEJAR",
                                    command=ventana_resultado.destroy,
                                    bg="red").grid(row=4, column=1)
            
        except ValueError:
            destruccion_ventana = ventana_resultado.destroy
            entrada_UDT.delete(0, END)
            entrada_UDT.insert(0, "ERROR!!!")



    boton_h = Button(ventana_UDT, 
                       text="HORA",
                       borderwidth=3,
                       width=15,
                       height=5,
                       command=resultado_h,
                       bg="light gray",
                       fg="black").grid(row=4, column=0)
    boton_m = Button(ventana_UDT, 
                        text="MINUTO",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_m,
                        bg="light gray",
                        fg="black").grid(row=4, column=1)
    boton_s = Button(ventana_UDT, 
                        text="SEGUNDO",
                        borderwidth=3,
                        width=15,
                        height=5,
                        command=resultado_s,
                        bg="light gray",
                        fg="black").grid(row=4, column=2)



boton_1 = Button(root, 
                 text="Unidad de longitud", 
                 command=envia_boton_1,
                 bg="cyan",
                 fg="black").grid(row=3, column=0)


boton_2 = Button(root, 
                 text="Unidad de Medida de Capacidad",
                 command=envia_boton_2,
                 bg="cyan",
                 fg="black").grid(row=3, column=1)

boton_3 = Button(root, 
                text="Unidad de tiempo",
                command=envia_boton_3,
                 bg="cyan",
                 fg="black").grid(row=3, column=2)

mainloop()