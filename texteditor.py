import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_file():
    filepath=askopenfilename(filetype=[("text files",".txt"),("all files",".*")])
    if not filepath:
        return
    text_edit.delete(1.0,tk.END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        text_edit.insert(tk.END,text)
    window.title(f"my own writing space-{filepath}")

def save_file():
    filepath=asksaveasfilename(
        defaultextension="txt",filetype=[("text files",".txt"),("all files",".*")]

    )
    if not filename:
        return
    with open(filepath,"w") as output_file:
        text=text_edit.get(1.0,tk.END)
        output_file.write(text)
    window.title(f"my own writing space-{filepath}")

window=tk.Tk()
window.title("my own writing space")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

text_edit=tk.Text(window)
fr_buttons=tk.Frame(window,relief=tk.RAISED,bd=2)
button_open=tk.Button(fr_buttons,text="open",command=open_file)
button_save=tk.Button(fr_buttons,text="save as....",command=save_file)

button_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
button_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsw")

window.mainloop()