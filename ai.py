import pandas
import numpy
from sklearn.tree import DecisionTreeClassifier
#"buy an electric vehicle"	
#"turn off all the lights"	
#"take shorter showers"	
#"carpool or use public transport"	
#"turn off electronics after usage"	
# "buy solar panels for your house"	
# "recycle more of your waste"	
# "use the bathroom less"	
# "buy an electric stove"	
# "switch to a smart central heating system"	
# "don't use the air conditioning in summer"	
# "don't use the heater in the winter"	
# "use less electronic devices in the day"	
# "walk to nearby places"	
# "use better lightbulbs (LEDs)"	

df = pandas.read_csv('LuminosityData - Sheet1.csv')
X = df.drop(columns=['Suggestions'])
Y = df['Suggestions']
 model = DecisionTreeClassifier()
 model.fit(X,Y)
 predictions = model.predict([[]])
 predictions

