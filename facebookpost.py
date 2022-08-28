import pyautogui
import time

groups = ['170969849960651','146981669342301','226276471968988','1576911445756616','560874788379339','1807687706140793','501869043507199','313473142459579','501869043507199','162836750786834','Fahrelansyah2','118413288774389','654018261469082','689324964515891','112965685725187','466491364398927','657460731019774','2104128323157353','687009925091481','336526031431522','KomunitasPenggunaWifi.id']

time.sleep(5)

pyautogui.keyDown('command')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('command')
    

for i in range(len(groups)):
    link = 'https://www.facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    
    print('sedang mengakses, tunggu 15 detik')
    time.sleep(10)
    
    # Mencari Fitur Post
    pyautogui.hotkey('command','f')
    pyautogui.hotkey('command', 'a')
    pyautogui.typewrite('Tulis sesuatu...')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(3)
    
    # Masukan Content
    pyautogui.hotkey('command','v')    
    # Post
    pyautogui.hotkey('command','f')
    pyautogui.hotkey('command', 'a')
    pyautogui.typewrite('tambahkan ke postingan anda')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    
    pyautogui.keyDown('command')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('command')
    
    time.sleep(5)    