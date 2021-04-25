import tkinter
import tkinter.font as font


energyscorePersonal = 0

print("For each multiple choice question, type in the letter that corresponds with the answer you choose")

#Question 1

def personal_question_one():

        incomeRange = input("What is your household income range? \nA. $0-$35,000\nB. $36,000-$105,000\nC. $106,000-$250,000\nD. $251,000~\n")
                if (incomeRange == "a"):
                    incomeRange = "$0 - $35,000"
                   

                elif (incomeRange == "b"):
                        incomeRange = "$36,000 - $105,000"
                        

                elif (incomeRange == "c"):
                        incomeRange = "$106,000 - $250,000"
                        

                elif (incomeRange == "d"):
                        incomeRange = "$251,000~"
                       
return personal_question_one()
        

#Question 2

def personal_question_one():

        incorrectAnswer_p_two = true
        householdNum = input("How many people live in your household? \nA. 1\nB. 2\nC. 3 or 4\nD. 5~\n")
                if (householdNum == "a"):
                    householdNum = "1"
                    incorrectAnswer_p_two = false

                elif (householdNum == "b"):
                        householdNum = "2"
                        incorrectAnswer_p_two = false

                elif (householdNum == "c"):
                        householdNum = "3 or 4"
                        incorrectAnswer_p_two = false

                elif (householdNum == "d"):
                        householdNum = "5~"
                        incorrectAnswer_p_two = false

                else:
                    incorrectAnswer_p_two == true













































































































