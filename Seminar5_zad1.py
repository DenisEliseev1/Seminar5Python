# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def delete (t, d):
    while t.find(d) > 0:
        t = t[:t.find(d)]+t[t.find(d)+len(d):]
        #print (t)
    else: 
        return t
    

text = 'текст абв на абв удаление'
print (text)
y = 'абв'
text = str (delete (text, y))
print (text)

