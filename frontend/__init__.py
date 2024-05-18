from tkinter import *

class Gui:
    '''
    classe que define a interface grafica da aplicação
    '''
    janela = Tk()
    janela.wm_title("Cadatro de Clientes")
    janela.geometry('440x350+500+200')
    janela.resizable(False, False)

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    lblNome = Label(janela, text="Nome")
    lblSobrenome = Label(janela, text="Sobrenome")
    lblEmail = Label(janela, text="Email")
    lblCPF = Label(janela, text="CPF")

    entNome = Entry(janela, textvariable=txtNome)
    entSobrenome = Entry(janela, textvariable=txtSobrenome)
    entEmail = Entry(janela, textvariable=txtEmail)
    entCPF = Entry(janela, textvariable=txtCPF)

    listClientes = Listbox(janela)
    scrollClientes = Scrollbar(janela)

    btnVerTodos = Button(janela,text="Ver Todos")
    btnBuscar = Button(janela, text="Buscar")
    btnInserir = Button(janela, text="Inserir")
    btnAtualizar = Button(janela, text="Atualizar Selecionados")
    btnDeletar = Button(janela, text="Deletar Selecionados")
    btnFechar = Button(janela, text="Fechar")




    lblNome.grid(row=0, column=0)
    lblSobrenome.grid(row=1, column=0)
    lblEmail.grid(row=2, column=0)
    lblCPF.grid(row=3, column=0)

    entNome.grid(row=0, column=1)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)

    btnVerTodos.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnAtualizar.grid(row=7, column=0, columnspan=2)
    btnDeletar.grid(row=8, column=0, columnspan=2)
    btnFechar.grid(row=9, column=0, columnspan=2)

    listClientes.configure(yscrollcommand=scrollClientes.set)

    scrollClientes.configure(command=listClientes.yview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    for child in janela.winfo_children():
        classe_widget = child.__class__.__name__
        if classe_widget == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif classe_widget == "Listbox":
            child.grid_configure(sticky='NS', padx=0, pady=0 )
        elif classe_widget == "Scrollbar":
            child.grid_configure(sticky='NS', padx=0, pady=0)
        else:
            child.grid_configure(sticky='N', padx=x_pad, pady=y_pad)
            

    def run(self):
        Gui.janela.mainloop()