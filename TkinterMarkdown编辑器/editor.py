from tkinter import *
from tkinter import messagebox,ttk,filedialog
from tkhtmlview import HTMLLabel
from markdown2 import Markdown

root=Tk()
root.geometry("800x900")
root.title('markdown editor')

topbar=Frame(root,width=800,height=200)
topbar.place(x=0,y=0)

showbar=Frame(root,width=800,height=700)
showbar.place(x=0,y=200)

def savefile():
    
    filedata = inputeditor.get("1.0" , END)
    savefilename = filedialog.asksaveasfilename(filetypes = (("Markdown File", "*.md"),
                                                                  ) , title="保存 Markdown 文件")
    if savefilename:
        try:
            f = open(savefilename+".md" , "w")
            f.write(filedata)
        except:
            messagebox.showerror("保存文件错误" , "哎呀！, 文件: {} 保存错误！".format(savefilename))

def openfile():
    openfilename = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"),
                                                                  ("Text File", "*.txt"),
                                                                  ("All Files", "*.*")))
    if openfilename:
        try:
            inputeditor.delete(1.0, END)
            inputeditor.insert(END , open(openfilename).read())
        except:
            messagebox.showerror("打开文件错误，哎呀，文件：{}保存错误".format(openfilename))
tools=ttk.Notebook(topbar,width=800,height=200)

def blood():
    inputeditor.insert("insert","**这里写粗体文本**")
def h1():
    inputeditor.insert("insert","#")
def h2():
    inputeditor.insert("insert","##")
def h3():
    inputeditor.insert("insert","###")
def h5():
    inputeditor.insert("insert","#####")
def unc():
    inputeditor.insert("insert","*要倾斜的文本*")
def userfrom():
    inputeditor.insert("insert",">引用的文本")
def pic():
    inputeditor.insert("insert",'![图片解释](图片链接 "图片标题（可写可不写）")')
def superlink():
    inputeditor.insert("insert",'[超链接名](超链接地址 "超链接title")')


filemenu=Frame(tools)
tools.add(filemenu,text="文件")
quickmenu=Frame(tools)
tools.add(quickmenu,text="插入")

Button(filemenu,text="保存",command=savefile,width=6,height=3).place(x=0,y=50)
Button(filemenu,text="打开",command=openfile,width=6,height=3).place(x=65,y=50)

Button(quickmenu,text="粗体",command=blood,width=6,height=3).place(x=0,y=50)
Button(quickmenu,text="h1",command=h1,width=6,height=3).place(x=60,y=50)
Button(quickmenu,text="h2",command=h2,width=6,height=3).place(x=120,y=50)
Button(quickmenu,text="h3",command=h3,width=6,height=3).place(x=180,y=50)
Button(quickmenu,text="h5",command=h5,width=6,height=3).place(x=240,y=50)
Button(quickmenu,text="斜体",command=unc,width=6,height=3).place(x=300,y=50)
Button(quickmenu,text="引用",command=userfrom,width=6,height=3).place(x=360,y=50)
Button(quickmenu,text="图片",command=pic,width=6,height=3).place(x=420,y=50)
Button(quickmenu,text="超链接",command=superlink,width=6,height=3).place(x=480,y=50)


tools.place(x=0,y=0)


def onInputChange(event):
    inputeditor.edit_modified(0)
    md2html = Markdown()
    outputbox.set_html(md2html.convert(inputeditor.get("1.0" , END)))
inputeditor=Text(showbar,height=70,width=60)
#inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
inputeditor.pack(side=LEFT,fill=BOTH)
outputbox = HTMLLabel(showbar,  background="white", html="<h1>这里什么也没有写</h1>",height=600,width=55)
outputbox.pack(side=RIGHT,fill=BOTH)
inputeditor.bind("<<Modified>>", onInputChange)
#outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
outputbox.fit_height()
#Button(showbar).place(x=0,y=0)\





root.mainloop()