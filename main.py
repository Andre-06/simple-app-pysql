from GUI import *
import connector as core

app: Gui = None


def view_command():
    rows = core.view()
    app.list_clients.delete(0, END)
    for r in rows:
        app.list_clients.insert(END, r)


def search_command():
    rows = core.search(app.txt_nome.get(),
                       app.txt_sobrenome.get(),
                       app.txt_email.get(),
                       app.txt_CPF.get())

    app.list_clients.delete(0, END)
    for r in rows:
        app.list_clients.insert(END, r)


def insert_command():
    nome = app.txt_nome.get().strip()
    sobrenome = app.txt_sobrenome.get().strip()
    email = app.txt_email.get().strip()
    cpf = app.txt_CPF.get().strip()

    if nome and sobrenome and email and cpf:
        core.insert(nome, sobrenome, email, cpf)
        view_command()


def update_command():
    if app.list_clients.curselection():
        index = app.list_clients.curselection()[0]
        selected = app.list_clients.get(index)
        core.update(selected[0],
                    app.txt_nome.get(),
                    app.txt_sobrenome.get(),
                    app.txt_email.get(),
                    app.txt_CPF.get())

        view_command()


def del_command():
    selecteds = app.list_clients.curselection()
    for index in selecteds:
        selected = app.list_clients.get(index)
        core.delete(selected[0])

    view_command()


def get_selected_row(event):
    index = app.list_clients.curselection()[0]
    selected = app.list_clients.get(index)

    app.ent_nome.delete(0, END)
    app.ent_nome.insert(END, selected[1])
    app.ent_sobrenome.delete(0, END)
    app.ent_sobrenome.insert(END, selected[2])
    app.ent_email.delete(0, END)
    app.ent_email.insert(END, selected[3])
    app.ent_CPF.delete(0, END)
    app.ent_CPF.insert(END, selected[4])


if __name__ == "__main__":
    app = Gui()

    app.list_clients.bind("<<ListboxSelect>>", get_selected_row)

    app.btn_view_all.configure(command=view_command)
    app.btn_buscar.configure(command=search_command)
    app.btn_inserir.configure(command=insert_command)
    app.btn_update.configure(command=update_command)
    app.btn_del.configure(command=del_command)
    app.btn_close.configure(command=app.window.destroy)

    app.run()








