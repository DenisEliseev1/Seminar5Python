# Создайте программу для игры в ""Крестики-нолики""

# Создать окно с кнопками

from tkinter import *
from tkinter import ttk

def clicked ():    
        # b = Button(window, text=" X ") 
        btn['text'] = 'X' 
        
window = Tk() #Создание окна
gamer = 1
window.title("Крестики - нолики") # создание наименования окна
window.geometry ('200x200')
text1 =  Label (window, text=f'Ход игрока {gamer}') # создание текста в окне для информирования игроков
text1.grid (column=0, row=0)
'''
for i in range(1,4): # Создание кнопок
    for j in range(3):
        btn = Button(window, text="   ")  
        #btn = Button(window, text="   ", command=clicked (gamer))  
        btn.grid(column=j, row=i)
'''
btn1 = ttk.Button(window, text="   ")
btn1.grid(column=0, row=1)
btn2 = ttk.Button(window, text="   ")
btn2.grid(column=1, row=1)
btn3 = ttk.Button(window, text="   ")
btn3.grid(column=2, row=1)
btn4 = ttk.Button(window, text="   ")
btn4.grid(column=0, row=2)
btn5 = ttk.Button(window, text="   ")
btn5.grid(column=1, row=2)
btn6 = ttk.Button(window, text="   ")
btn6.grid(column=2, row=2)
btn7 = ttk.Button(window, text="   ")
btn7.grid(column=0, row=3)
btn8 = ttk.Button(window, text="   ")
btn8.grid(column=1, row=3)
btn9 = ttk.Button(window, text="   ")
btn9.grid(column=2, row=3)
print (type (btn1))
window.bind_class ('Button','<ButtonPress-1>', clicked)
window.mainloop() # не даёт закрыть окно




# прописать логику при нажатии на кнопку в определённый ход
# прописать условия выхода