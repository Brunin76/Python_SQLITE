class My_crud:
   
   def __init__(self, dados):
      import sqlite3
      self.conexao = sqlite3.connect(dados)
      self.cursor = self.conexao.cursor()

# Criação da tabela
   
   def criar_tabela(self):
      sql = """
         CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome text not null,
            CPF INTEGER
         );   
      """
      self.cursor.execute(sql)
      print('Tabela criada')

# inserir dados no banco.

   def inserir(self,nome, cpf):
      sql = """
         INSERT INTO pessoas (nome, cpf)
         VALUES (?, ?)      
      """
      
      cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
      if len(cpf) <14 or len(cpf) >14:
         return cpf, print(f'CPF inválido, tente novamente com 11 dígitos. ')
      else:
         pass
      self.cursor.execute(sql, [nome, cpf])
      self.conexao.commit()
      print('salvo com sucesso! ')

# ler apenas onde a id foi pedida.   
   
   def lerDB(self,id):
      sql = """
         SELECT * FROM pessoas WHERE id =?;
      """
      if id != id:
         return id, print('Essa id não existe, tente outra. ')
      self.cursor.execute(sql,[id,])
      for linha in self.cursor.fetchall():
         print(linha)

# ler toda a tabela.
   
   def lertabelaDB(self):
      sql = """
         SELECT * FROM pessoas;
      """
      self.cursor.execute(sql)
      for linha in self.cursor.fetchall():
         print(linha)


# edita o banco de dados.
   
   def alterarDB(self, nome, cpf, id):
      sql = """
         UPDATE pessoas
         SET nome = ? , cpf = ?
         WHERE id = ?;
      """
      
      cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
      if len(cpf) <14 or len(cpf) >14:
         return cpf, print(f'CPF inválido, digitos, tente novamente com 11 dígitos. ')
      else:
         pass
      self.cursor.execute(sql, [nome, cpf, id])
      self.conexao.commit()
      print('Alterado com sucesso! ')
   
# deletar dados só onde a id foi colocada.

   def deletar(self, id):
      sql = """
         DELETE FROM pessoas
         WHERE id = ?;
      """
      
      self.conexao.execute(sql, [id,])
      self.conexao.commit()
      print('Deletado com sucesso! ')

# deleta todos do DB:
   
   def deletar_tudo(self):
      sql = """
         DELETE FROM PESSOAS;
      """
      self.conexao.execute(sql)
      self.conexao.commit()
      print('Todos os dados foram deletados! ')

   def fechar(self):
      self.cursor.close()
      self.conexao.close()