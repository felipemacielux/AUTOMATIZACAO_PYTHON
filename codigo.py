    # Passo a passo do projeto
    # 1. Entrar no sistema da empresa
            #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui # biblioteca para automação de mouse e teclado
import time

# São executados simultaneamente, precisa colocar a pausa entre eles
pyautogui.PAUSE = 0.3 # a cada comando dele deve dar uma pausa de 5 segundos / Ele soma o time.sleep()

'''Principais comandos do pyautogui

pyautogui.click # clicar em algum lugar da tela
pyautogui.write # escrever um texto
pyautogui.press # apertar uma tecla
pyautogui.hotkey # apertar uma combinação de teclas ("ctrl", "alt", "shift")

'''
# Continuando o primeiro passo o navegador deve ser aberto
pyautogui.press('win') # apertar a tecla win (é tratado como string porque dentro do pyautogui refere-se a um tecla especifica do teclado)
pyautogui.write('chrome') # escrever o nome do navegador que deseja abrir, que no caso aqui foi o chrome
pyautogui.press('enter') # apertar a tecla enter para abrir o navegador


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' # o valor que pode ser usado em vários momentos do código, porque se for alterado em algum momento pode ser alterado na hora de executar o projeto
pyautogui.write(link) # escrever o link do site que deseja acessar assim que o chrome abrir / foi pego a variavel do link acima, isso porque o link pode mudar, você poderá usar mais variaveis com outros links ou a mesma só chamando a variavel

pyautogui.press('enter') # apertar a tecla enter para abrir o link do site

#Aqui será necessário dar uma pausa de uns 3 segundos, utilizamos a biblioteca time para isso
time.sleep(3) # diferente do .PAUSE é que o time.sleep vai aguardar em um momento especifico do código

    # 2. Fazer login
pyautogui.click(x=828, y=-435) #precisa ser colocado as coordenadas para que ele consiga identificar a area, e o pyautogui vai pegar essas coordenadas e clicar em cima do botão do login / vai pegar as coordenadas através do código auxiliar.py
pyautogui.write('felipemacielfolhaverde@gmail.com') # escrever o email
pyautogui.press('tab') # apertar a tecla tab para pular para a proxima caixa de texto
pyautogui.write('123456') # escrever a senha
pyautogui.press('enter') # apertar a tecla enter para logar / ou pode ser feito com o processo do pyautogui.click

time.sleep(3) # Esperar o tempo para que o tempo consiga ser carregado corretamente

    # 3. Importar a base de dados # baixar a versão completa do pandas / pip install pandas numpy openpyxl
import pandas
# consegue pegar todas as informações da base de dados e armazenar dentro de uma variavel
tabela = pandas.read_csv("produtos.csv")

   
    # 4. Cadastrar um produto
#para cada linha dentro da tabela (linha = index)
for linha in tabela.index:

# Deve clicar no primeiro campo
    
    pyautogui.click(x=879, y=-582) # vai alterar depedendo de onde está o campo e também da resolução da tela

    # codigo do produto
    # Vai ser no critério de linha e coluna da tabela identificado pelas listas, não precisando ser criado a coluna por fora
    pyautogui.write(tabela.loc[linha, "codigo"])# tabela.loc quer dizer que está usando toda ela para selecionar linhas e colunas com base em seus rótulos.
    pyautogui.press('tab')

    # marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press('tab')

    #tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press('tab')

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #colocado o str para situações em que será preciso números porque o pyautogui não consegue interpretar como número e sim como texto
    pyautogui.press('tab')

    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    #OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #senão tiver vazia escreve a obs
        pyautogui.write(obs)# uma informação que está vazia na tabela, tem que abrir condicionais
    pyautogui.press('tab')

    #para clicar no botão enviar
    pyautogui.press('enter')
   

    # Assim que tiver cadastrado um novo produto deve retornar para o primeiro campo e cadastrar os demais itens
    pyautogui.scroll(5000)

    # 5. Repetir o processo de cadastro até terminar a base de dados