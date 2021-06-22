import pyautogui
import pyperclip
import time
import pandas


doc = ['107246', '107259', '107370', '107282']

time.sleep(3)
print(pyautogui.position())

def buscarNota(doc):
    diamax = '31'
    dia = '01'
    mes = '07'
    ano = '2016'
    cod_empresa = '13830'
    #posição da janela na area de trabalho
    pyautogui.click(x=278, y=765)
    #------------------------------------
    pyautogui.moveTo(x=325, y=43, duration=1)
    pyautogui.click(x=325, y=43)

    pyautogui.click(x=22, y=83)
    pyautogui.click(x=22, y=83)
    pyautogui.click(x=90, y=406)

    time.sleep(3)
    pyautogui.write(ano)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.write(mes)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.write(dia)
    pyautogui.press('enter')


    pyautogui.click(x=222, y=406)
    time.sleep(2)
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.write(diamax)
    pyautogui.press('right')
    pyautogui.write('08')
    pyautogui.press('right')
    pyautogui.write(ano)
    time.sleep(1)


    pyautogui.click(x=136, y=628)
    pyautogui.write(doc)

    pyautogui.click(x=166, y=359)
    pyautogui.write(cod_empresa)
    pyautogui.press('f8')
    time.sleep(3)
    pyautogui.click(x=361, y=355)
    pyautogui.press('f10')
    time.sleep(5)
    pyautogui.press('f8')
    pyautogui.click(x=369, y=320, clicks=2)
    time.sleep(30)

    pyautogui.click(x=281, y=241)
    pyautogui.click(x=344, y=325, clicks=2)
    pyautogui.hotkey('ctrl', 'c')

#fechamento 
def exit():
    pyautogui.click(x=405, y=204)
    pyautogui.click(x=280, y=198)
    
def navegadorDownload():

    pyautogui.click(x=313, y=751)
    pyautogui.click(x=469, y=280)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(x=725, y=331)



def main(lista):
    for c in range(len(lista)):
        buscarNota(lista[c])
        exit()
        navegadorDownload()




main(doc)