import random
import pyautogui
import webbrowser

SITE = 'https://guitarflash.com/?lg=pt'
MUSICAS = ['Somewhere I Belong', 'Do I Wanna Know', 'Nothing Else Matters', 'Come As You Are']

def navega_para_site():
    webbrowser.open_new(SITE)

def clica_no_botao_jogar():
    pyautogui.click(249, 346, duration=0.8)

def define_musica_aleatoria():
    return random.choice(MUSICAS)

def seleciona_musica():
    pyautogui.click(579, 496, duration=0.8)
    musica = define_musica_aleatoria()
    print(f'Música selecionada: {musica}')
    pyautogui.write(musica, interval=0.25)
    pyautogui.click(322, 526, duration=1)

def desce_tela():
    pyautogui.scroll(-300)
