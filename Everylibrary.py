
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import glob
import csv


# In[ ]:

reviews = pd.read_csv("/Users/annettechiu/Downloads/CA_1998.csv")


# In[ ]:

csvfiles = glob.glob()


# In[5]:

reviews.head()


# In[6]:

reviews.LOCGVT.describe()


# In[7]:

reviews.LOCGVT.count()


# In[9]:

import glob, os


# In[10]:

path = os.getcwd()
files = os.listdir(path)
files


# In[3]:

ca_1998 = pd.read_csv("/Users/annettechiu/Desktop/CASample/CA_1998.csv")
ca_1999 = pd.read_csv("/Users/annettechiu/Desktop/CASample/CA_1999.csv")
ca_2000 = pd.read_csv("/Users/annettechiu/Desktop/CASample/CA_2000.csv")


# In[4]:

ca_1998.head()
ca_1999.head()
ca_2000.head()


# In[ ]:



