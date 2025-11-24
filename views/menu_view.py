from controllers.autor_controller import AutorController
from controllers.livro_controller import LivroController

class MenuView:
    def __init__(self):
        self.autor_controller = AutorController()
        self.livro_controller = LivroController()
    
    def mostrar_menu_principal(self):
        while True:
            print("\n" + "="*40)
            print("\nSISTEMA BIBLIOTECA")
            print("="*40)
            print("1. Gerenciar Autores")
            print("2. Gerenciar Livros")
            print("3. Sair")
            print("="*40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.menu_autores()
            elif opcao == "2":
                self.menu_livros()
            elif opcao == "3":
                print("Obrigado por usar o sistema! Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    def menu_autores(self):
        while True:
            print("\n" + "="*30)
            print("\nGERENCIAR AUTORES")
            print("="*30)
            print("1. Cadastrar Autor")
            print("2. Listar Autores")
            print("3. Atualizar Autor")
            print("4. Excluir Autor")
            print("5. Voltar ao Menu Principal")
            print("="*30)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_autor()
            elif opcao == "2":
                self.listar_autores()
            elif opcao == "3":
                self.atualizar_autor()
            elif opcao == "4":
                self.excluir_autor()
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")
    
    def menu_livros(self):
        while True:
            print("\n" + "="*30)
            print("\nGERENCIAR LIVROS")
            print("="*30)
            print("1. Cadastrar Livro")
            print("2. Listar Livros")
            print("3. Atualizar Livro")
            print("4. Excluir Livro")
            print("5. Voltar ao Menu Principal")
            print("="*30)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_livro()
            elif opcao == "2":
                self.listar_livros()
            elif opcao == "3":
                self.atualizar_livro()
            elif opcao == "4":
                self.excluir_livro()
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")
    
    def cadastrar_autor(self):
        print("\n--- CADASTRAR AUTOR ---")
        nome = input("Nome do autor: ").strip()
        nacionalidade = input("Nacionalidade (opcional): ").strip() or None
        
        sucesso, mensagem = self.autor_controller.cadastrar_autor(nome, nacionalidade)
        print(mensagem)
    
    def listar_autores(self):
        print("\n--- LISTA DE AUTORES ---")
        sucesso, resultado = self.autor_controller.listar_autores()
        
        if not sucesso:
            print(resultado)
            return
        
        if not resultado:
            print("Nenhum autor cadastrado.")
            return
        
        print(f"{'ID':<5} {'NOME':<25} {'NACIONALIDADE':<15}")
        print("-" * 50)
        for autor in resultado:
            print(f"{autor[0]:<5} {autor[1]:<25} {autor[2] or 'N/I':<15}")
    
    def atualizar_autor(self):
        print("\n--- ATUALIZAR AUTOR ---")
        try:
            autor_id = int(input("ID do autor a ser atualizado: "))
        except ValueError:
            print("ID deve ser um número inteiro.")
            return
        
        nome = input("Novo nome: ").strip()
        nacionalidade = input("Nova nacionalidade (opcional): ").strip() or None
        
        if not nome:
            print("Nome é obrigatório.")
            return
        
        sucesso, mensagem = self.autor_controller.atualizar_autor(autor_id, nome, nacionalidade)
        print(mensagem)
    
    def excluir_autor(self):
        print("\n--- EXCLUIR AUTOR ---")
        try:
            autor_id = int(input("ID do autor a ser excluído: "))
        except ValueError:
            print("ID deve ser um número inteiro.")
            return
        
        confirmacao = input("Tem certeza que deseja excluir este autor? (s/N): ").strip().lower()
        if confirmacao == 's':
            sucesso, mensagem = self.autor_controller.excluir_autor(autor_id)
            print(mensagem)
        else:
            print("Operação cancelada.")
    
    def cadastrar_livro(self):
        print("\n--- CADASTRAR LIVRO ---")
        
        sucesso, autores = self.livro_controller.listar_autores()
        if not sucesso or not autores:
            print("Nenhum autor cadastrado. Cadastre um autor primeiro.")
            return
        
        print("Autores disponíveis:")
        for autor in autores:
            print(f"  ID {autor[0]}: {autor[1]}")
        
        titulo = input("Título do livro: ").strip()
        
        try:
            ano_input = input("Ano de publicação (opcional): ").strip()
            ano_publicacao = int(ano_input) if ano_input else None
            autor_id = int(input("ID do autor: "))
        except ValueError:
            print("Ano deve ser um número e ID deve ser inteiro.")
            return
        
        sucesso, mensagem = self.livro_controller.cadastrar_livro(titulo, ano_publicacao, autor_id)
        print(mensagem)
    
    def listar_livros(self):
        print("\n--- LISTA DE LIVROS ---")
        sucesso, resultado = self.livro_controller.listar_livros()
        
        if not sucesso:
            print(resultado)
            return
        
        if not resultado:
            print("Nenhum livro cadastrado.")
            return
        
        print(f"{'ID':<5} {'TÍTULO':<35} {'ANO':<8} {'AUTOR':<20}")
        print("-" * 75)
        for livro in resultado:
            ano_str = str(livro[2]) if livro[2] else "N/I"
            print(f"{livro[0]:<5} {livro[1]:<35} {ano_str:<8} {livro[3] or 'N/I':<20}")
    
    def atualizar_livro(self):
        print("\n--- ATUALIZAR LIVRO ---")
        try:
            livro_id = int(input("ID do livro a ser atualizado: "))
        except ValueError:
            print("ID deve ser um número inteiro.")
            return
        
        sucesso, autores = self.livro_controller.listar_autores()
        if sucesso and autores:
            print("Autores disponíveis:")
            for autor in autores:
                print(f"  ID {autor[0]}: {autor[1]}")
        
        titulo = input("Novo título: ").strip()
        
        try:
            ano_input = input("Novo ano (opcional): ").strip()
            ano_publicacao = int(ano_input) if ano_input else None
            autor_id = int(input("Novo ID do autor: "))
        except ValueError:
            print("Ano e ID do autor devem ser números.")
            return
        
        sucesso, mensagem = self.livro_controller.atualizar_livro(livro_id, titulo, ano_publicacao, autor_id)
        print(mensagem)
    
    def excluir_livro(self):
        print("\n--- EXCLUIR LIVRO ---")
        try:
            livro_id = int(input("ID do livro a ser excluído: "))
        except ValueError:
            print("ID deve ser um número inteiro.")
            return
        
        confirmacao = input("Tem certeza que deseja excluir este livro? (s/N): ").strip().lower()
        if confirmacao == 's':
            sucesso, mensagem = self.livro_controller.excluir_livro(livro_id)
            print(mensagem)
        else:
            print("Operação cancelada.")