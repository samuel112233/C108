import csv
import pandas as pd 
import plotly.figure_factory as ff 
import random


diceResult=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
fig=ff.create_distplot([diceResult],['result'])
fig.show()