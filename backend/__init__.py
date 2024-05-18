import sqlite3


class Banco:
    def __init__(self) -> None:
        self.database = 'usuarios.db'
        self.conn = None
        self.cur = None
        self.conectado = False


    def conectar(self):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        self.conectado = True
    

    def executar(self, sql, parametros = None):
        if self.conectado:
            if parametros is not None:
                self.cur.execute(sql, parametros)
            else:
                self.cur.execute(sql)
            return True
        else:
            return False


    def desconectar(self):
        self.conn.close()
        self.conectado = False

    
    def mostrar(self):
        return self.cur.fetchall()


    def persistir(self):
        if self.conectado:
            self.conn.commit()
            return True
        else:
            return False
        

def iniciar_banco():
    controle = Banco()
    controle.conectar()
    controle.executar("CREATE TABLE IF NOT EXISTS cadastros ("
                      "id INTEGER PRIMARY KEY NOT NULL," 
                      "nome TEXT,"
                      "sobrenome TEXT,"
                      "cpf TEXT," 
                      "email TEXT)")
    controle.persistir()
    controle.desconectar()


def ver():
    controle = Banco()
    controle.conectar()
    controle.executar("SELECT * FROM cadastros")
    linhas = controle.mostrar()
    controle.desconectar()
    return linhas


def inserir(nome, sobrenome, cpf, email):
    controle = Banco()
    controle.conectar()
    controle.executar('INSERT INTO cadastros VALUES(NULL, ?, ?, ?, ?)', (nome, sobrenome, cpf, email)) 
    controle.persistir()
    controle.desconectar()


def procurar(nome='', sobrenome='', email='', cpf=''):
    controle = Banco()
    controle.conectar()
    controle.executar('SELECT * FROM cadastros WHERE nome=? or sobrenome=? or email=? or cpf=?', (nome, sobrenome, email, cpf))
    linha = controle.mostrar()
    controle.desconectar()
    return linha


def atualizar(id, nome, sobrenome, email, cpf):
    controle = Banco()
    controle.conectar()
    controle.executar('UPDATE cadastros SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?', (nome, sobrenome, email, cpf, int(id)))
    controle.persistir()
    controle.desconectar()


def deletar(id):
    controle = Banco()
    controle.conectar()
    controle.executar('DELETE FROM cadastros WHERE id=?', (str(id)))
    controle.persistir()
    controle.desconectar()
