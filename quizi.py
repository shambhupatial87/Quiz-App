# import everything from tkinter
from tkinter import *
#  importing  messagebox from tkinter as mb
from tkinter import messagebox as mb
# importing json for using jason file later on
import json

# creating of class( for defining various components of our GUI)
class Quizi:

    # using construction for initializing and assigning values to data members of class
    def __init__(self):

        self.que_no = 0
        self.disp_the_title()
        self.disp_the_ques()
        # intvar holds integer
        self.selected_option = IntVar()

        # for creating multiple choice options ( for choosing a particular type of option)
        self.opts = self.radio_buttons()

        self.disp_the_opt()

        self.buttons()
        # the no of questions that will appear on screen is equal to questions which appear in json file
        self.size_of_data = len(question)

        # no of correct questions at start =0
        self.flag = 0

    def disp_the_resc(self):
            # calculates the wrong number  of questions
            wrong_count = self.size_of_data - self.flag
            flag = f"correct answers : {self.flag}"
            wrong = f"Wrong answers : { wrong_count}"

            # calculates the percentage of no of correct answers
            score = int(self.flag / self.size_of_data * 100)
            result = f"Score: {score}%"

            # to display result in form of message box
            mb.showinfo("FINAL RESULT ", f"{result}\n{flag}\n{wrong}\n\n\nTHE CORRECT ANSWER LIST IS :\n {answer}\n")

    def check_the_answer(self, que_no):

        #for checking  if choosed options  are correct
        # if user has choosed the correct option as shown in json file
        if self.selected_option.get() == answer[que_no]:
            # if the option is correct it return true
            return True

    def next_button(self):

        # Check if the answer is correct
        if self.check_the_answer(self.que_no):
            # incrementing the initial value of correct option by user with 1
            self.flag += 1

        # moving towards the next question
        self.que_no += 1

        # if the que_no size is equal to the size_of_data i.e user has attempted all the questions
        if self.que_no == self.size_of_data:

            # for displaying result
            self.disp_the_resc()

            # ends the gui
            goble.destroy()
        else:
            # moves towards the next question
            self.disp_the_ques()
            self.disp_the_opt()

    def buttons(self):

     # position of next button
     next_button = Button(goble, text="Next", command=self.next_button,
                          width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

     # defining position of next button
     next_button.place(x=350, y=300)

     # button for quiting ( close the GUI window)
     quit_button = Button(goble, text="Quit", command=goble.destroy,
                          width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

     # defining position of quit button
     quit_button.place(x=700, y=50)

    def disp_the_title(self):
     #  for title box
      title = Label(goble, text="PREP QUIZ",
                  width=60, bg="#ffffff", fg="#05bce0",justify =CENTER,
                    font=("Monotype corsiva",22, "bold","underline"))

    # position of title box
      title.place(x=5, y=2)

       # display questions
  #Question Box
    def disp_the_ques(self):
       question_no = Label(goble, text=question[self.que_no], width=60,
                    bg="#ffffff", fg="#2d3142", justify = LEFT,
                      font=('ariel', 16), anchor='w',)
   #position of question box
       question_no.place(x=20, y=100)


    def disp_the_opt(self):
        val = 0

        # deselecting the options
        self.selected_option.set(0)

        # creating a loop to show options in radio buttons
        for option in options[self.que_no]:
            self.opts[val]['text'] = option
            val =val+1


    def radio_buttons(self):
        # creating an empty list of options ( for adding options to the list later on)
        question_list = []

        # defining position of first option
        y_axis_position = 150

        # adding the options to the list
        # for displaying only 4 options to user
        while len(question_list) < 4:
            # setting radio button
            radio_button = Radiobutton(goble, text=" ", variable=self.selected_option, value=len(question_list) + 1,
                                        font=("ariel", 15))

            # adding the button to the list ( appended every element of the list  into buttons)
            question_list.append(radio_button)

            # placing the button
            radio_button.place(x=100, y=y_axis_position)

            # incrementing the y-axis position by 40
            y_axis_position += 40

        # return the radio buttons
        return question_list

# for defining GUI as goble
goble = Tk()
goble.configure(bg="#add8e6")


# set the size of the quiz app
goble.geometry("950x396")

# customised  title for quiz app (GUI Window)
goble.title(" EASY QUIZI ")


with open('info.json') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# create an object of the Quiz Class.
quiz = Quizi()

#starting Quizi app window
goble.mainloop()