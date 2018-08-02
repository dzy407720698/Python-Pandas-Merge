# Python-Pandas-Merge
import pandas as pd 
import os
dflist=[]
for f in os.listdir('/Users/annettechiu/Desktop/USA_csv'): 
    path = '/Users/annettechiu/Desktop/USA_csv/{}'
    df = pandas.read_csv(path.format(f),encoding='big5')
    print df
