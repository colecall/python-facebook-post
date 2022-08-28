import pyautogui
import time

groups = ['jualalatmusikbarubekasdepok','otindonesia','onshop','bisnissejati','onlineshopindonesia','bjbsa','270120406830347','303608223460800','1521811324791492','1510354615910702','104885313182476','937239399696310','917921991633241','1998608737030457','1708598352552088','1052957408061989']
time.sleep(5)

pyautogui.keyDown('command')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('command')
    

for i in range(len(groups)):
    link = 'https://www.facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('/buy_sell_discussion')
    pyautogui.typewrite('\n')
    
    print('sedang mengakses, tunggu 15 detik')
    time.sleep(10)
    
    # Mencari Fitur Post
    pyautogui.hotkey('command','f')
    pyautogui.hotkey('command', 'a')
    pyautogui.typewrite('foto/video')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(3)
    
    # Ambil File
    pyautogui.hotkey('command', 'a')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(5)
    # Masukan Content
    pyautogui.typewrite('Gasken Murah!')
    
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