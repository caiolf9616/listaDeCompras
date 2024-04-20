from revisao import*
import time

print('        Bem vindo a sua Lista de Compras')
print()


while True:
    opcao = int(input(
        '''
           1--> Adcionar Produtos
           2--> Ver Produtos na Lista
           3--> Atualizar Produtos da Lista
           4--> Excluir Produtos da Lista
           5--> Sair Da Lista
           :  
           '''
    ))
    
    if opcao == 1:
        add_produtos()
    
    if opcao == 2:
        ver_produtos()
    
    if opcao == 3:
        atualizar_produtos()
        
    if opcao == 4:
        excluir_produto()
    
    if opcao == 5:
        time.sleep(1)
        print("Fim")
        break                
        
    
      
