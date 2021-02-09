from binance.client import Client
from tkinter import *

cmdList = {
    "foo":"bar"
}


class gui:

    def __init__(self, master):
        
        master.columnconfigure(0, weight=1)

        # Intended to act as a pseudo-console for output
        self.output = Listbox(master)
        self.output.grid(row=0, column=0, columnspan=2,sticky="nsew")
        # Get user input for commands
        self.inputBox = Entry(master)
        self.inputBox.grid(row=1, column=0, sticky="nsew")
    
        self.submit = Button(master, text="→", command=self.processCommand)
        self.submit.grid(row=1, column=1)


        self.out("bTrader successfully loaded.", 1)


    def out(self, text, origin):
        # Origin 1 is from the application and will not be prefaced by >, origin 0 is from user and will be prefaced in order to clearly denote commands
        if origin == 1:
            self.output.insert(END, str(text))
        else:
            self.output.insert(END, ">" + str(text))


    def processCommand(self):
        # Gets contents of inputBox, stores to variable txt then clears box
        txt = self.inputBox.get()

        if not txt == "":
            self.inputBox.delete(0, 'end')
            self.out(txt, 0)
            if txt not in cmdList:
                self.out("Invalid command! Type 'help' for a list of commands", 1)
        
if __name__=="__main__":
    root = Tk()
    root.geometry("450x350")
    ui = gui(root)
    root.mainloop()
    



