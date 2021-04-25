import tkinter
import tkinter.font as font
energyscorePersonal = 0

print("For each multiple choice question, type in the letter that corresponds with the answer you choose")
 
 #Question 1
 
 
 def business_question_one():

        incorrectAnswer_b_one = true
        incomeRange = input("What is the annual income of your business?\nA. $0 - $50,000\nB. $50,000 - $100,000\nC. $100,000 - $200,000\nD. $200,000-$400,000\nE. $400,000-$750,000\nF. $750,000 - $1,000,000\nG. $1,000,000+")
                if (incomeRange == "a"):
                    incomeRange = "$0 - $50,000"
                    incorrectAnswer_b_one = false

                elif (incomeRange == "b"):
                        incomeRange = "$50,000 - $100,000"
                        incorrectAnswer_b_one = false

                elif (incomeRange == "c"):
                        incomeRange = "$100,000 - $200,000"
                        incorrectAnswer_b_one = false

                elif (incomeRange == "d"):
                        incomeRange = "$200,000-$400,000"
                        incorrectAnswer_b_one = false

                elif (incomeRange == "e"):
                        incomeRange = "$400,000-$750,000"
                        incorrectAnswer_b_one = false

                elif (incomeRange == "f"):
                    incomeRange = "$750,000 - $1,000,000"
                    incorrectAnswer_b_one = false

                elif (incomeRange == "g"):
                    incomeRange = "$1,000,000"
                    incorrectAnswer = false
                else:
                    incorrectAnswer = true
