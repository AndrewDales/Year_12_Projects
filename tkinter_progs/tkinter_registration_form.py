import tkinter as tk


class TestGUI(tk.Frame):
    """ TestGUI is a simple single frame tkinter app demonstrating setting up a button and binding a key press"""

    def __init__(self, parent):
        super().__init__(parent)

        text_labels = ["Registration Form", "Full name", "Email", "Gender", "Country", "Programming"]
        country_options = ["France", "Germany", "United Kingdom", "United States", "Other"]

        # Add widgets
        # Text labels
        self.labels = [tk.Label(self, text=text_label,
                                justify=tk.LEFT,
                                font=('Arial', 12))
                       for text_label in text_labels]
        self.labels[0].config(font=('Arial', 24))

        # Submit button
        self.submit_button = tk.Button(self, text='Submit',
                                       bg="red",
                                       fg="white",
                                       font=('Arial', 12))

        # Edit boxes
        self.edits = [tk.Entry(self, width=40, font=('Arial', 12))
                      for _ in range(2)]

        # Frame with gender choices
        self.gender_frame = GenderRadioBox(self)

        # Country dropdown
        self.country_var = tk.StringVar()
        self.country_var.set("select your country")
        self.country_select = tk.OptionMenu(self, self.country_var, *country_options)
        self.country_select.config(width=20, anchor='w', font=('Arial', 12))

        # Place the widgets in the grid
        self.place_widgets()

    def place_widgets(self):
        # Place all the text labels in self.labels using grid
        # Registration Label - include columnspan across both columns
        self.labels[0].grid(row=0, column=0, columnspan=2, padx=10, pady=3, sticky="w")
        for i, label in enumerate(self.labels[1:], 1):
            label.grid(row=i, column=0, padx=10, pady=3, sticky="w")

        # Place Submit button
        self.submit_button.grid(row=len(self.labels), column=0, padx=15, pady=(3, 10), sticky="w")

        # Place Edit Boxes
        for i, edt in enumerate(self.edits, 1):
            edt.grid(row=i, column=1, padx=(10, 25), pady=3, sticky="we")

        # Place the Gender frame
        self.gender_frame.grid(row=3, column=1, padx=10, pady=3, sticky="w")

        # Place drop-down window
        self.country_select.grid(row=4, column=1, padx=10, pady=3, sticky="w")


class GenderRadioBox(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        selected_gender = tk.StringVar()
        # selected_gender.set('O')

        gender_values = [('Male', 'M'),
                         ('Female', 'F'),
                         ('Other', 'O')]

        self.radio_options = [tk.Radiobutton(self, text=option[0],
                                             value=option[1],
                                             variable=selected_gender,
                                             font=('Arial', 12))
                              for option in gender_values]

        for ro in self.radio_options:
            ro.pack(side=tk.LEFT)


if __name__ == "__main__":
    root = tk.Tk()
    #  root.geometry('600x400+100+100')
    root.title('Registration Form')
    root.resizable(1, 0)
    TestGUI(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
