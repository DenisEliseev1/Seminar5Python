def run (): # Ход игрока
    print (f'Ход игрока - {g[9]} введите номер ячейки для хода \nХод игрока 1 - Х, игрока 2 - О')
    y = int (input('Ваш ход -'))
    if ((g[y-1]!='X') or (g[y-1]!='O')) == True: # Проверка на занятость клетки
        match g[9]: # Проверка очередности и ввод значения
                case 1: 
                        g[y-1] = 'X'
                        g[9], g[10] = g[10], g[9]
                case 2:
                        g[y-1] = 'O'
                        g[9], g[10] = g[10], g[9]
    else:
        run (g) # если клетка занята функция повторятется

def winner (g): # определение победителя
        f = lambda g, x, y, z: g[x]==g[y]==g[z]
        v = (bool (f(g,0,1,2)) or bool (f(g,3,4,5)) or bool (f(g,6,7,8)) 
             or bool (f(g,2,4,6))  or bool (f(g,0,4,8))  or bool (f(g,0,3,6))  
             or bool (f(g,1,4,7)) or bool (f(g,2,5,8)))
        return v
def game ():
        i=0
        while i<9:
                if winner(g) == True:
                        print (f'Выиграл игрок {g[10]}')
                        break
                else:
                        run()
                        gp(g)
                        i+=1

print ('Крестики-нолики, вариант в терминале')
g = [1,2,3,4,5,6,7,8,9,1,2]
gp = lambda g: print (f'|{g[0]}|{g[1]}|{g[2]}|\n|{g[3]}|{g[4]}|{g[5]}|\n|{g[6]}|{g[7]}|{g[8]}|')
gp (g)
game ()
