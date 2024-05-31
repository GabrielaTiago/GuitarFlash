import keyboard
import pyautogui

from modules.temporizadores import pausa_curta

POS_BTN_VERDE = (280, 580)
POS_BTN_VERMELHO = (352, 580)
POS_BTN_AMARELO = (422, 580)

COR_VERDE = (0, 152, 0)
COR_VERMELHO =  (255, 0, 0)
COR_AMARELO = (244, 244, 2)

def preciona_tecla_de_inicio():
    pyautogui.press('e')
    print('Para finalizar o jogo, pressione a tecla "Q" a qualquer momento\n')

def botao_verde():
    if verifica_botao(POS_BTN_VERDE, COR_VERDE):
        pyautogui.press('a')
        pausa_curta()

def botao_vermelho():
    if verifica_botao(POS_BTN_VERMELHO, COR_VERMELHO):
        pyautogui.press('s')
        pausa_curta()

def botao_amarelo():
    if verifica_botao(POS_BTN_AMARELO, COR_AMARELO):
        pyautogui.press('j')
        pausa_curta()

def verifica_botao(posicao: tuple, cor: tuple):
    return pyautogui.pixelMatchesColor(posicao[0], posicao[1], (cor[0], cor[1], cor[2]), tolerance=10)

def joga():
    print('Jogo iniciado!')
    while keyboard.is_pressed('Q') == False:
        botao_verde()
        botao_vermelho()
        botao_amarelo()
    print('Jogo finalizado!')
