from models.autor_model import AutorModel
from models.livro_model import LivroModel

class AutorController:
    def __init__(self):
        self.model = AutorModel()
        self.livro_model = LivroModel()
    
    def cadastrar_autor(self, nome, nacionalidade):
        """Cadastra um novo autor"""
        if not nome:
            return False, "Nome do autor é obrigatório"
        
        try:
            autor_id = self.model.criar(nome, nacionalidade)
            return True, f"Autor cadastrado com sucesso! ID: {autor_id}"
        except Exception as e:
            return False, f"Erro ao cadastrar autor: {e}"
    
    def listar_autores(self):
        """Lista todos os autores"""
        try:
            autores = self.model.listar_todos()
            return True, autores
        except Exception as e:
            return False, f"Erro ao listar autores: {e}"
    
    def buscar_autor_por_id(self, autor_id):
        """Busca um autor específico pelo ID"""
        try:
            autor = self.model.buscar_por_id(autor_id)
            return True, autor
        except Exception as e:
            return False, f"Erro ao buscar autor: {e}"
    
    def atualizar_autor(self, autor_id, nome, nacionalidade):
        """Atualiza os dados de um autor"""
        if not self.model.existe(autor_id):
            return False, "Autor não encontrado"
        
        if not nome:
            return False, "Nome do autor é obrigatório"
        
        try:
            self.model.atualizar(autor_id, nome, nacionalidade)
            return True, "Autor atualizado com sucesso!"
        except Exception as e:
            return False, f"Erro ao atualizar autor: {e}"
    
    def excluir_autor(self, autor_id):
        """Exclui um autor e seus livros associados"""
        if not self.model.existe(autor_id):
            return False, "Autor não encontrado"
        
        try:
            # Verificar se o autor tem livros
            livros_do_autor = self.livro_model.buscar_livros_por_autor(autor_id)
            
            if livros_do_autor:
                # Se tem livros, mostrar e perguntar
                print(f"\nATENÇÃO: Este autor tem {len(livros_do_autor)} livro(s) associado(s):")
                for livro in livros_do_autor:
                    print(f" {livro[1]} (ID: {livro[0]})")
                
                confirmacao = input("\nDeseja excluir o autor E TODOS os seus livros? (s/N): ").strip().lower()
                if confirmacao != 's':
                    return False, "Operação cancelada."
                
                # Excluir todos os livros do autor
                for livro in livros_do_autor:
                    self.livro_model.excluir(livro[0])
                print("Livros do autor excluídos com sucesso!")
            
            # Agora excluir o autor
            self.model.excluir(autor_id)
            return True, "Autor excluído com sucesso!"
            
        except Exception as e:
            return False, f"Erro ao excluir autor: {e}"
