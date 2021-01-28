
# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
from tkinter import *
from tkinter import messagebox
import json
import random

import tkinter.ttk as ttk
import tkinter.font as font
import locale
locale.getpreferredencoding()


class ProgramGUI:

    def __init__(self,master):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data file and creating the user interface.
        # See Points 1 to 6 "Constructor of the GUI Class of quizle.py" section of the  brief. 
        self.master = master
        master.title("PJISP")
        master.minsize(width=1100,height=600)
        master.maxsize(width=1100,height=600)
        frame = Frame(master)
        
        font.nametofont('TkDefaultFont').configure(size=18)

        
        frame.pack()
       
        try:
            with open('pitanja','r', encoding='utf8') as data_file:
                self.data = json.load(data_file)
        except:
            print("Missing/Invalid file")
            master.destroy()
            return    

        if len(self.data)<5:
            messagebox.showerror("Error","Insufficient number of questions")
            master.destroy()
            return

        self.user_score = 0
        self.no_of_question_answered = 0
        self.correct_question = 0
        self.instance = 0
        self.diff_level_value = 0

        self.diifficulty_level = Label(frame)
        self.diifficulty_level.grid(row=1,columnspan=2,padx=20,pady=10)
        
        #tacni odg
        self.tacan = Label(frame)
        self.tacan.grid(row=5,columnspan=2,padx=20,pady=10)

        self.question = Label(frame)
        self.question.grid(row=2,columnspan=2,padx=20,pady=10)

        self.question_entry = Entry(frame)
        self.question_entry.grid(row=3)
        
        self.button = Button(frame,text="Dalje",command=self.checkAnswer)
        self.button.grid(row=3,column=1)
    
        self.question_status = Label(frame)
        self.question_status.grid(row=4,columnspan=2,padx=20,pady=10)

        self.loadQuestion()



       
    def loadQuestion(self):
        # This method is responsible for displaying a question in the GUI,
        # as well as showing the special message for difficult questions and showing the user's current progress 
        # See Point 1 of the "Methods in the GUI Class of quizle.py" section of the  brief.
        self.question_entry.focus_set()
        if self.instance == 0:
            
            self.current_question_set = random.sample(self.data,15)
        
        question = random.choice(self.current_question_set)
            
        self.current_question = question['question']
        self.diff_level_value = int(question['diff_level'])

        if(int(question['diff_level'])>=15):
            self.diifficulty_level.grid(row=1,columnspan=2,padx=20,pady=10)
        else:
            self.diifficulty_level.grid_forget()
            
        self.question.config(text=self.current_question)
        self.question_status.config(text="%s od %s odgovora tačno"%(self.correct_question,self.no_of_question_answered))
        self.question_answer  = question['answer']
        
        self.current_question_set.remove(question)
        
        print(self.current_question_set)

    def checkAnswer(self):
        # This method is responsible for determining whether the user's answer is correct and showing a Correct/Incorrect messagebox.
        # It also checks how many questions have been asked to determine whether or not to end the game.
        # See Point 2 of the "Methods in the GUI Class of quizle.py" section of the a brief.
        self.no_of_question_answered += 1
        if type(self.question_entry.get()) == str:
            user_answer = str(self.question_entry.get()).lower()
        else:
            user_answer = self.question_entry.get()

        if user_answer in self.question_answer:
            self.correct_question +=1
            self.user_score +=1
            #messagebox.showsuccess("Tačno","Tačno!")
        else:
            self.tacan.config(text="Odgovor na prošlo pitanje: " + str(self.question_answer))
        
        print('ques',self.no_of_question_answered)
        if self.no_of_question_answered == 15:
            print('yo:',self.no_of_question_answered)
            messagebox.showinfo("Poena","Poeni: %s \n\n" %(self.user_score))
            self.master.destroy()
        else:
            self.instance +=1
            self.question_entry.delete(0, 'end')
            self.loadQuestion()



# Create an object of the ProgramGUI class to begin the program.
root = Tk()
gui = ProgramGUI(root)
root.mainloop()
