from Mycrud import My_crud

mycrud = My_crud('moleza.sqlite')
mycrud. criar_tabela()

while True:
    print('''
    Escolha uma opçâo:
    1 - Incluir dados.
    2 - Ler apenas 1 da tabela.
    3 - Ler toda a tabela.
    4 - Alterar dados.
    5 - Deletar 1 id.
    6 - Deletar tudo.
    7 - sair.
    ''')

# inserir nome e cpf.

    valor = input('==> ')
    if valor == "1":
        nome = str(input('Entre com seu nome: '))
        cpf = str(input('Entre com seu CPF: '))
        dados = {
        'nome': nome,
        'cpf': cpf
        }
        mycrud.inserir(nome, cpf)

# mostra apenas onde o id foi pedido.
    
    elif valor == '2':
        id = int(input('Entre com sua ID: '))
        resultado = mycrud.lerDB(id)
        print(resultado)

# mostra toda a tabela.
    elif valor == '3':
        id = int(input('Digite 3 para mostrar toda a tabela: '))
        resultado = mycrud.lertabelaDB()
        print(resultado)

# alterar tabela.   

    elif valor == '4':
        id = int(input('Entre com a ID: '))
        nome = str(input('Entre com o novo nome: '))
        cpf = str(input('Entre com o novo CPF: '))
        dados = {
            'nome': nome,
            'cpf': cpf
        }
        mycrud.alterarDB(nome, cpf, id)

# deletar um valor do DB a partir do id.

    elif valor == '5':
        id = input('Entre com a sua ID: ')
        mycrud.deletar(id)

# deleta todos os valores do DB.

    elif valor == '6':
        id = input('Digite 0 para apagar todos os dados: ')
        mycrud.deletar_tudo()
    
    else:
        break
print('Até mais tarde. ')