import tkinter as tk


class TestGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="antique white")
        self.txt = tk.Label(self, text="My tkinter app",
                            bg="blue",
                            fg="white")
        self.btn = tk.Button(self, text="Press me",
                             bg="red",
                             fg="yellow")
        self.edt = tk.Entry(self,
                            bg="green",
                            fg="pink")
        self.sld = tk.Scale(self,
                            from_=0,
                            to=100,
                            orient='vertical')
        self.place_widgets()

    def place_widgets(self):
        self.txt.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
        self.btn.grid(row=0, column=1, padx=10, pady=10, sticky="news")
        self.edt.grid(row=1, column=0, padx=10, pady=10, sticky="news")
        self.sld.grid(row=1, column=1, padx=10, pady=10, sticky="news")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=2)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tkinter Class Example')
    main_frame = TestGUI(root)
    main_frame.pack()
    root.mainloop()
