


import tkinter as tk

def save_file():
    inputValue = text_widget.get("1.0", tk.END)
    print(inputValue)
    save_name = tk.Tk()
    save_name.geometry("300x100")
    save_name.title("Save your file")
    name_widget = tk.Text(save_name, bg = "white", height = 1, width = 30)
    name_widget.place(x = 20, y = 30)
    name_label = tk.Label(save_name, text = "Save as: ")
    name_label.place(x = 20, y = 10)

    def save():
        name_value = name_widget.get("1.0", tk.END)
        name_value = name_value.replace("\n", "")

        with open(f"{name_value}.txt", "w", encoding = "utf8") as file:
            file.write(inputValue)
        save_name.destroy()
    save_but = tk.Button(save_name, text = "Save", height = 1, width = 10, command = save)
    save_but.place(x = 20, y = 60)


    save_name.mainloop()

root = tk.Tk()
root.geometry("400x400")
root.title("PyPad")
text_widget = tk.Text(root, bg = "white", height = 200, width = 200)
text_widget.place(x = 0, y = 25)
button_new = tk.Button(root, width = 10, text = "New", command = lambda: text_widget.delete("1.0", tk.END))
button_new.place(x = 0, y = 0)
button_save = tk.Button(root, width = 10, text = "Save", command = save_file)
button_save.place(x = 80, y = 0)

root.mainloop()

