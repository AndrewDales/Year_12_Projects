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

        self.intro_label.grid(row=0, column=0, padx=10, pady=5, sticky="news")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Simple tkinter GUI')
    root.resizable(1, 0)
    TestGUI(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
