Authors: Yash Kumar, Siddhant Sen, Bharat Pappu

files
index.html 
README.txt (README.txt)
site.html (main quiz page)
hi.html (resulting website with results)
ai.py (contains code that is used in server.py)
LuminosityData - Sheet1.csv (data used in the training of the ai to determine the suggestions)
Personal qa.py (contains questions)
Procfile (assists in Heroku server)
requirements.txt (assists in Heroku server)
server.py (main program)


Functionality of program
opens website with questionnaire
ai analyzes the answers to questionnaire and gives a suggestion to improve the "energy score"
energy score is a measure of how an individual impacts energy sustainability

known bugs
- server/website can crash
- if it does, all hope is lost  
Copyright and Licensing Information
libraries used: numpy, pandas, scikit-learn