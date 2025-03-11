from ZODB import FileStorage, DB  
from BTrees.OOBTree import OOBTree  
import transaction

class BibliotecaDB:
    def __init__(self):
        self.storage = FileStorage.FileStorage('biblioteca.fs')
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        if not hasattr(self.root, 'usuarios'):
            self.root.usuarios = OOBTree()
        if not hasattr(self.root, 'funcionarios'):
            self.root.funcionarios = OOBTree()
        if not hasattr(self.root, 'livros'):
            self.root.livros = OOBTree()
        if not hasattr(self.root, 'emprestimos'):
            self.root.emprestimos = OOBTree()
        transaction.commit()

    def fechar(self):
        self.connection.close()
        self.db.close()
        self.storage.close()

    def salvar_usuario(self, usuario):
        self.root.usuarios[usuario.id_usuario] = usuario
        transaction.commit()

    def buscar_usuario(self, id_usuario):
        return self.root.usuarios.get(id_usuario)

    def listar_usuarios(self):
        return list(self.root.usuarios.values())

    def salvar_funcionario(self, funcionario):
        self.root.funcionarios[funcionario.id_funcionario] = funcionario
        transaction.commit()

    def buscar_funcionario(self, id_funcionario):
        return self.root.funcionarios.get(id_funcionario)

    def salvar_livro(self, livro):
        self.root.livros[livro.codigolivro] = livro
        transaction.commit()

    def buscar_livro(self, codigolivro):
        return self.root.livros.get(codigolivro)

    def editar_livro(self, codigolivro, novo_nome, novo_autor):
        livro = self.buscar_livro(codigolivro)
        if livro:
            livro.nome = novo_nome
            livro.autor = novo_autor
            transaction.commit()
            print(f"Livro '{livro.nome}' editado com sucesso!")
        else:
            print("Livro não encontrado!")

    def listar_livros_disponiveis(self):
        return [livro for livro in self.root.livros.values() if livro.disponivel]

    def salvar_emprestimo(self, emprestimo):
        self.root.emprestimos[emprestimo.id] = emprestimo
        transaction.commit()

    def buscar_emprestimo(self, id_emprestimo):
        return self.root.emprestimos.get(id_emprestimo)

    def listar_emprestimos_ativos(self):
        return [emp for emp in self.root.emprestimos.values() if not emp.devolvido]
