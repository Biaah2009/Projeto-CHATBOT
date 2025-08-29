import sqlite3

def get_connection():
    conn = sqlite3.connect("funcionarios.db", check_same_thread=False)
    return conn

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   cargo TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL
                   )
    """ )
    conn.commit()
    conn.close()

def inserir_funcionarios(nome, cargo,email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcinarios (nome,cargo,email) VALUES (?,?,?)",(nome,cargo,email))
    conn.commit()
    conn.close()

def listar_funcionarios():
    conn = get_connection()
    cursor = conn.cursor()
    data = cursor.fetchall()
    conn.close()
    return data
     