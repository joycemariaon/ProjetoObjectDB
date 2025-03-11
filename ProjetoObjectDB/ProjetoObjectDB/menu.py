from modelos import Usuario, Funcionario, Livro, Emprestimo
from biblioteca_db import BibliotecaDB

db = BibliotecaDB()

def menu():
    while True:
        try:
            print("Selecione a opção: ")
            print(" 1. Usuário")
            print(" 2. Funcionário")
            print(" 3. Livros")
            print(" 4. Empréstimo")
            print(" 5. Sair")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                print("Usuário: ")
                print("1. Criar usuário")
                print("2. Editar usuário")
                print("3. Remover usuário")

                opc = int(input("Selecione uma opção: "))

                if opc == 1:
                    nome = input("Digite o nome: ")
                    cpf = input("Digite o CPF: ")
                    email = input("Digite o email: ")
                    
                    
                    usuario = Usuario(None, nome, cpf, email)  
                    db.salvar_usuario(usuario)
                    print("Usuário criado com sucesso!")

                elif opc == 2:
                    cpf = input("Digite o CPF do usuário que deseja editar: ")
                    usuario = db.buscar_usuario_por_cpf(cpf)

                    if usuario:
                        novo_nome = input("Novo nome: ")
                        novo_email = input("Novo email: ")
                        db.editar_usuario(cpf, novo_nome, novo_email)
                        print("Usuário atualizado com sucesso!")
                    else:
                        print("Usuário não encontrado.")

                elif opc == 3:
                    cpf = input("Digite o CPF do usuário que deseja remover: ")
                    usuario = db.buscar_usuario_por_cpf(cpf)

                    if usuario:
                        db.remover_usuario(cpf)
                        print("Usuário removido com sucesso!")
                    else:
                        print("Usuário não encontrado.")

            elif opcao == 2:
                print("Funcionário: ")
                print("1. Adicionar Funcionário")
                print("2. Editar Funcionário")
                print("3. Remover Funcionário")

                opc = int(input("Selecione uma opção: "))

                if opc == 1:
                    nome = input("Digite o nome: ")
                    cpf = input("Digite o CPF: ")
                    email = input("Digite o email: ")
                
                    
                    funcionario = Funcionario(None, nome, cpf, email)
                    db.salvar_funcionario(funcionario)
                    print("Funcionário adicionado com sucesso!")

                elif opc == 2:
                    cpf = input("Digite o CPF do funcionário que deseja editar: ")
                    funcionario = db.buscar_funcionario_por_cpf(cpf)

                    if funcionario:
                        novo_nome = input("Novo nome: ")
                        novo_email = input("Novo email: ")
                        db.editar_funcionario(cpf, novo_nome, novo_email)
                        print("Funcionário atualizado com sucesso!")
                    else:
                        print("Funcionário não encontrado.")

                elif opc == 3:
                    cpf = input("Digite o CPF do funcionário que deseja remover: ")
                    funcionario = db.buscar_funcionario_por_cpf(cpf)

                    if funcionario:
                        db.remover_funcionario(cpf)
                        print("Funcionário removido com sucesso!")
                    else:
                        print("Funcionário não encontrado.")

            elif opcao == 3:
                print("Livro: ")
                print("1. Adicionar Livro")
                print("2. Editar Livro")
                print("3. Remover Livro")

                opc = int(input("Selecione uma opção: "))

                if opc == 1:
                    nome = input("Digite o nome do livro: ")
                    autor = input("Digite o autor: ")
                    codigolivro = input("Código do livro: ")
                    
                    livro = Livro(None, nome, autor, codigolivro)
                    db.salvar_livro(livro)
                    print("Livro adicionado com sucesso!")

                elif opc == 2:
                    codigolivro = input("Digite o código do livro que deseja editar: ")
                    livro = db.buscar_livro_por_codigo(codigolivro)

                    if livro:
                        novo_nome = input("Novo nome: ")
                        novo_autor = input("Novo autor: ")
                        db.editar_livro(codigolivro, novo_nome, novo_autor)
                        print("Livro atualizado com sucesso!")
                    else:
                        print("Livro não encontrado.")

                elif opc == 3:
                    codigolivro = input("Digite o código do livro que deseja remover: ")
                    livro = db.buscar_livro_por_codigo(codigolivro)

                    if livro:
                        db.remover_livro(codigolivro)
                        print("Livro removido com sucesso!")
                    else:
                        print("Livro não encontrado.")

            elif opcao == 4:
                print("Empréstimo: ")
                print("1. Realizar Empréstimo")
                print("2. Devolver Livro")
                print("3. Listar Empréstimos")

                opc = int(input("Selecione uma opção: "))

                if opc == 1:
                    cpf_usuario = input("Digite o CPF do usuário: ")
                    usuario = db.buscar_usuario_por_cpf(cpf_usuario)

                    if not usuario:
                        print("Usuário não encontrado.")
                        continue
                    
                    codigo_livro = input("Digite o código do livro: ")
                    livro = db.buscar_livro_por_codigo(codigo_livro)

                    if not livro or not db.verificar_disponibilidade_livro(codigo_livro):
                        print("Livro indisponível para empréstimo.")
                        continue
                    
                    emprestimo = Emprestimo(usuario.id, livro.id)
                    db.realizar_emprestimo(emprestimo)
                    print("Empréstimo realizado com sucesso!")

                elif opc == 2:
                    codigo_livro = input("Digite o código do livro que deseja devolver: ")
                    if db.buscar_emprestimo_por_livro(codigo_livro):
                        db.devolver_livro(codigo_livro)
                        print("Livro devolvido com sucesso!")
                    else:
                        print("Nenhum empréstimo encontrado.")

            elif opcao == 5:
                print("Encerrando a sessão. ")
                break

        except ValueError:
            print("Entrada inválida. Digite uma opção válida.")

menu()