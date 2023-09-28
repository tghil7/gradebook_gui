import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import datetime;
import csv;
import copy;

#Create a frame and add it to the root module
m = tk.Tk(); 
m.title ('Python GUI Gradebook')
m.geometry ('900x700')
menubar = Menu(m)

def newWindow():
    m = tk.Tk(); 
    m.title ('New Window - Python GUI Gradebook')
    m.geometry ('600x600')

def closeWindow():
    m.destroy() 


def createMenu():
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
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    readFromFile(filename)
    
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
    list_of_grade_letters.insert(0, 'Letter Grade') #Insert the expression 'Letter Grade' for display purposes
    grades.append (list_of_grade_letters)#Add the letter grades to the original container
    '''for i in range (len(list_of_grade_letters)):
        grades[i].append(list_of_grade_letters[i])'''
    return grades



def main():
    createMenu()

if __name__=="__main__":   
    main()
    m.mainloop()