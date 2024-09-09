import tkinter as tk

class calc:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("500x800")
        self.root.title("Calculator")

        self.title_label = tk.Label(self.root, text="Calculate: mean & standard deviation", font=('Ariel', 18))
        self.title_label.pack(padx = 20, pady = 20)

        self.explain_label = tk.Label(self.root, text="Enter numbers and seperate with space")
        self.explain_label.pack()

        self.imput_entry = tk.Entry(self.root, width=100, font=('Ariel', 24))
        self.imput_entry.pack(padx = 10)

        
        self.inputframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)
        self.buttonframe.columnconfigure(2, weight = 1)

        col1count = 0
        col2count = 0

        

        for i in range(9):

            self.btn = tk.Button(self.buttonframe, text = i + 1, font=('Ariel', 18))
            self.btn.bind("<Return>", input)

            if i <= 2:
                self.btn.grid(row = 0, column = i, sticky = tk.W + tk.E)
        
        
            elif i >= 3 and i <= 5:
                self.btn.grid(row = 1, column = col1count, sticky = tk.W + tk.E)

                col1count += 1
                
            elif i >= 6:
                self.btn.grid(row = 2, column = col2count, sticky = tk.W + tk.E)
                col2count += 1
            
        

        self.btn = tk.Button(self.buttonframe, text = 0, font=('Ariel', 18))


            
        self.buttonframe.pack(fill = "x")
 
        




        self.calc_button = tk.Button(self.root, text = "Calculate", font = ('Ariel', 18), command = self.calc)
        self.calc_button.pack(pady = 20)







 
        self.root.mainloop()
    
    def calc(self):
        print("hello")






    


calc()