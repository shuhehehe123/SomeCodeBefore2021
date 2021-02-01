from tkinter import *

#窗口
root=Tk()
root.title('天气查询')
root.geometry('500x600')

blank=Entry(root)

search_button=Button(root,text='查询')

blank.place(x=50,y=0)
search_button.place(x=200,y=0)

root.mainloop()