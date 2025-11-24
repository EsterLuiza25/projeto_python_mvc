from models.database import Database

class LivroModel:
    def __init__(self):
        self.db = Database() 
    
    def criar(self, titulo, ano_publicacao, autor_id):
        query = "INSERT INTO livro (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s) RETURNING id"
        result = self.db.execute(query, (titulo, ano_publicacao, autor_id))
        return result.fetchone()[0]
    
    def listar_todos(self):
        query = """
            SELECT l.id, l.titulo, l.ano_publicacao, a.nome as autor_nome
            FROM livro l
            LEFT JOIN autor a ON l.autor_id = a.id
            ORDER BY l.id
        """
        return self.db.fetch_all(query)
    
    def buscar_livros_por_autor(self, autor_id):
        query = "SELECT id, titulo FROM livro WHERE autor_id = %s"
        return self.db.fetch_all(query, (autor_id,))
    
    def buscar_por_id(self, livro_id):
        query = "SELECT id, titulo, ano_publicacao, autor_id FROM livro WHERE id = %s"
        return self.db.fetch_one(query, (livro_id,))
    
    def atualizar(self, livro_id, titulo, ano_publicacao, autor_id):
        query = "UPDATE livro SET titulo = %s, ano_publicacao = %s, autor_id = %s WHERE id = %s"
        self.db.execute(query, (titulo, ano_publicacao, autor_id, livro_id))
    
    def excluir(self, livro_id):
        query = "DELETE FROM livro WHERE id = %s"
        self.db.execute(query, (livro_id,))