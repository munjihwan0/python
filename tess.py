from tkinter import *
def selectData() :
    pass
def insertData() :
    pass

root = Tk()
root.title("컴퓨터과 3학년 1반 9번 문지환")

edtFrame = Frame(root)
edtFrame.pack()
listFrame = Frame(root)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10)
edt2 = Entry(edtFrame, width=10)
edt3 = Entry(edtFrame, width=10)
edt4 = Entry(edtFrame, width=10)

edt1.pack(side = LEFT, padx=10, pady=10)
edt2.pack(side = LEFT, padx=10, pady=10)
edt3.pack(side = LEFT, padx=10, pady=10)
edt4.pack(side = LEFT, padx=10, pady=10)

btninsert = Button(edtFrame, text="입력", command = insertData)
btninsert.pack(side = LEFT, padx=10, pady=10)

btnSelect = Button(edtFrame , text="조회", command = selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame,bg = 'yellowgreen')
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame,bg = 'yellowgreen')
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame,bg = 'yellowgreen')
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame,bg = 'yellowgreen')
listData4.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
