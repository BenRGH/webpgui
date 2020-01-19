from tkinter import Tk, WORD, END, Button, Label, filedialog, scrolledtext, Spinbox
import subprocess

files = ''
qualityValue = 70

def select():
    global files
    files = filedialog.askopenfilenames()
    fileslistbox.delete(1.0,END)
    fileslistbox.insert(END, '\n'.join(files))

def convert():
    print(files)
    skeletonCmd = "./cwebp.exe -q {q} {fileIn} -o {fileOut}.webp"
    for i in files:
        subprocess.call(skeletonCmd.format(
            q=qualityValue,
            fileIn=i,
            fileOut=i.split(".")[0]
        ))
    global fileslistbox
    fileslistbox.delete(1.0,END)
    fileslistbox.insert(END, sysout)

 
window = Tk()

window.title("webpgui")
window.geometry('570x220')
window.resizable(False, False)

lbl = Label(window, text="Convert to webp", font=("Arial Bold", 20))
lbl.grid(column=0, row=0, padx=(100, 10))

fileslistbox = scrolledtext.ScrolledText(window, width=50, height=9, wrap=WORD)
fileslistbox.grid(column=0, row=1, padx=(10, 10))

selectBtn = Button(window, text="Select", command=select, height=9, width=6, bg="lightblue")
selectBtn.grid(column=1, row=1, padx=(0,10))

convertBtn = Button(window, text="Convert", command=convert, height=9, width=6, bg="lightgreen")
convertBtn.grid(column=2, row=1)

qlbl = Label(window, text="Quality %:", font=("Arial Bold", 10), width=10)
qlbl.grid(column=0, row=2)

quality = Spinbox(window, from_=0, to=100, width=6, font=("Arial Bold", 10))
quality.delete(0,END)
quality.insert(0,qualityValue)
quality.grid(column=1, row=2)

window.mainloop()