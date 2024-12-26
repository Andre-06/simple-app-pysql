from sqlite3.dbapi2 import Connection, Cursor
import sqlite3 as sql


class TransactionObject:
    database = "clientes.sqlite"
    conn: Connection = None
    cursor: Cursor = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cursor = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, query, parms=None):
        if not TransactionObject.connected:
            return False

        if parms:
            TransactionObject.cursor.execute(query, parms)
        else:
            TransactionObject.cursor.execute(query)

        return True

    def fetchall(self):
        return TransactionObject.cursor.fetchall()

    def persist(self):
        if not TransactionObject.connected:
            return False

        TransactionObject.conn.commit()
        return True


def init_db():
    trans = TransactionObject()
    trans.connect()

    trans.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome VARCHAR(100) NOT NULL,
            sobrenome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            cpf VARCHAR(11) NOT NULL
        )
    """)

    trans.persist()
    trans.disconnect()


def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()

    trans.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?) ", (nome, sobrenome, email, cpf))

    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()

    trans.execute("SELECT * FROM clientes")

    rows = trans.fetchall()

    trans.disconnect()
    return rows


def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObject()
    trans.connect()

    trans.execute("SELECT * FROM clientes WHERE nome =? or sobrenome =? or email =? or cpf =? ",
                  (nome, sobrenome, email, cpf))
    rows = trans.fetchall()

    trans.disconnect()
    return rows


def delete(codigo):
    trans = TransactionObject()
    trans.connect()

    trans.execute("DELETE FROM clientes WHERE codigo = ?", (codigo,))
    trans.persist()

    trans.disconnect()


def update(codigo, nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()

    trans.execute("UPDATE clientes SET nome =? , sobrenome =? , email =? , cpf =? WHERE codigo = ?",
                  (nome, sobrenome, email, cpf, codigo))

    trans.persist()
    trans.disconnect()


init_db()
