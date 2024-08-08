import sqlite3

db_string = 'crud_usuarios.db'

conn = sqlite3.connect(db_string)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

conn.commit()


def criar_usuario(nome, idade, email):
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)
        ''', (nome, idade, email))
        conn.commit()
        print("Usuário criado com sucesso!")
    except sqlite3.IntegrityError:
        print("Error: Email já cadastrado.")

def ler_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    return usuarios

def ler_usuario_por_id(user_id):
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
    usuarios = cursor.fetchone()
    return usuarios

def atualizar_usuario(user_id, novo_nome, nova_idade, novo_email):
    try:
        cursor.execute('''
                       UPDATE usuarios
                       SET nome = ?, idade = ?, email = ?
                       WHERE id = ?
        ''', (novo_nome, nova_idade, novo_email, user_id))
        conn.commit()
        print("Usuário atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Email já cadastrado.")

def deletar_usuario(user_id):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()
    print("Usuário deletado com sucesso!")


# criar_usuario("Lootiano", 20, "lucianograbin12@gmail.com")
# criar_usuario('Alice', 30, 'alice@example.com')
# criar_usuario('Bob', 25, 'bob@example.com')

def read_user():
    print("Lista de Usuários:")
    usuarios = ler_usuarios()
    for usuario in usuarios:
        print(usuario)

def read_from_id(user_id):
    print(f'\nDetalhes do Usuário ID {user_id}:')
    usuario = ler_usuario_por_id(2)
    if usuario:
        print(usuario)
    else:
        print("Usuário não encontrado.")

def update_user(user_id):
    print(f'\nAtualizando Usuário ID  {user_id}:')
    atualizar_usuario(user_id, 'Alice Martins', 31, 'alice.martins@example.com')

    print("\nLista de usuários atualizada:")
    usuarios = ler_usuarios()
    for usuario in usuarios:
        print(usuario)

def delete_user(user_id):
    print(f'\nDeletando usuário ID {user_id}:')
    deletar_usuario(3)

# read_from_id(3)
# update_user(1)
# deletar_usuario(1)

conn.close()