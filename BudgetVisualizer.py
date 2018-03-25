import tkinter as tk
import os

def StoreValues(values, path, master_p):
    if values[-1] not in os.listdir(path):
        os.mknod(path + '/Database/%s.txt' % values[-1])
        filewrite = open(path + '/Database/%s.txt' % values[-1], 'r+')
        filewrite.write('.'.join(values[0]) + '\n')
        if values[1] == 1:
            filewrite.write('Yes\n')
        else:
            filewrite.write('No\n')
        if values[2] == 1:
            filewrite.write('Yes\n')
        else:
            filewrite.write('No\n')
        if values[3] == 1:
            filewrite.write('Yes\n')
        else:
            filewrite.write('No\n')
        if values[4] == 1:
            filewrite.write('Yes\n')
        elif values[4] == 2:
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
        helpmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        master.config(menu=menubar)

class FillTab():
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x450')
        self.master.title('Budget Visualizer - Preliminary Information')
        self.firstTaker = tk.Label(self.master, text = 'Input your budget items, separated by periods (items be modified later).\n(i.e. Gas Bill.Electricity.etc.)', pady = 10)
        self.firstEntry = tk.Entry(self.master)
        self.secondTaker = tk.Label(self.master, text = 'Check all that apply.\nCreate a budget visual for:', pady = 10)
        self.firstCheckvar = tk.IntVar()
        self.secondCheckvar = tk.IntVar()
        self.thirdCheckvar = tk.IntVar()
        self.firstRadioVar = tk.IntVar()
        self.firstCheck = tk.Checkbutton(self.master, text = 'Weekly Budget', variable = self.firstCheckvar)
        self.secondCheck = tk.Checkbutton(self.master, text = 'Monthly Budget', variable = self.secondCheckvar)
        self.thirdCheck = tk.Checkbutton(self.master, text = 'Annual Budget', variable = self.thirdCheckvar)
        self.thirdTaker = tk.Label(self.master, text = 'Select.\nWould you like an average for each section?', pady = 10)
        self.averageRadio1 = tk.Radiobutton(self.master, text = 'Yes', variable = self.firstRadioVar, value = 1)
        self.averageRadio2 = tk.Radiobutton(self.master, text = 'No', variable = self.firstRadioVar, value = 2)
        self.fourthTaker = tk.Label(self.master, text = 'Values can be inputted when the budget is created.', pady = 30)
        self.firstButton = tk.Button(self.master, text = 'Finish', command = lambda: destroy([self.firstEntry.get().split('.' or ','), self.firstCheckvar.get(), self.secondCheckvar.get(), self.thirdCheckvar.get(), self.firstRadioVar.get(), self.secondEntry.get()], os.path.dirname(os.path.abspath(__file__)), master))
        self.fifthTaker = tk.Label(self.master, text = 'Name of File:', pady = 10)
        self.secondEntry = tk.Entry(self.master)

        FillTablist = [self.firstTaker, self.firstEntry, self.secondTaker, self.firstCheck, self.secondCheck, self.thirdCheck, self.thirdTaker, self.averageRadio1, self.averageRadio2, self.fourthTaker, self.fifthTaker, self.secondEntry, self.firstButton]
        for item in FillTablist:
            item.pack()
        def destroy(values, path, master_p):
            for item in FillTablist:
                item.destroy()
            StoreValues(values, path, master_p)

class Budget():
    def __init__(self, master, value, new_file):
        self.master = master
        self.master.title('Budget Visualizer - %s' % value[-1])
        if new_file == True:
            fp = open(os.path.dirname(os.path.abspath(__file__)) + '/Database/%s.txt' % value[-1], 'r+')
            self.rows = fp.readline().strip().split('.')
            self.rownum = len(self.rows)
        elif new_file == False:
            fp = open(os.path.dirname(os.path.abspath(__file__)) + '/Database/%s.txt' % value, 'r+')
            self.rows = fp.readline().strip().split('.')
            self.rownum = len(self.rows)

window = tk.Tk()
def main():
    global window
    window.resizable(False, False)
    if 'Database' not in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/Database')
    app = Home(window)
    window.mainloop()

def Redirect():
    global window
    def RedirectTwo(val):
        global window
        filename.destroy()
        filenamebut.destroy()
        Budget(window, val, False)
    filename = tk.Entry(window)
    filenamebut = tk.Button(window, text = 'Ok', command = lambda: RedirectTwo(filename.get()))
    filename.place(x = 45, y = 20)
    filenamebut.place(x = 1, y = 16)  

if __name__ =='__main__':
    main()
