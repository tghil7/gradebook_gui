import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import datetime;
import csv;
import copy;

#Create a frame 
m = tk.Tk();
file_read = [] #List to store the list of values from the file read
#Add text window to my user interface
def add_text(m):    
    # Create a LabelFrame for the welcome message
    welcome_frame = ttk.LabelFrame(m)
    welcome_frame.pack(padx=10, pady=10, fill="both")

    # Display the welcome message
    welcome_label = ttk.Label(welcome_frame, text="PYTHON GRADEBOOK \n Anicet Akanza \n Application Development\n Graphical User Interface Assignment")
    welcome_label.pack(padx=10, pady=10)
    
#Create the interface   
def createGUI():
    m.title ('Python GUI Gradebook')
    m.geometry ('1000x1200')
    menubar = Menu(m)
    #Create the first frame for adding the text
    #text_frame = LabelFrame(m, text="PYTHON GRADEBOOK \n Anicet Akanza \n Application Development\n Graphical User Interface Assignment")
    add_text(m)
    #Add the second frame that will have the computation result
    #result_frame.grid(row=2, column=0, rowspan=15)
    return menubar

def newWindow():
    m = tk.Tk(); 
    m.title ('New Window - Python GUI Gradebook')
    m.geometry ('600x600')

def closeWindow():
    m.destroy() 


def createMenu():
    menubar = createGUI()
    #Add each tab of the menu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label= 'New Window' , command=newWindow)
    file_menu.add_command(label= 'Open File' , command=openFile)
    file_menu.add_command(label= 'Save File' , command=newWindow)
    file_menu.add_command(label= 'Print' , command=newWindow)
    file_menu.add_separator()
    file_menu.add_command(label= 'Exit Program' , command=closeWindow)
    menubar.add_cascade(label="File", menu=file_menu)
    m.config(menu=menubar)

def readFromFile(filename): 
    grades = []
    with open(filename, newline="") as file: 
        reader = csv.reader(file) 
        for row in reader: grades.append(row)
    return grades

def writeToFile(list):
    with open("gradebook_updated.csv", "w", newline="") as file: 
        writer = csv.writer(file) 
        writer.writerows(list)

def openFile():
    filename = filedialog.askopenfilename(initialdir = "C:/Users/Anicet/Documents/ESU/IS 826 OA",
                                          title = "Select a File",
                                          filetypes = (('text files', '*.txt'),
                                                       ("all files",
                                                        "*.*")))
    file_read = readFromFile(filename)
    createTable(file_read)
    createGraph(file_read)

    
def computeStudentAvg(grades):
    # Compute the student average
    student_grades = []
    list_student_grades = copy.deepcopy(grades)  # Move the grades to another list on which operations will be performed.
    compute_student_average = []
    #Remove the first list containing the grades only
    list_student_grades.pop(0)
    #Get each element of the list
    for student_records in  list_student_grades: 
        student_records.pop(0)
        # Convert the grades into integers
        student_grades = [eval (i) for i in student_records]
        #Compute the grades for each student and add it to the list of student average grades. 
        compute_student_average.append((sum(student_grades)/len(student_grades)))
    compute_student_average.insert(0,'Average');
    grades.append(compute_student_average);
    '''for i in range (len(grades)):
        grades[i].append(compute_student_average[i])'''
    
    return grades

def computeClassAvg(grades):
    list_average = []; #This item will store the list of average per grade group
    list_student_grades = copy.deepcopy(grades)
    list_student_grades.pop(0)
    '''This block code converts each grade into string and computes the 
    average of each grade group.'''
    for student_records in  list_student_grades: 
        student_records.pop(0)
    for i in range (len(list_student_grades)):
        element_instance = list_student_grades[i]; # Get each element in the two-dimensional list
        student_grades = [eval (i) for i in element_instance]; # Convert the grades into integers
        list_average.append(student_grades);
    column_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*list_average)];
    column_average.append(sum(column_average)/len(column_average))
    column_average.insert(0, 'Class Average')
    grades.append(column_average)
    return grades;





def getGrade (number):
    if number >=90:
        return 'A';
    elif number <90 and number >=80:
        return 'B';
    elif number <80 and number >=70:
        return 'C';
    elif number <70 and number >=60:
        return 'D';
    elif number < 60:
        return 'F';


# This function specifically only calculates and returns the average grade for each student. 
def computeStudentAvgReturnOnly(Name_and_Grade_of_all_students):
    # Compute the student average
    element_i_instance = [];
    compute_student_average_class= [];
    #Get each element of the list
    for i in range (len(Name_and_Grade_of_all_students)):
        # Getting all the student's names and grades 
        element_i_instance = Name_and_Grade_of_all_students[i];
        student_name = element_i_instance.pop(0); # Retrieve the student's name.
        # Convert the grades into integers
        student_grades = [eval (i) for i in element_i_instance]
        #Compute the grades for each student and add it to the list of student average grades. 
        compute_student_average = [(sum(student_grades)/len(student_grades))]
        compute_student_average_class.append(compute_student_average);
    return compute_student_average_class;


 

def compute_letter_grade(grades):
    compute_grade_average_class = [];
    list_of_grade_letters = []
    # Get the average grade for each student
    list_student_grades_new = copy.deepcopy(grades)
    list_student_grades_new.pop(0) # Remove the list of name and grades

    # Compute the grade average of each student below.
    compute_grade_average_class = computeStudentAvgReturnOnly(list_student_grades_new)
    
    for item in compute_grade_average_class:   
        for i in item: 
            list_of_grade_letters.append(getGrade(i)) # Add each grade let'ter
    #list_of_grade_letters.insert(0, 'Letter Grade') #Insert the expression 'Letter Grade' for display purposes
    grades.append (list_of_grade_letters)#Add the letter grades to the original container
    '''for i in range (len(list_of_grade_letters)):
        grades[i].append(list_of_grade_letters[i])'''
    return list_of_grade_letters


#This function generate a table to display the gradebook file selected by the user. 
def createTable(grade_list):
    # Read the contents of the opened file.
    # Print the contents of the file to the interface
    csv_frame = ttk.LabelFrame(m)
    csv_frame.pack(padx=10, pady=10, fill="both")
    # Display CSV data in a Treeview widget
    columns = grade_list[0]  # Assume the first row contains column names
    tree = ttk.Treeview(csv_frame, columns=columns, show='headings')

    # Set column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Adjust column width as needed

    # Populate the Treeview with data
    for row in grade_list[1:]:
        tree.insert('', 'end', values=row)
        
    #Add the other results to the display
    tree.pack(fill="both", expand="yes")

def createGraph(file):
    #Get the list of grade letters
    grade_letters = compute_letter_grade(file)
    #Get the percentage of A's in the letter grade 
    count_of_a = 0
    count_of_b = 0
    count_of_c = 0
    count_of_d = 0
    count_of_f = 0

    #Loop through the grade letters to get the count.
    for item in grade_letters:
        if item == 'A':
            count_of_a += 1
        elif item == 'B':
            count_of_b +=1
        elif item == 'C':
            count_of_c +=1
        elif item == 'D':
            count_of_d +=1
        elif item == 'F':
            count_of_f +=1

    chart_frame = ttk.LabelFrame(m)
    chart_frame.pack(padx=10, pady=10, fill="both", expand="yes")
    #Create a canvas and add it to this frame. 
    canvas = Canvas(chart_frame, width=100, height=100)
    canvas.pack(padx=10, pady=10,fill="both", expand="yes")
    #Add the canvas coordinates
    st = 0
    coord = 50, 50, 300, 300
    #Add the percentage of grade letters to create the pie.
    PieV=[(count_of_a *100/len(grade_letters)),(count_of_b *100/len(grade_letters)),(count_of_c *100/len(grade_letters)),(count_of_d *100/len(grade_letters)), (count_of_f *100/len(grade_letters))]
    colV=["Red","Aqua","Green","Blue","Yellow"]
    for val,col in zip(PieV,colV):    
        canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
        st = st + val*3.6
    canvas.create_rectangle((350, 350), (450, 150))
    
    

def main():
    createMenu()
    

if __name__=="__main__": 
    main()  
    m.mainloop()
    