import pyautogui
import time

groups = [
    '+1 (423) 219-2866', '+62 812-1099-0459', '+62 812-1320-9509', '+62 812-1699-2527', '+62 812-1713-9256', '+62 812-2350-7266', '+62 812-2514-7629', 
    '+62 812-2717-6119', '+62 812-3335-5664', '+62 812-3997-0666', '+62 812-4260-8078', '+62 812-4302-3852', '+62 812-8127-4140', '+62 812-8583-7542', 
    '+62 812-8615-4531', '+62 812-8618-1784', '+62 812-8726-4653', '+62 812-8736-8408', '+62 812-8993-5242', '+62 812-9005-3660', '+62 812-9772-7008', 
    '+62 812-9837-4424', '+62 812-9934-1891', '+62 813-1040-4291', '+62 813-1144-2155', '+62 813-1614-2833', '+62 813-2426-1130', '+62 813-3006-7834', 
    '+62 813-3036-5661', '+62 813-3314-4137', '+62 813-3691-3641', '+62 813-4385-9463', '+62 813-4659-2436', '+62 813-5718-9585', '+62 813-6320-5735', 
    '+62 813-6519-0751', '+62 813-7326-9730', '+62 813-7982-6684', '+62 813-8447-8029', '+62 813-8948-3505', '+62 814-1419-3985', '+62 815-1461-1055', 
    '+62 815-1555-5820', '+62 815-2825-2655', '+62 816-3278-1106', '+62 819-0323-2209', '+62 819-1179-4623', '+62 819-9098-8804', '+62 821-1329-3786', 
    '+62 821-1700-5624', '+62 821-2424-6148', '+62 821-3638-0885', '+62 821-3815-7158', '+62 821-6658-3109', '+62 821-6979-3040', '+62 821-9881-8887', 
    '+62 822-1152-9571', '+62 822-1307-7895', '+62 822-1432-1618', '+62 822-1787-7294', '+62 822-2693-6373', '+62 822-2777-7396', '+62 822-4297-5549', 
    '+62 822-4487-9410', '+62 822-4617-4831', '+62 822-4803-0234', '+62 822-5295-3670', '+62 822-5356-7744', '+62 822-6026-1705', '+62 822-6187-1215', 
    '+62 822-6849-9740', '+62 822-7657-5945', '+62 822-8220-7940', '+62 822-8252-6154', '+62 822-8258-5741', '+62 822-9155-1636', '+62 822-9322-7635', 
    '+62 822-9697-4919', '+62 822-9807-5595', '+62 822-9840-4197', '+62 823-2023-2281', '+62 823-2923-2015', '+62 823-3895-2429', '+62 823-3944-9735', 
    '+62 823-8296-7945', '+62 823-8585-6692', '+62 823-9126-9089', '+62 831-2405-1446', '+62 831-3148-6695', '+62 831-7044-9390', '+62 831-8477-6835', 
    '+62 831-9935-2329', '+62 838-1254-0166', '+62 838-2915-4171', '+62 838-3234-4895', '+62 838-3660-0900', '+62 838-5312-1830', '+62 838-7845-8041', 
    '+62 838-9431-2008', '+62 838-9534-8458', '+62 851-5502-7794', '+62 851-5514-9420', '+62 851-5515-5814', '+62 851-5515-8382', '+62 851-5524-6224', 
    '+62 851-5545-6647', '+62 851-5546-0103', '+62 851-5605-2421', '+62 851-5614-9251', '+62 851-5621-9745', '+62 851-5623-8833', '+62 851-5634-9142', 
    '+62 851-5697-6341', '+62 851-5761-0544', '+62 851-5772-5422', '+62 851-5834-4258', '+62 851-5882-4759', '+62 851-6128-4056', '+62 851-6164-2243', 
    '+62 851-7101-0223', '+62 852-1854-3751', '+62 852-2964-1286', '+62 852-3317-5707', '+62 852-3569-5049', '+62 852-4193-6109', '+62 852-5881-1998', 
    '+62 852-6762-2765', '+62 852-9869-1292', '+62 852-9944-0959', '+62 853-2016-9186', '+62 853-2154-3374', '+62 853-2678-1779', '+62 853-3003-2334', 
    '+62 853-4262-2831', '+62 853-4691-8317', '+62 853-5876-3564', '+62 853-6258-1787', '+62 856-0091-1628', '+62 856-2107-315', '+62 856-2446-2650', 
    '+62 856-3090-411', '+62 856-4207-9252', '+62 856-4302-7156', '+62 856-4640-8825', '+62 856-7979-046', '+62 856-9709-8208', '+62 857-0378-4016', 
    '+62 857-0400-3999', '+62 857-0696-1423', '+62 857-0814-5366', '+62 857-1027-5685', '+62 857-2466-0941', '+62 857-3805-0589', '+62 857-4010-8699', 
    '+62 857-5909-0498', '+62 857-7031-0875', '+62 857-7092-4422', '+62 857-7223-9015', '+62 857-7966-6574', '+62 857-8064-0905', '+62 857-9372-6252', 
    '+62 857-9439-7743', '+62 858-4396-8654', '+62 858-5923-1120', '+62 858-5924-9310', '+62 858-6631-3827', '+62 858-7125-9300', '+62 858-8577-0540', 
    '+62 858-9184-4317', '+62 858-9246-1249', '+62 858-9290-7311', '+62 858-9349-8804', '+62 858-9443-5830', '+62 877-7108-9000', '+62 877-8211-6900', 
    '+62 878-1638-5269', '+62 878-2175-5682', '+62 878-5068-3841', '+62 878-5540-0863', '+62 878-7000-7248', '+62 878-7356-9120', '+62 878-8870-7531', 
    '+62 878-9471-7568', '+62 881-1173-460', '+62 882-1030-6405', '+62 882-3288-9398', '+62 889-7302-3547', '+62 895-0111-0550', '+62 895-1600-5499', 
    '+62 895-1736-6267', '+62 895-2435-0491', '+62 895-2487-3468', '+62 895-2488-2131', '+62 895-2794-6040', '+62 895-2907-4743', '+62 895-2954-5531', 
    '+62 895-2991-0216', '+62 895-3304-00346', '+62 895-3321-11594', '+62 895-3323-79264', '+62 895-3403-65932', '+62 895-3472-82572', '+62 895-3491-33844', 
    '+62 895-3723-53053', '+62 895-3774-48600', '+62 895-3779-49988', '+62 895-4226-12241', '+62 895-6187-72656', '+62 895-6353-76226', '+62 895-8005-26036', 
    '+62 896-0112-7273', '+62 896-0271-8787', '+62 896-0354-5768', '+62 896-0651-9291', '+62 896-1876-4875', '+62 896-3283-3063', '+62 896-3644-9852', 
    '+62 896-3713-2844', '+62 896-5170-7382', '+62 896-5217-7933', '+62 896-5374-2719', '+62 896-5486-4884', '+62 896-5685-8168', '+62 896-5809-6073', 
    '+62 896-6261-6946', '+62 896-6348-8224', '+62 896-6748-4999', '+62 896-6943-1230', '+62 896-7179-3468', '+62 896-8079-7323', '+62 896-8185-3050', 
    '+62 896-8282-4251', '+62 896-8533-6014', '+62 896-8771-4407', '+62 896-9423-5443', '+62 896-9867-5508', '+62 897-3882-923', '+62 897-6029-707', 
    '+62 897-6595-914', '+62 897-7453-936', '+62 897-9132-463', '+62 897-9626-811', '+62 898-5375-603', '+62 898-8341-244', '+62 899-0728-036', 
    '+62 899-4091-258', '+62 899-4169-769', '+62 899-4622-890', '+62 899-5468-989', '+62 899-6960-546', '+62 899-7367-438', 'Bingung', 'Rendy', 
    '+62 812-1099-0459', '+62 812-1320-9509', '+62 812-1699-2527', '+62 812-1713-9256', '+62 812-2350-7266', '+62 812-2514-7629', 
    '+62 812-2717-6119', '+62 812-3335-5664', '+62 812-3997-0666', '+62 812-4260-8078', '+62 812-4302-3852', '+62 812-8127-4140', '+62 812-8583-7542', 
    '+62 812-8615-4531', '+62 812-8618-1784', '+62 812-8726-4653', '+62 812-8736-8408', '+62 812-8993-5242', '+62 812-9005-3660', '+62 812-9772-7008', 
    '+62 812-9837-4424', '+62 812-9934-1891', '+62 813-1040-4291', '+62 813-1144-2155', '+62 813-1614-2833', '+62 813-2426-1130', '+62 813-3006-7834', 
    '+62 813-3036-5661', '+62 813-3314-4137', '+62 813-3691-3641', '+62 813-4385-9463', '+62 813-4659-2436', '+62 813-5718-9585', '+62 813-6320-5735', 
    '+62 813-6519-0751', '+62 813-7326-9730', '+62 813-7982-6684', '+62 813-8447-8029', '+62 813-8948-3505', '+62 814-1419-3985', '+62 815-1461-1055', 
    '+62 815-1555-5820', '+62 815-2825-2655', '+62 816-3278-1106', '+62 819-0323-2209', '+62 819-1179-4623', '+62 819-9098-8804', '+62 821-1329-3786', 
    '+62 821-1700-5624', '+62 821-2424-6148', '+62 821-3638-0885', '+62 821-3815-7158', '+62 821-6658-3109', '+62 821-6979-3040', '+62 821-9881-8887', 
    '+62 822-1152-9571', '+62 822-1307-7895', '+62 822-1432-1618', '+62 822-1787-7294', '+62 822-2693-6373', '+62 822-2777-7396', '+62 822-4297-5549', 
    '+62 822-4487-9410', '+62 822-4617-4831', '+62 822-4803-0234', '+62 822-5295-3670', '+62 822-5356-7744', '+62 822-6026-1705', '+62 822-6187-1215', 
    '+62 822-6849-9740', '+62 822-7657-5945', '+62 822-8220-7940', '+62 822-8252-6154', '+62 822-8258-5741', '+62 822-9155-1636', '+62 822-9322-7635', 
    '+62 822-9697-4919', '+62 822-9807-5595', '+62 822-9840-4197', '+62 823-2023-2281', '+62 823-2923-2015', '+62 823-3895-2429', '+62 823-3944-9735', 
    '+62 823-8296-7945', '+62 823-8585-6692', '+62 823-9126-9089', '+62 831-2405-1446', '+62 831-3148-6695', '+62 831-7044-9390', '+62 831-8477-6835', 
    '+62 831-9935-2329', '+62 838-1254-0166', '+62 838-2915-4171', '+62 838-3234-4895', '+62 838-3660-0900', '+62 838-5312-1830', '+62 838-7845-8041', 
    '+62 838-9431-2008', '+62 838-9534-8458', '+62 851-5502-7794', '+62 851-5514-9420', '+62 851-5515-5814', '+62 851-5515-8382', '+62 851-5524-6224', 
    '+62 851-5545-6647', '+62 851-5546-0103', '+62 851-5605-2421', '+62 851-5614-9251', '+62 851-5621-9745', '+62 851-5623-8833', '+62 851-5634-9142', 
    '+62 851-5697-6341', '+62 851-5761-0544', '+62 851-5772-5422', '+62 851-5834-4258', '+62 851-5882-4759', '+62 851-6128-4056', '+62 851-6164-2243', 
    '+62 851-7101-0223', '+62 852-1854-3751', '+62 852-2964-1286', '+62 852-3317-5707', '+62 852-3569-5049', '+62 852-4193-6109', '+62 852-5881-1998', 
    '+62 852-6762-2765', '+62 852-9869-1292', '+62 852-9944-0959', '+62 853-2016-9186', '+62 853-2154-3374', '+62 853-2678-1779', '+62 853-3003-2334', 
    '+62 853-4262-2831', '+62 853-4691-8317', '+62 853-5876-3564', '+62 853-6258-1787', '+62 856-0091-1628', '+62 856-2107-315', '+62 856-2446-2650', 
    '+62 856-3090-411', '+62 856-4207-9252', '+62 856-4302-7156', '+62 856-4640-8825', '+62 856-7979-046', '+62 856-9709-8208', '+62 857-0378-4016', 
    '+62 857-0400-3999', '+62 857-0696-1423', '+62 857-0814-5366', '+62 857-1027-5685', '+62 857-2466-0941', '+62 857-3805-0589', '+62 857-4010-8699', 
    '+62 857-5909-0498', '+62 857-7031-0875', '+62 857-7092-4422', '+62 857-7223-9015', '+62 857-7966-6574', '+62 857-8064-0905', '+62 857-9372-6252', 
    '+62 857-9439-7743', '+62 858-4396-8654', '+62 858-5923-1120', '+62 858-5924-9310', '+62 858-6631-3827', '+62 858-7125-9300', '+62 858-8577-0540', 
    '+62 858-9184-4317', '+62 858-9246-1249', '+62 858-9290-7311', '+62 858-9349-8804', '+62 858-9443-5830', '+62 877-7108-9000', '+62 877-8211-6900', 
    '+62 878-1638-5269', '+62 878-2175-5682', '+62 878-5068-3841', '+62 878-5540-0863', '+62 878-7000-7248', '+62 878-7356-9120', '+62 878-8870-7531', 
    '+62 878-9471-7568', '+62 881-1173-460', '+62 882-1030-6405', '+62 882-3288-9398', '+62 889-7302-3547', '+62 895-0111-0550', '+62 895-1600-5499', 
    '+62 895-1736-6267', '+62 895-2435-0491', '+62 895-2487-3468', '+62 895-2488-2131', '+62 895-2794-6040', '+62 895-2907-4743', '+62 895-2954-5531', 
    '+62 895-2991-0216', '+62 895-3304-00346', '+62 895-3321-11594', '+62 895-3323-79264', '+62 895-3403-65932', '+62 895-3472-82572', '+62 895-3491-33844', 
    '+62 895-3723-53053', '+62 895-3774-48600', '+62 895-3779-49988', '+62 895-4226-12241', '+62 895-6187-72656', '+62 895-6353-76226', '+62 895-8005-26036', 
    '+62 896-0112-7273', '+62 896-0271-8787', '+62 896-0354-5768', '+62 896-0651-9291', '+62 896-1876-4875', '+62 896-3283-3063', '+62 896-3644-9852', 
    '+62 896-3713-2844', '+62 896-5170-7382', '+62 896-5217-7933', '+62 896-5374-2719', '+62 896-5486-4884', '+62 896-5685-8168', '+62 896-5809-6073', 
    '+62 896-6261-6946', '+62 896-6348-8224', '+62 896-6748-4999', '+62 896-6943-1230', '+62 896-7179-3468', '+62 896-8079-7323', '+62 896-8185-3050', 
    '+62 896-8282-4251', '+62 896-8533-6014', '+62 896-8771-4407', '+62 896-9423-5443', '+62 896-9867-5508', '+62 897-3882-923', '+62 897-6029-707', 
    '+62 897-6595-914', '+62 897-7453-936', '+62 897-9132-463', '+62 897-9626-811', '+62 898-5375-603', '+62 898-8341-244', '+62 899-0728-036', 
    '+62 899-4091-258', '+62 899-4169-769', '+62 899-4622-890', '+62 899-5468-989', '+62 899-6960-546', '+62 899-7367-438']


# START
time.sleep(5)
    

for i in range(len(groups)):
    link = 'https://www.facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('/buy_sell_discussion')
    pyautogui.typewrite('\n')
    
    print('sedang mengakses, tunggu 15 detik')
    time.sleep(15)
    
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
    
    # Masukan Content
    pyautogui.typewrite('Gasken Murah!')
    
    # Masukan Foto
    pyautogui.hotkey('command','f')
    pyautogui.hotkey('command', 'a')
    pyautogui.typewrite('tambahkan foto/video')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(3)
    
    # File
    pyautogui.hotkey('command', 'a')
    time.sleep(3)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    
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