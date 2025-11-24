from models.livro_model import LivroModel
from models.autor_model import AutorModel

class LivroController:
    def __init__(self):
        self.livro_model = LivroModel()
        self.autor_model = AutorModel()
    
    def cadastrar_livro(self, titulo, ano_publicacao, autor_id):
        if not titulo:
            return False, "Título do livro é obrigatório"
        
        if not self.autor_model.existe(autor_id):
            return False, "Autor não encontrado"
        
        try:
            livro_id = self.livro_model.criar(titulo, ano_publicacao, autor_id)
            return True, f"Livro cadastrado com sucesso! ID: {livro_id}"
        except Exception as e:
            return False, f"Erro ao cadastrar livro: {e}"
    
    def listar_livros(self):
        try:
            livros = self.livro_model.listar_todos()
            return True, livros
        except Exception as e:
            return False, f"Erro ao listar livros: {e}"
    
    def atualizar_livro(self, livro_id, titulo, ano_publicacao, autor_id):
        livro = self.livro_model.buscar_por_id(livro_id)
        if not livro:
            return False, "Livro não encontrado"
        
        if not titulo:
            return False, "Título do livro é obrigatório"
        
        if not self.autor_model.existe(autor_id):
            return False, "Autor não encontrado"
        
        try:
            self.livro_model.atualizar(livro_id, titulo, ano_publicacao, autor_id)
            return True, "Livro atualizado com sucesso!"
        except Exception as e:
            return False, f"Erro ao atualizar livro: {e}"
    
    def excluir_livro(self, livro_id):
        livro = self.livro_model.buscar_por_id(livro_id)
        if not livro:
            return False, "Livro não encontrado"
        
        try:
            self.livro_model.excluir(livro_id)
            return True, "Livro excluído com sucesso!"
        except Exception as e:
            return False, f"Erro ao excluir livro: {e}"
    
    def listar_autores(self):
        try:
            autores = self.autor_model.listar_todos()
            return True, autores
        except Exception as e:
            return False, f"Erro ao listar autores: {e}"