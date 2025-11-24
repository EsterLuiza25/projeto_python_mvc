from models.database import Database

class AutorModel:
    def __init__(self):
        self.db = Database()
    
    def criar(self, nome, nacionalidade):
        query = "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s) RETURNING id"
        result = self.db.execute(query, (nome, nacionalidade))
        return result.fetchone()[0]
    
    def listar_todos(self):
        query = "SELECT id, nome, nacionalidade FROM autor ORDER BY id"
        return self.db.fetch_all(query)
    
    def buscar_por_id(self, autor_id):
        query = "SELECT id, nome, nacionalidade FROM autor WHERE id = %s"
        return self.db.fetch_one(query, (autor_id,))
    
    def atualizar(self, autor_id, nome, nacionalidade):
        query = "UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s"
        self.db.execute(query, (nome, nacionalidade, autor_id))
    
    def excluir(self, autor_id):
        query = "DELETE FROM autor WHERE id = %s"
        self.db.execute(query, (autor_id,))
    
    def existe(self, autor_id):
        query = "SELECT 1 FROM autor WHERE id = %s"
        return self.db.fetch_one(query, (autor_id,)) is not None