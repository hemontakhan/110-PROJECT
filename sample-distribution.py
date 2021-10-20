from typing import Counter
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

reader = pd.read_csv('article.csv')


def random_set_of_mean(counter):
    dataset = []
    for a in range(0,counter) : 
     random_index = random.randint(0,len(reader))
     value = reader[random_index]
     dataset.append(value)
    
    mean = statistics.mean(dataset)
    print('Mean of the Data is:-',mean)
    return mean

def setup():
    mean_list = []
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)
    show_fig(mean_list)


def show_fig(mean_list):
    data_file = mean_list
    chart = ff.create_distplot([data_file],['responses'],show_hist=False)
    chart.show()