import tkinter as tk
import os
import calendar, datetime
from tkinter import messagebox
from tkinter import Image


def StoreValues(values, path, master_p):
    if values[-1] not in os.listdir(path):
        os.mknod(path + '/Database/%s.txt' % values[-1])
        filewrite = open(path + '/Database/%s.txt' % values[-1], 'r+')
        filewrite.write('.'.join(values[0]) + '\n')
        if values[1] == 1:
            filewrite.write('Yes\n')
        elif values[1] == 2:
            filewrite.write('No\n')
        filewrite.close()
    Budget(master_p, values, True)

class Home():
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x500')
        self.master.title('Budget Visualizer - Home')
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New File", command = lambda: FillTab(master))
        filemenu.add_command(label="Open File", command = Redirect)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)
        

class FillTab():
    def __init__(self, master):
        global info
        info.destroy()
        self.master = master
        self.master.geometry('500x350')
        self.master.title('Budget Visualizer - Preliminary Information')
        self.firstTaker = tk.Label(self.master, text = 'Input your budget items, separated by periods.\n(i.e. Gas Bill.Electricity.etc.)', pady = 10)
        self.firstEntry = tk.Entry(self.master)
        self.thirdTaker = tk.Label(self.master, text = 'Select.\nWould you like an average for each section?', pady = 10)
        self.firstRadioVar = tk.IntVar()
        self.averageRadio1 = tk.Radiobutton(self.master, text = 'Yes', variable = self.firstRadioVar, value = 1)
        self.averageRadio2 = tk.Radiobutton(self.master, text = 'No', variable = self.firstRadioVar, value = 2)
        self.fourthTaker = tk.Label(self.master, text = 'Values can be inputted when the budget is created.', pady = 30)
        self.firstButton = tk.Button(self.master, text = 'Finish', command = lambda: destroy([self.firstEntry.get().split('.' or ','), self.firstRadioVar.get(), self.secondEntry.get()], os.path.dirname(os.path.abspath(__file__)), master))
        self.fifthTaker = tk.Label(self.master, text = 'Name of File:', pady = 10)
        self.secondEntry = tk.Entry(self.master)

        FillTablist = [self.firstTaker, self.firstEntry, self.thirdTaker, self.averageRadio1, self.averageRadio2, self.fourthTaker, self.fifthTaker, self.secondEntry, self.firstButton]
        for item in FillTablist:
            item.pack()

        def destroy(values, path, master_p):
            for item in FillTablist:
                item.destroy()
            StoreValues(values, path, master_p)

class Budget():
    def __init__(self, master, value, new_file):
        self.master = master
        self.rowthree = []
        self.rowfive = []
        self.average = 'No'
        self.new_file = new_file
        if self.new_file == True:
            self.master.title('Budget Visualizer - %s' % value[-1])
            self.fp = open(os.path.dirname(os.path.abspath(__file__)) + '/Database/%s.txt' % value[-1], 'r+')
            self.rows = self.fp.readline().strip().split('.')
            self.rowstwo = self.rows
            for item in self.rows:
                self.rowthree.append([item])
                self.rowfive.append([item])

            self.rownum = len(self.rows)
            self.show(value[-1], self.fp)
            if value[1] == '1':
                self.average = 'Yes'
        elif self.new_file == False:
            self.master.title('Budget Visualizer - %s' % value)
            self.fp = open(os.path.dirname(os.path.abspath(__file__)) + '/Database/%s.txt' % value, 'r+')
            self.rows = self.fp.readline().strip().split('.')
            self.rowstwo = self.rows
            for item in self.rows:
                self.rowthree.append([item])
                self.rowfive.append([item])
            self.rownum = len(self.rows)
            self.show(value, self.fp)
            self.average = 'Yes'

        
    def show(self, value, filename):
        if len(self.rows) > 4:
            self.master.geometry('1000x720')
        else:
            self.master.geometry('1000x400')
        self.y = 5
        self.y_2 = 100
        self.x_2 = 140
        self.x_3 = 140
        self.y_3 = 100
        self.y_4 = 100
        self.iter = ''
        self.itertwo = 0
        self.month_list = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.','Total','Average']

        for r in range(len(self.rowstwo)):
            self.rowthree[r].append(list(range(1,15)))
            self.rowfive[r].append(list(range(1,15)))
            for v in range(12):
                self.rowfive[r][1][v] = tk.StringVar()

        for x in range(len(self.rows)):
            item_graph = tk.Label(self.master, text = self.rows[x])
            item_graph.place(x = 76, y = self.y_2)
            self.y_2 += 30
        for s in range(len(self.month_list)):
            month_graph = tk.Label(self.master, text = self.month_list[s])
            month_graph.place(x = self.x_2, y = 80)
            self.x_2 += 60
        for h in range(len(self.rows)):
            for f in range(12):
                self.rowthree[h][1][f] = tk.Entry(self.master, width = 6, textvariable = self.rowfive[h][1][f])
                self.rowthree[h][1][f].place(x = self.x_3, y = self.y_3)
                self.x_3 += 60
            self.rowthree[h][1][12] = tk.Label(self.master)
            self.rowthree[h][1][12].place(x = 860, y = self.y_4)
            self.rowthree[h][1][13] = tk.Label(self.master)
            self.rowthree[h][1][13].place(x = 920, y = self.y_4)
            self.y_4 += 30
            self.y_3 += 30
            self.x_3 = 140

        if self.new_file == False:
            self.initialize()
        else:
            pass

        self.save = tk.Button(self.master, text = 'Save', command = lambda: self.change())
        self.save.place(x = 5, y = self.y)
        self.y += 30
        
    def change(self):
        self.rowfour = []
        for j in range(len(self.rows)):
            for a in range(12):
                self.fp.write(self.rowthree[j][1][a].get() + ' ')
                self.rowfour.append(int(self.rowthree[j][1][a].get()))
            self.rowthree[j][1][12].config(text = sum(self.rowfour))
            self.rowthree[j][1][13].config(text = sum(self.rowfour) / 12)
            self.rowfour[:] = []
    
    def initialize(self):
        self.n = 0
        data = self.fp.readlines()
        data = data[1].strip()
        self.check = data.split(' ')
        for k in range(len(self.rows)):
            for g in range(12):
                self.rowfive[k][1][g].set(self.check[self.n])
                self.n += 1
                
                


window = tk.Tk()

img = tk.PhotoImage('BudgetFavicon.jpeg')
panel = tk.Label(window, image = img)
info = tk.Label(window, text = '\nTo create a new Budget, click File -> New File.\nFill in preliminary information, and the table will be created\nfor you. Whenever the end of the month arrives, the application\nwill alert you to pay your bills. This app is a\nvery efficient way of keeping track of your finances!\nThis project is currently only available in monthly budget mode.', pady = 20, font = ('Comic Sans MS', 10))
info.pack()
panel.pack()

def main():
    global window
    window.resizable(False, False)
    if 'Database' not in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/Database')
    now = datetime.datetime.now()
    if now.day == calendar.monthrange(now.year, now.month)[1]:
        messagebox.showinfo('Title', 'Time to pay the bills!')
    app = Home(window)
    window.mainloop()

def Redirect():
    global window
    global info
    info.destroy()
    def RedirectTwo(val):
        global window
        filename.destroy()
        filenamebut.destroy()
        filelist.destroy()
        Budget(window, val, False)
    filename = tk.Entry(window)
    filelist = tk.Listbox(window, width = 60, height = 200)
    filelist.config(bg = window.cget('bg'))
    filelist.place(x = 5, y = 50)
    for element in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/Database'):
        filelist.insert(1, element)
    filenamebut = tk.Button(window, text = 'Ok', command = lambda: RedirectTwo(filename.get()))
    filename.place(x = 45, y = 20)
    filenamebut.place(x = 1, y = 16)  

if __name__ =='__main__':
    main()
