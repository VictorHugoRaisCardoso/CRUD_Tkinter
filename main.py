from frontend import *
import backend as core


app = None
app = Gui()

core.iniciar_banco()


def comando_ver():
    linhas = core.ver()
    app.listClientes.delete(0,END)
    for linha in linhas:
        app.listClientes.insert(END, linha)


def comando_procurar():
    app.listClientes.delete(0, END)
    linhas = core.procurar(
        app.txtNome.get(), 
        app.txtSobrenome.get(),
        app.txtEmail.get(), 
        app.txtCPF.get())
    for linha in linhas:
        app.listClientes.insert(END, linha)


def comando_inserir():
    core.inserir(
        app.txtNome.get(),
        app.txtSobrenome.get(),
        app.txtEmail.get(),
        app.txtCPF.get())
    comando_ver()


def getSelecionarLinha(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])


app.listClientes.bind('<<ListboxSelect>>', getSelecionarLinha)

def comando_atualizar():
    core.atualizar(selected[0], 
                app.txtNome.get(),
                app.txtSobrenome.get(),
                app.txtEmail.get(),
                app.txtCPF.get())
    comando_ver()


def comando_deletar():
    id = selected[0]
    core.deletar(id)
    comando_ver()



app.btnVerTodos.configure(command=comando_ver)
app.btnBuscar.configure(command=comando_procurar)
app.btnInserir.configure(command=comando_inserir)
app.btnAtualizar.configure(command=comando_atualizar)
app.btnDeletar.configure(command=comando_deletar)
app.btnFechar.configure(command=app.janela.destroy)

if __name__ == '__main__':
    app.run()