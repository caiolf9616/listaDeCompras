import time
lista_decompas = {'Produtos':[]}

def add_produtos():
    nome_produto = input('Nome do produto:')
    preco_produto = float(input('Preço do produto:'))
    quantidade_produto = int(input('Quantidade do produto:')) 
    preco_total = (preco_produto * quantidade_produto)
    
    produto = {'nome': nome_produto, 'preco':preco_produto, 'quantidade': quantidade_produto, 'Valor Total':preco_total}
    lista_decompas['Produtos'].append(produto)
    time.sleep(2)
    print('Adicionado Com Sucesso!')
    
def calcular_valor_total(produto):
    return produto['preco'] * produto['quantidade']    
    
    
def ver_produtos():
    total_produtos = 0
    
    for produto in lista_decompas['Produtos']:
        produto['Valor total'] = calcular_valor_total(produto)
        time.sleep(2)
        print(f"Produto: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}, Valor Total: {produto['Valor Total']}")
        
        total_produtos += produto['Valor total']
        
    
    print(f'Valor total dos produtos:R$ {round(total_produtos, 2 )}')    
        
        
            
def atualizar_produtos():
    nome_novo_produto = input('Qual Produto deseja atualizar?:')
    
    for produto in lista_decompas['Produtos']:
        if produto['nome'] == nome_novo_produto:
            nome_novo = input('Novo Nome do Produto:')
            nova_quantidade = int(input('Nova quantidade:'))
            novo_valor = float(input('Novo valor:'))
            
            produto['nome']= nome_novo
            produto['quantidade'] = nova_quantidade
            produto['preco'] = novo_valor
            produto['Valor Total'] = nova_quantidade * novo_valor
            
            time.sleep(2)
            print('Atualizado com Sucesso!')
            
            
def excluir_produto():
    if not lista_decompas['Produtos']:
        time.sleep(2)
        print('A lista está vazia!')
        return
    nome_produto_excluir = input('Qual o produto que você que excluir?:')
    
    for produto in lista_decompas['Produtos']:
        if produto['nome'] == nome_produto_excluir:
           lista_decompas['Produtos'].remove(produto) 
           time.sleep(2)
           print('Produto excluido com sucesso!')
           return
       
    print('Produto não emcontrado na lista!') 

        
       