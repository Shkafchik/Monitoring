from tkinter import *
import psutil
import os


def SysInfo():#Вывод конфигурации пк
    os.system('cls')
    os.system('SYSTEMINFO')

def Proizv():#Производительность пк
    os.system('cls')
    AllMem = psutil.virtual_memory().total
    UsedMem = psutil.virtual_memory().used
    UsedMemPerc = UsedMem * 100 / AllMem
    l = Label(root, text = '')
    l.place(x = 170, y = 150)#163
    l['text'] = "% Использования Цп: {0:.2f}".format(psutil.cpu_percent()) + "%" + "\nВсего озу: " + str(psutil.virtual_memory().total) + "\nЗагруженность ОЗУ: {0:.2f}".format(UsedMemPerc) + "%"

def Proc():#Запущенные процессы
    os.system('cls')
    for proc in psutil.process_iter(['pid', 'name']):
        print("\n" + str(proc.info))
        print("Количество памяти используемой процессом: " + str(proc.memory_info().rss))

os.system('cls')#Очищаем консоль

root = Tk()#Создаем окно tkinter
root.title('Мониторинг показателей Пк')
root.configure(background = '#BDE9EB')
root.resizable(False, False)#Централизуем окно 

window_height = 300
window_width = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

b1 = Button(bg ='White', command = SysInfo,text = 'Cведения о конфигурации компьютера')
b1.place(x = 140.5, y = 30)#233
b2 = Button(bg ='White', command = Proizv,text = 'Производительность компьютера')
b2.place(x = 155, y = 120)#198
b3 = Button(bg = 'White', command = Proc, text ='Запущенные процессы компьютера')
b3.place(x = 150, y =247)#212


root.mainloop()

