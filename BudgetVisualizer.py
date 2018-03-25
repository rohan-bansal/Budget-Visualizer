import tkinter as tk
import os

def StoreValues(values, path):
    if values[-1] not in os.listdir(path):
        os.mknod(path + '/%s' % values[-1])
    
class Home():
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x500')
        self.master.title('Budget Visualizer - Home')
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New File", command = lambda: FillTab(master))
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
        self.firstTaker = tk.Label(self.master, text = 'Input your budget items, separated by commas (can be modified later).\n(i.e. Gas Bill, Electricity, etc.)', pady = 10)
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
        self.firstButton = tk.Button(self.master, text = 'Finish', command = lambda: StoreValues([self.firstEntry.get(), self.firstCheckvar.get(), self.secondCheckvar.get(), self.thirdCheckvar.get(), self.firstRadioVar.get(), self.secondEntry.get()], os.path.dirname(os.path.abspath(__file__))))
        self.fifthTaker = tk.Label(self.master, text = 'Name of File:', pady = 10)
        self.secondEntry = tk.Entry(self.master)

        FillTablist = [self.firstTaker, self.firstEntry, self.secondTaker, self.firstCheck, self.secondCheck, self.thirdCheck, self.thirdTaker, self.averageRadio1, self.averageRadio2, self.fourthTaker, self.fifthTaker, self.secondEntry, self.firstButton]
        for item in FillTablist:
            item.pack()


'''
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
'''
def main():
    window = tk.Tk()
    window.resizable(False, False)
    app = Home(window)
    window.mainloop()

if __name__ =='__main__':
    main()
