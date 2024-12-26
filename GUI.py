from tkinter import *


class Gui:
    x_pad = 5
    y_pad = 5
    width_entry = 30

    window = Tk()
    window.wm_title("SIMPLE APP - PYSQL")

    txt_nome = StringVar()
    txt_sobrenome = StringVar()
    txt_email = StringVar()
    txt_CPF = StringVar()

    lbl_nome = Label(window, text="Nome")
    lbl_sobrenome = Label(window, text="Sobrenome")
    lbl_email = Label(window, text="Email")
    lbl_CPF = Label(window, text="CPF")

    ent_nome = Entry(window, textvariable=txt_nome, width=width_entry)
    ent_sobrenome = Entry(window, textvariable=txt_sobrenome, width=width_entry)
    ent_email = Entry(window, textvariable=txt_email, width=width_entry)
    ent_CPF = Entry(window, textvariable=txt_CPF, width=width_entry)

    list_clients = Listbox(window, width=100)
    scroll_clients = Scrollbar(window)

    btn_view_all = Button(window, text="Ver Todos")
    btn_buscar = Button(window, text="Buscar")
    btn_inserir = Button(window, text="Inserir")
    btn_update = Button(window, text="Atualizar Selecionados")
    btn_del = Button(window, text="Deletar Selecionados")
    btn_close = Button(window, text="Fechar")

    lbl_nome.grid(row=0,column=0)
    lbl_sobrenome.grid(row=1,column=0)
    lbl_email.grid(row=2,column=0)
    lbl_CPF.grid(row=3, column=0)
    ent_nome.grid(row=0, column=1, padx=50, pady=50)
    ent_sobrenome.grid(row=1, column=1)
    ent_email.grid(row=2, column=1)
    ent_CPF.grid(row=3, column=1)
    list_clients.grid(row=0, column=2, rowspan=10)
    scroll_clients.grid(row=0, column=6, rowspan=10)
    btn_view_all.grid(row=4, column=0, columnspan=2)
    btn_buscar.grid(row=5, column=0, columnspan=2)
    btn_inserir.grid(row=6, column=0, columnspan=2)
    btn_update.grid(row=7, column=0, columnspan=2)
    btn_del.grid(row=8, column=0, columnspan=2)
    btn_close.grid(row=9, column=0, columnspan=2)

    list_clients.configure(yscrollcommand=scroll_clients.set)
    scroll_clients.configure(command=list_clients.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')


    def run(self):
        Gui.window.mainloop()

