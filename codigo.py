    # Passo a passo do projeto
    # 1. Entrar no sistema da empresa
            #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui # biblioteca para automação de mouse e teclado
import time

# São executados simultaneamente, precisa colocar a pausa entre eles
pyautogui.PAUSE = 0.3 # a cada comando dele deve dar uma pausa de 5 segundos

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
pyautogui.click(x=497, y=268) #precisa ser colocado as coordenadas para que ele consiga identificar a area, e o pyautogui vai pegar essas coordenadas e clicar em cima do botão do login

    # 3. Importar a base de dados
    # 4. Cadastrar um produto
    # 5. Repetir o processo de cadastro até terminar a base de dados

