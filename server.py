from flask import Flask, request, render_template
import pandas
import numpy
from sklearn.tree import DecisionTreeClassifier




app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return app.send_static_file("site.html")


@app.route('/you', methods= ["POST"])
def yolo():     
    print(request.form["screen"])
    new_list = [int(x) for x in request.form.values()]
    print(new_list)
    
    ai_1 = new_list[0]
    ai_2 = new_list[1]
    ai_3 = new_list[2]
    ai_4 = new_list[3]
    ai_5 = new_list[4]
    ai_6 = new_list[5]
    ai_7 = new_list[6]
    ai_8 = new_list[7]
    ai_9 = new_list[8]
    ai_10 = new_list[9]
    ai_11 = new_list[10]
    ai_12 = new_list[11]

    score = ai_2*2 + ai_3*5 + ai_4*5 + ai_5*5 + ai_6*3 + ai_7*2 + ai_8*2 + ai_9*2 + ai_10 + ai_11 + ai_12*2

    
    
    luminosity_data = pandas.read_csv('LuminosityData - Sheet1.csv')

    X = luminosity_data.drop(columns=['Suggestions'])
    Y = luminosity_data['Suggestions']

    model = DecisionTreeClassifier()
    model.fit(X,Y)
    luminosity_data
    prediction = model.predict([[ai_1, ai_2, ai_3, ai_4, ai_5, ai_6, ai_7, ai_8, ai_9, ai_10, ai_11, ai_12, 1]])
    sug = prediction[0]
    if (sug == 1):
         sheesh = "Buy an electric car."
    elif (sug == 2):
         sheesh = "Turn off lights in your house."
    elif (sug == 3):
         sheesh = "Take shorter showers."
    elif (sug == 4):
         sheesh = "Carpool or use public transport."
    elif (sug == 5):
         sheesh = "Turn off electronics after usage."
    elif (sug == 6):
         sheesh = "Buy solar panels for your house."
    elif (sug == 7):
         sheesh = "Recycle more of your waste."
    elif (sug == 8):
         sheesh = "Use the bathroom less."
    elif (sug == 9):
         sheesh = "Buy an electric stove."
    elif (sug == 10):
         sheesh = "Switch to a smart central heating system."
    elif (sug == 11):
         sheesh = "Don't use the air conditioning in summer."
    elif (sug == 12):
         sheesh = "Don't use the heater in the winter."
    elif (sug == 13):
         sheesh = "Use less electronic devices in the day."
    elif (sug == 14):
         sheesh = "Walk to nearby places."
    elif (sug == 15):
         sheesh = "Use better lightbulbs."
    
    
	


    






    score = score
    return render_template("hi.html", score = score, sheesh = sheesh)

