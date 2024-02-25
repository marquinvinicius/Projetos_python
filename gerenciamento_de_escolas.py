import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='projetoescola',
)
cursor = conexao.cursor()

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []

    def __int__(self):
        return self.idade

    def __str__(self):
        return self.nome

    def adicionar_nota(self):
        nota = int(input('Qual o valor da nota? '))
        q = int(input('Qual a nota [1,2,3]: '))
        comando = f"""update alunos
        set nota{q} = {nota}
        where nome = '{self.nome}'"""
        cursor.execute(comando)
        conexao.commit()

    def exibir(self):
        return print(f'Nome: {self.nome}\n'
                     f'Idade: {self.idade}\n'
                     f'Notas: {self.notas}\n'
                     f'Media: {self.medias():.1f}')
    def medias(self):
        r = 0
        for x in self.notas:
            r += x
        me = r / len(self.notas)
        return me
    def registrar(self):
        comando = f'''insert into alunos (nome)
                    value ('{self.nome}')'''
        cursor.execute(comando)
        conexao.commit()


class Escola():
    def __init__(self, nome, limite_alunos):
        self.nome = nome
        self.limite_alunos = limite_alunos
    def __str__(self):
        return f"{self.nome}"
    def __int__(self):
        return self.limite_alunos

    def registrar(self):
        comando = f'''insert into escolas (nome, limite_alunos)
                    values ('{self.nome}', '{self.limite_alunos}')'''
        cursor.execute(comando)
        conexao.commit()

class Matricula:
    def __init__(self, aluno, escola):
        self.aluno = aluno
        self.escola = escola

    def __str__(self):
        return self.aluno
