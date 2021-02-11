from binance.client import Client
from configparser import ConfigParser
from tkinter import *

cmdList = {
    "config":"self.configure()"  
}

class gui:

    def __init__(self, master):
        
        master.columnconfigure(0, weight=1)

        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)

        # Intended to act as a pseudo-console for output
        self.output = Listbox(master)
        self.output.grid(row=0, column=0, columnspan=2,sticky="nsew")
        # Get user input for commands
        self.inputBox = Entry(master)
        self.inputBox.grid(row=1, column=0, sticky="ew")
    
        self.submit = Button(master, text="→", command=self.processCommand)
        self.submit.grid(row=1, column=1, sticky="ew")

        #Bind enter key to yield same results as clicking submit button
        master.bind('<Return>', self.processCommand)

        self.out("bTrader successfully loaded.", 1)


    def out(self, text, origin):
        # Origin 1 is from the application and will not be prefaced by >, origin 0 is from user and will be prefaced in order to clearly denote commands
        if origin == 1:
            self.output.insert(END, str(text))
        else:
            self.output.insert(END, ">" + str(text))

        self.output.yview(END)


    def processCommand(self, *event): #*event parameter added since master.bind also passes thru keystroke event to method
        # Gets contents of inputBox, stores to variable txt then clears box
        txt = self.inputBox.get()
        
        #separates the command and puts each word given in an individual list index
        command = txt.split()

        if not txt == "":
            self.inputBox.delete(0, 'end')
            self.out(txt, 0)

            self.args = []

            #make arguments separate list
            if len(command) > 1:
                for i in range(len(command)):
                    self.args.append(command[i])
                
                print(self.args)


            #If the first item in the list (the main command) exists in the dictionary
            if command[0] not in cmdList:
                self.out("Invalid command! Type 'help' for a list of commands", 1)
            else:
                exec(cmdList[command[0]])

    def configure(self):
        pass
        

        

if __name__=="__main__":
    #main window params
    root = Tk()
    root.geometry("450x350")
    root.title("bTrader")
    ui = gui(root)
    root.mainloop()
    



