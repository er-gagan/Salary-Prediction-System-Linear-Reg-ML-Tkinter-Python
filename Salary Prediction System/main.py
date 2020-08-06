from tkinter import *
from regression import *
root = Tk()
root.title("Salary Prediction System")
root.geometry('800x650')
root.resizable(0,0)

test_data = StringVar()
selectCsv = StringVar()
year=StringVar()

Label(root,text="Welcome to Salary Prediction System",font=("ArialBlck",20)).place(x=170,y=5)
csv_files = None
def find_dataset():
    global csv_files
    csv_files = checkcsv()
    if csv_files=='No csv file in the directory':
        t1.insert('1.0',csv_files)
    else:
        csv_file = display_and_select_csv(csv_files)
        t1.insert('1.0',csv_file)

csvfile_select = None 
def getcsv():
    global csv_files,csvfile_select
    csv = int(selectCsv.get())
    csvfile_select = csv_files[csv]
    selectfile = f'''{csvfile_select} is selected\nReading csv file..\nCreating Dataset..\nDataset created.'''
    Label(root,text=selectfile,font=("ArialBlack",13)).place(x=200,y=120)
    
Button(root,text="Find DataSet",font=('ArialBlack',13),command=find_dataset,bd=5).place(x=20,y=50)
t1 = Text(root,font=("ArialBlack",13),height=3,width=50)
t1.place(x=150,y=50)
Label(root,text="Write here..",font=("ArialBlack",12)).place(x=610,y=50)
Entry(root,font=('ArialBlack',18),width=5,textvariable=selectCsv).place(x=610,y=80)
Button(root,text="Submit",font=('ArialBlack',13),bd=3,command=getcsv).place(x=700,y=78)
listdata=None
def test_data_fun():
    global csvfile_select,listdata
    testdata = test_data.get()
    listdata = test_model(csvfile_select,testdata)
    Label(root,text="Model creation in progression",font=("ArialBlack",13)).place(x=300,y=210)
    Label(root,text="Model is created",font=("ArialBlack",13)).place(x=330,y=235)

testdata_list=['0.1','0.2','0.3']
test_data.set("Enter test data size (between 0 and 1)")
o1 = OptionMenu(root,test_data,*testdata_list)
o1.config(font=("ArialBlack",15))
o1['menu'].configure(font=("ArialBlack",15))
o1.place(x=150,y=200)
Button(root,text="Submit",font=("ArialBlack",13),command=test_data_fun).place(x=155,y=240)

def predict():
    global listdata
    Label(root,text="X Test: "+str(listdata[0]),font=("ArialBlack",15)).place(x=100,y=310)
    Label(root,text="Y Test: "+str(listdata[1]),font=("ArialBlack",15)).place(x=100,y=340)
    Label(root,text="Y Pred: "+str(listdata[2]),font=("ArialBlack",15)).place(x=100,y=370)

Button(root,text="Click here to predict test data in trained model..",font=("ArialBlack",12),command=predict).place(x=230,y=265)
    
Button(root,text="Click here to see above result in graphical format..",command=show_data,font=("ArialBlack",12)).place(x=230,y=410)

Label(root,text="Now you can predict salary of an employee using our model",font=("ArialBlack",13)).place(x=200,y=450)

Label(root,text="Enter experience in years of the candidates,\nseparated by comma",font=("ArialBlack",13)).place(x=20,y=500)

def get_year():
    Year = year.get()
    all_year_Predict = salary_predict(Year)
    print(all_year_Predict)
    
Entry(root,font=("ArialBlack",14),textvariable=year,width=30,bd=5).place(x=20,y=550)
Button(root,text="Submit",command=get_year,font=("ArialBlack",12)).place(x=150,y=600)

root.mainloop()