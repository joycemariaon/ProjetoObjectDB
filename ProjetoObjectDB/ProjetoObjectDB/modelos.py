from persistent import Persistent

class Persistent:
    def salvar(self):
        pass
    
    def remover(self):
        pass
    
    def buscar(self):
        pass

class Livro(Persistent):
    def __init__(self, id, nome, autor, codigolivro):
        self.id = id
        self.nome = nome
        self.autor = autor
        self.codigolivro = codigolivro
        self.disponivel = True

    def __str__(self):
        return f"Livro: {self.nome}, Autor: {self.autor}, Código: {self.codigolivro}"

    def mudar_disponibilidade(self, disponibilidade):
        self.disponivel = disponibilidade
        status = "disponível" if disponibilidade else "não disponível"
        print(f"O livro {self.nome} agora está {status}.")

class Usuario(Persistent):
    def __init__(self, id_usuario, nome, cpf, email, numero_cartao ):
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.numero_cartao = numero_cartao 

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id_usuario}, CPF: {self.cpf}, Email: {self.email}"

class Funcionario(Persistent):
    def __init__(self, id_funcionario, nome, cpf, email, matricula, cargo):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.matricula = matricula
        self.cargo = cargo
    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id_funcionario}"

class Emprestimo(Persistent):
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.devolvido = False

    def __str__(self):
        status = "Devolvido" if self.devolvido else "Não devolvido"
        return f"Livro: {self.livro.nome}, Usuário: {self.usuario.nome}, Empréstimo: {self.data_emprestimo}, Devolução: {self.data_devolucao}, Status: {status}"

    def devolver(self):
        self.devolvido = True

    def verificar_disponibilidade(self):
        if self.livro.disponivel:
            print(f"O livro {self.livro.nome} está disponível para empréstimo.")
        else:
            print(f"O livro {self.livro.nome} não está disponível.")
