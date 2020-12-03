import random #Módulo usado para escolher valores
import PySimpleGUI as sg
import os
 
 
class PassGen:
   def __init__(self):
       # Definindo um tema
       sg.theme('reddit')
       #Criando um Layout
       layout = [
           [sg.Text('Site', size=(35, 1)),
            sg.Input(key='site', size=(40, 1))],
           [sg.Text('Usuário', size=(35, 1)),
            sg.Input(key='usuario', size=(40, 1))],
           [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
               range(30)), key='total_chars', default_value=1, size=(3, 1))],
           [sg.Output(size=(64, 5))],
           [sg.Button('Gerar Senha')]
       ]
       # criar uma janela e associa-la ao layout
       self.janela = sg.Window('Gerador de senhas', layout) #Nome que aparecerá na parte suprior da janela
 
   def Iniciar(self):
       while True:
           evento, valores = self.janela.read() #apresentar a janela para o usuário
           if evento == sg.WINDOW_CLOSED:
               break
           if evento == 'Gerar Senha':
               nova_senha = self.gerar_senha(valores)
               print(nova_senha)
               self.salvar_senha(nova_senha, valores)
 
   def gerar_senha(self, valores):
       char_list = '!@#$%/=¨&*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890' #Valores que podem ser escolhidos de forma aleatória
       chars = random.choices(char_list, k=int(valores['total_chars']))
       new_pass = ''.join(chars)
       print(' Essa será a sua senha: ',)
       return new_pass
      
   def salvar_senha(self, nova_senha, valores):
       with open('senhas.txt', 'a', newline='') as arquivo:
           arquivo.write(
               f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}")
 
      
 
 
gen = PassGen()
gen.Iniciar()

