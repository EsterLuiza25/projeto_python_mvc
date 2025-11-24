import psycopg2

class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                database="biblioteca",   
                user="postgres",
                password="postgres",      
                port="5432"
            )
            self.cursor = self.connection.cursor()
            self._criar_tabelas()
            print("Conectado ao PostgreSQL com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar com o banco: {e}")
            exit(1)
    
    def _criar_tabelas(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS autor (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    nacionalidade VARCHAR(50)
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS livro (
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(200) NOT NULL,
                    ano_publicacao INTEGER,
                    autor_id INTEGER REFERENCES autor(id)
                )
            """)
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")
    
    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor
        except Exception as e:
            self.connection.rollback()
            raise e
    
    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()