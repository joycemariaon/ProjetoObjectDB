from modelos import Usuario, Funcionario, Livro, Emprestimo
from biblioteca_db import BibliotecaDB

usuario_id = 1
funcionario_id = 1
livro_id = 1
emprestimo_id = 1

def usuario_crud():
    while True:
        print("\nSubmenu Usuário:")
        print("1 - Criar Usuário")
        print("2 - Buscar Usuário")
        print("3 - Atualizar Usuário")
        print("4 - Remover Usuário")
        print("5 - Voltar ao menu")

        choice = input("Escolha uma opção de 1 a 5:")

        if choice == '1':
            db = BibliotecaDB()
            try:
                global usuario_id
                nome = input("Insira o nome do usuário: ")
                cpf = input("Insira o CPF do usuário: ")
                email = input("Insira o email do usuário: ")
                numero_cartao = input("Insira o número do cartão do usuário: ")

                usuario = Usuario(usuario_id, nome, cpf, email, numero_cartao)
                db.salvar_usuario(usuario)
                usuario_id += 1
                print(f"Usuário {usuario.nome} ({usuario.id_usuario}) salvo com sucesso!")
            finally:
                db.fechar()

        elif choice == '2':
            db = BibliotecaDB()
            try:
                id_usuario = int(input("Digite o id do usuário: "))
                usuario = db.buscar_usuario(id_usuario)
                if usuario:
                    print(f"Usuário: ID={usuario.id_usuario}, Nome={usuario.nome}, CPF={usuario.cpf}, Email={usuario.email}, Cartão={usuario.numero_cartao}")
                else:
                    print(f"Usuário com ID {id_usuario} não encontrado.")
            finally:
                db.fechar()

        elif choice == '3':
            db = BibliotecaDB()
            try:
                id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
                usuario = db.buscar_usuario(id_usuario)
                if usuario:
                    print(f"\nUsuário encontrado: {usuario.nome} (ID: {usuario.id_usuario})")
                    print("O que você gostaria de atualizar?")
                    print("1 - Nome")
                    print("2 - CPF")
                    print("3 - Email")
                    print("4 - Número do Cartão")
                    print("5 - Voltar")

                    update_choice = input("Escolha uma opção de 1 a 5:")

                    if update_choice == '1':
                        nome = input(f"Digite o novo nome (atual: {usuario.nome}): ")
                        usuario.nome = nome
                        db.salvar_usuario(usuario)
                        print(f"Nome atualizado para: {usuario.nome}")
                    elif update_choice == '2':
                        cpf = input(f"Digite o novo CPF (atual: {usuario.cpf}): ")
                        usuario.cpf = cpf
                        db.salvar_usuario(usuario)
                        print(f"CPF atualizado para: {usuario.cpf}")
                    elif update_choice == '3':
                        email = input(f"Digite o novo email (atual: {usuario.email}): ")
                        usuario.email = email
                        db.salvar_usuario(usuario)
                        print(f"Email atualizado para: {usuario.email}")
                    elif update_choice == '4':
                        numero_cartao = input(f"Digite o novo número do cartão (atual: {usuario.numero_cartao}): ")
                        usuario.numero_cartao = numero_cartao
                        db.salvar_usuario(usuario)
                        print(f"Número do cartão atualizado para: {usuario.numero_cartao}")
                    elif update_choice == '5':
                        print("Voltando ao menu...")
                        return  
                    else:
                        print("Opção inválida.")
                else:
                    print(f"Usuário com ID {id_usuario} não encontrado.")
            finally:
                db.fechar()

        elif choice == '4':
            db = BibliotecaDB()
            try:
                id_usuario = int(input("Digite o ID do usuário a ser removido: "))
                usuario = db.buscar_usuario(id_usuario)
                if usuario:
                    db.remover_usuario(usuario)
                    print(f"Usuário {usuario.nome} ({usuario.id_usuario}) removido com sucesso!")
                else:
                    print(f"Usuário com ID {id_usuario} não encontrado.")
            finally:
                db.fechar()

        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente uma das opções exibidas acima.")

def funcionario_crud():
    while True:
        print("\nSubmenu Funcionário:")
        print("1 - Criar Funcionário")
        print("2 - Buscar Funcionário Por ID")
        print("3 - Atualizar Funcionário")
        print("4 - Remover Funcionário")
        print("5 - Voltar ao menu principal")

        choice = input("Escolha uma opção de 1 a 5: ")

        if choice == '1':
            db = BibliotecaDB()
            try:
                global funcionario_id
                nome = input("Insira o nome do funcionário: ")
                cpf = input("Insira o CPF do funcionário: ")
                email = input("Insira o email do funcionário: ")
                matricula = input("Insira a matrícula do funcionário: ")
                cargo = input("Insira o cargo do funcionário: ")

                funcionario = Funcionario(funcionario_id, nome, cpf, email, matricula, cargo)
                db.salvar_funcionario(funcionario)
                funcionario_id += 1
                print(f"Funcionário {funcionario.nome} (matrícula: {funcionario.matricula}) salvo com sucesso!")
            finally:
                db.fechar()

        elif choice == '2':
            db = BibliotecaDB()
            try:
                id = int(input("Digite o ID do funcionário: "))
                funcionario = db.buscar_funcionario(id)
                if funcionario:
                    print(f"Funcionário {funcionario.nome} (ID: {funcionario.id_funcionario}) encontrado")
                else:
                    print(f"Funcionário com ID {id} não encontrado.")
            finally:
                db.fechar()

        elif choice == '3':
            db = BibliotecaDB()
            try:
                funcionario_id = int(input("Digite o ID do Funcionário a ser atualizado: "))
                funcionario = db.buscar_funcionario(funcionario_id)
                if funcionario:
                    print(f"\nFuncionário encontrado: {funcionario.nome} (ID: {funcionario.id_funcionario})")
                    print("O que você gostaria de atualizar?")
                    print("1 - Nome")
                    print("2 - CPF")
                    print("3 - Email")
                    print("4 - Cargo")
                    print("5 - Voltar")

                    update_choice = input("Escolha uma opção de 1 a 5:")

                    if update_choice == '1':
                        nome = input(f"Digite o novo nome (atual: {funcionario.nome}): ")
                        funcionario.nome = nome
                        db.salvar_funcionario(funcionario)
                        print(f"Nome atualizado para: {funcionario.nome}")
                    elif update_choice == '2':
                        cpf = input(f"Digite o novo CPF (atual: {funcionario.cpf}): ")
                        funcionario.cpf = cpf
                        db.salvar_funcionario(funcionario)
                        print(f"CPF atualizado para: {funcionario.cpf}")
                    elif update_choice == '3':
                        email = input(f"Digite o novo email (atual: {funcionario.email}): ")
                        funcionario.email = email
                        db.salvar_funcionario(funcionario)
                        print(f"Email atualizado para: {funcionario.email}")
                    elif update_choice == '4':
                        cargo = input(f"Digite o novo cargo (atual: {funcionario.cargo}): ")
                        funcionario.cargo = cargo
                        db.salvar_funcionario(funcionario)
                        print(f"Cargo atualizado para: {funcionario.cargo}")
                    elif update_choice == '5':
                        print("Voltando ao menu...")
                        return 
                    else:
                        print("Opção inválida.")
                else:
                    print(f"Funcionário com ID {funcionario_id} não encontrado.")
            finally:
                db.fechar()

        elif choice == '4':
            db = BibliotecaDB()
            try:
                id_funcionario = int(input("Digite o ID do funcionário a ser removido: "))
                funcionario = db.buscar_funcionario(id_funcionario)
                if funcionario:
                    db.remover_funcionario(funcionario)
                    print(f"Funcionário {funcionario.nome} (matrícula: {funcionario.matricula}) removido com sucesso!")
                else:
                    print(f"Funcionário com ID {id_funcionario} não encontrado.")
            finally:
                db.fechar()

        elif choice == '5':
            print("Voltando ao menu principal...")  
            return  
        else:
            print("Opção inválida. Tente novamente uma das opções exibidas acima.")



def livro_crud():
    while True:
        print("\nSubmenu Livro:")
        print("1 - Criar Livro")
        print("2 - Buscar Livro por ID")
        print("3 - Atualizar Livro")
        print("4 - Remover Livro")
        print("5 - Voltar ao menu principal")

        choice = input("Escolha uma opção de 1 a 5:")

        if choice == '1':
            db = BibliotecaDB()

            try:
                global livro_id
                titulo = input('Insira o título do livro: ')
                autor = input('Insira o nome do autor do livro: ')
                isbn = input('Insira o ISBN do livro: ')

                livro = Livro(livro_id, titulo, autor, isbn)
                db.salvar_livro(livro)
                livro_id += 1
                print(f"Livro {livro.titulo} cadastrado com sucesso")
            finally:
                db.fechar()
        elif choice == '2':
            db = BibliotecaDB()
            try:
                id = input('Digite o ID do livro')

                livro = db.buscar_livro(id)
                print(f'Livro {livro.titulo} encontrado')
            finally:
                db.fechar()

       

        elif choice == '4':
            db = BibliotecaDB()

            try:
                livros = db.listar_livros_disponiveis()
                for livro in livros:
                    print(f"Livro: ID={livro.id}, título={livro.titulo}, ISBN={livro.isbn}, autor={livro.autor}")
            finally:
                db.fechar()

        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente uma das opções exibidas acima.")
  
def emprestimo_crud():
    while True:
        print("\nSubmenu Empréstimo:")
        print("1 - Criar Empréstimo")
        print("2 - Buscar Empréstimo por ID")
        print("3 - Buscar Empréstimos Ativos")
        print("4 - Remover Empréstimos")
        print("5 - Voltar ao menu principal")

        choice = input("Escolha uma opção de 1 a 5: ")

        if choice == '1':
            db = BibliotecaDB()

            try:
                global emprestimo_id
                id_usuario = int(input('Digite o ID do usuário: '))
                id_livro = int(input('Digite o ID do livro: '))

                usuario = db.buscar_usuario(id_usuario)
                livro = db.buscar_livro(id_livro)

                if usuario and livro:
                    emprestimo = Emprestimo(emprestimo_id, usuario, livro)
                    db.salvar_emprestimo(emprestimo)
                    emprestimo_id += 1
                    print(f"Empréstimo do livro {emprestimo.livro.titulo} ao usuário {emprestimo.usuario.nome} cadastrado com sucesso!")
                else:
                    print("Usuário ou livro não encontrados.")
            finally:
                db.fechar()

        elif choice == '2':
            db = BibliotecaDB()

            try:
                id_emprestimo = int(input("Digite o ID do empréstimo: "))
                emprestimo = db.buscar_emprestimo(id_emprestimo)

                if emprestimo:
                    print(f"Livro {emprestimo.livro.titulo} emprestado ao usuário {emprestimo.usuario.nome} na data {emprestimo.data_emprestimo}. Devolução prevista para {emprestimo.data_devolucao}.")
                else:
                    print(f"Empréstimo com ID {id_emprestimo} não encontrado.")
            finally:
                db.fechar()

        elif choice == '3':
            db = BibliotecaDB()

            try:
                emprestimos_ativos = db.listar_emprestimos_ativos()

                if emprestimos_ativos:
                    for emprestimo in emprestimos_ativos:
                        print(f"Livro {emprestimo.livro.titulo} emprestado ao usuário {emprestimo.usuario.nome} na data {emprestimo.data_emprestimo}. Devolução prevista para {emprestimo.data_devolucao}.")
                else:
                    print("Não há empréstimos ativos.")
            finally:
                db.fechar()

        elif choice == '4':
            db = BibliotecaDB()
            try:
                id_emprestimo = int(input("Digite o ID do empréstimo a ser removido: "))
                emprestimo = db.buscar_emprestimo(id_emprestimo)
                if emprestimo:
                    db.remover_emprestimo(emprestimo)
                    print(f"Empréstimo do livro {emprestimo.livro.titulo} removido com sucesso!")
                else:
                    print(f"Empréstimo com ID {id_emprestimo} não encontrado.")
            finally:
                db.fechar()

        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente uma das opções exibidas acima.")


def main():
    while True:
        print("\nMenu:")
        print("1 - Usuário")
        print("2 - Funcionário")
        print("3 - Livro")
        print("4 - Empréstimo")
        print("5 - Sair")

        choice = input("Escolha uma das opções: ")

        if choice == '1':
            usuario_crud()
        elif choice == '2':
            funcionario_crud()
        elif choice == '3':
            livro_crud()
        elif choice == '4':
            emprestimo_crud()
        elif choice == '5':
            print("Saindo do sistema")
            break  
        else:
            print("Opção inválida. Tente novamente uma das opções exibidas acima.")

if __name__ == "__main__":
    main()

