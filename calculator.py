import tkinter as tk
from tkinter import ttk

from math import sqrt



class data():
    def __init__(self) -> None:
        self.history = []

    def write(self, list_expression = []):
        self.history.append(list_expression)

    def read(self):
        return self.history


class Calculator(data):
    def __init__(self) -> None:
        Gui()
    
    def calculate(self, input):
        try: 
            result = str(eval(input))
            self.write([input, result])
            return str(eval(input))
        except:
            print("exeption")

class Gui(Calculator):
    def __init__(self):
        self.state = "calc"
        
        
        self.root = tk.Tk()
        self.root.title("Calculator")
        

        self.build()
        self.style()

 


        self.root.mainloop()





    def build(self):

        

        self.calc_frame = tk.Frame(self.root)
        


        self.history_wrap_frame = tk.Frame(self.root, width = 200)
        



        self.history_wrap_frame.grid(row=0, column=0)
        self.calc_frame.grid(row=0, column=1)
        


        # HISTORY
        self.display = tk.Label(self.history_wrap_frame, text = "History", font=("Arial", 32), width=12)
        self.display.pack()

        self.history_frame = tk.Frame(self.root, width = 200, height = 300) 
        #self.history_frame.grid(row=0, column=0)



        # DISPLAY

        

        self.display = tk.Label(self.calc_frame, text = "0", font=("Arial", 32), anchor="e", justify="right", width=12)
        self.display.pack()





        # Frame for numbers and operators
        self.numpad_frame = tk.Frame(self.calc_frame)
        self.numpad_frame.pack()

        #Numpad
        list_buttons = [
            "(", ")", "C", "\u2190",
            "\u221A", "x^2", "x^x", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ".", "="
        ]

        self.buildButtons(list_buttons, self.numpad_frame, 4) 


    def buildButtons(self, list_buttons, frame, maxCol = 1): #Create buttons for a frame 
        row = 0
        col = 0

        for button_text in list_buttons:
            button = tk.Button(frame, text=button_text, font=("Arial", 16), width=6, height=2, borderwidth=0)
            button.grid(row=row, column=col, padx=2, pady=2)
            button.bind("<Button-1>", self.events)
            col += 1
            if col == maxCol:
                col = 0
                row += 1
    
    def displayText(self, text):
        

        if len(self.display.cget("text")) == 0:
            newText = 0
        else:
                
            if self.display.cget("text") == "0":
                newText = text
            else:
                newText = self.display.cget("text") + text
                    
        self.display.config(text = newText)



    def events(self, event): #Button events
        newText = ""
        text = event.widget.cget("text")
        self.display.focus_set()

        match text:
            case "=":
                new = self.display.cget("text").replace('\u221A', 'sqrt')
                new = new.replace('^', '**')

                newText = self.calculate(new)
                self.display.config(text = newText)

            case "C":
                self.display.config(text = "0")
            

            case "\u2190": #Backspace

                newText = self.display.cget("text")[:-1]
                self.display.config(text = newText)
                if len(self.display.cget("text")) == 0:
                    self.display.config(text = "0")

            case "+/-":
                if self.display.cget("text")[0] != "-":
                    newText = "-" + self.display.cget("text")
                else:
                    newText = self.display.cget("text")[1:]

                self.display.config(text = newText)
                
            case "\u221A": #Squareroot
                newText = text + "("
                self.displayText(newText)
            
            case "x^2": 
                newText = "^2"
                self.displayText(newText)

            case "x^x":
                print("SAdasdsdsd")
                newText = "^"
                self.displayText(newText)
            
            case "\u2591":
                self.stateMachine("history")


            case _:
                newText = text
                self.displayText(newText)

    def styleChildren(self, widget, bg_color, text_color):
        widget.configure(bg=bg_color)
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.configure(fg=text_color)
        if isinstance(widget, tk.Frame):
            for child in widget.winfo_children():
                self.styleChildren(child, bg_color, text_color)
                    

    def style(self):

        backgroundColor = "#262626"
        fontColor = "#ffffff"

        self.styleChildren(self.numpad_frame, "#3d3d3d", fontColor)

        self.root.config(background = backgroundColor)
        self.display.config(background = backgroundColor)
        self.numpad_frame.config(background = backgroundColor)
        self.display.config(fg = fontColor)


    




    



    




if __name__ == "__main__":
    Calculator()