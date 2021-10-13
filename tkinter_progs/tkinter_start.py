import tkinter as tk


class TestGUI(tk.Frame):
    """ TestGUI is a simple single frame tkinter app demonstrating setting up a button and binding a key press"""

    def __init__(self, parent):
        super().__init__(parent)
        # Configure the frame
        self.config(bg="antique white")
        self.columnconfigure(0, weight=1)

        # Add widgets
        self.edit_text = tk.StringVar()
        self.intro_label = tk.Label(self, text="Press button to say Hello",
                                    bg="navy",
                                    fg="white")
        self.hello_button = tk.Button(self, text='Say Hello (H)',
                                      command=self.press_button)
        self.text_area = tk.Label(self, textvariable=self.edit_text,
                                  background="white",
                                  width=20, height=10)

        self.place_widgets()
        self.bind('<Key>', self.press_key)
        # Put focus on the frame to allow key bind to work
        self.focus()

    def place_widgets(self):
        self.intro_label.grid(row=0, column=0, padx=10, pady=5, sticky="news")
        self.hello_button.grid(row=1, column=0, pady=5)
        self.text_area.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="news")

    def press_button(self):
        txt = self.edit_text.get()
        txt += "Hello World!\n"
        self.edit_text.set(txt)

    def press_key(self, event):
        key_pressed = event.char.lower()
        if key_pressed == "h":
            self.hello_button.invoke()


if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry('400x400+100+100')
    root.title('Simple tkinter GUI')
    root.resizable(1, 0)
    TestGUI(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
