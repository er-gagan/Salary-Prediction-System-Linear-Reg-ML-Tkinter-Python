from tkinter import *
root = Tk()
root.title("Salary Prediction System")
root.geometry('800x650')
root.resizable(0,0)

test_data = StringVar()

Label(root,text="Welcome to Salary Prediction System",font=("ArialBlack",20)).place(x=170,y=5)
Button(root,text="Find DataSet",font=('ArialBlack',13),bd=5).place(x=20,y=50)
Text(root,font=("ArialBlack",13),height=3,width=50).place(x=150,y=50)

Label(root,text="Write here..",font=("ArialBlack",12)).place(x=610,y=50)
Entry(root,font=('ArialBlack',18),width=5).place(x=610,y=80)
Button(root,text="Submit",font=('ArialBlack',13),bd=3).place(x=700,y=78)
testdata_list=['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8',]
test_data.set("Enter test data size (between 0 and 1)")
o1 = OptionMenu(root,test_data,*testdata_list)
o1.config(font=("ArialBlack",15))
o1['menu'].configure(font=("ArialBlack",15))
o1.place(x=150,y=200)

Button(root,text="Submit",font=("ArialBlack",13)).place(x=155,y=240)

Button(root,text="Click here to predict test data in trained model..",font=("ArialBlack",12)).place(x=230,y=280)

Button(root,text="Click here to see above result in graphical format..",font=("ArialBlack",12)).place(x=230,y=420)

Label(root,text="Enter experience in years of the candidates,\nseparated by comma",font=("ArialBlack",13)).place(x=20,y=540)
Entry(root,font=("ArialBlack",14),width=30,bd=5).place(x=20,y=590)

root.mainloop()