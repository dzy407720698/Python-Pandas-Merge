
# coding: utf-8

# In[18]:

import pandas as pd
import numpy as np


# In[25]:

data92 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/1992.csv')
data93 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/1993.csv')
data92


# In[27]:

data93


# In[37]:

data = None
filelist = ['/Users/annettechiu/Desktop/USA_csv/1992.csv','/Users/annettechiu/Desktop/USA_csv/1993.csv','/Users/annettechiu/Desktop/USA_csv/1994.csv','/Users/annettechiu/Desktop/USA_csv/1995.csv','/Users/annettechiu/Desktop/USA_csv/1996.csv','/Users/annettechiu/Desktop/USA_csv/1997.csv','/Users/annettechiu/Desktop/USA_csv/1998.csv','/Users/annettechiu/Desktop/USA_csv/1998.csv','/Users/annettechiu/Desktop/USA_csv/1999.csv','/Users/annettechiu/Desktop/USA_csv/2000.csv','/Users/annettechiu/Desktop/USA_csv/2001.csv','/Users/annettechiu/Desktop/USA_csv/2002.csv','/Users/annettechiu/Desktop/USA_csv/2003.csv','/Users/annettechiu/Desktop/USA_csv/2004.csv','/Users/annettechiu/Desktop/USA_csv/2005.csv','/Users/annettechiu/Desktop/USA_csv/2006.csv','/Users/annettechiu/Desktop/USA_csv/2007.csv','/Users/annettechiu/Desktop/USA_csv/2008.csv','/Users/annettechiu/Desktop/USA_csv/2009.csv','/Users/annettechiu/Desktop/USA_csv/2010.csv','/Users/annettechiu/Desktop/USA_csv/2011.csv','/Users/annettechiu/Desktop/USA_csv/2012.csv','/Users/annettechiu/Desktop/USA_csv/2013.csv','/Users/annettechiu/Desktop/USA_csv/2014.csv','/Users/annettechiu/Desktop/USA_csv/2015.csv','/Users/annettechiu/Desktop/USA_csv/2016.csv']
for f in filelist:
    if data is None:
        data = pd.read_csv(f, index_col='LIBNAME')
    else:
        data = pd.merge(data,pd.read_csv(f))
        print data
        


# In[37]:

data = None
filelist = ['/Users/annettechiu/Desktop/USA_csv/1992.csv','/Users/annettechiu/Desktop/USA_csv/1993.csv','/Users/annettechiu/Desktop/USA_csv/1994.csv','/Users/annettechiu/Desktop/USA_csv/1995.csv','/Users/annettechiu/Desktop/USA_csv/1996.csv','/Users/annettechiu/Desktop/USA_csv/1997.csv','/Users/annettechiu/Desktop/USA_csv/1998.csv','/Users/annettechiu/Desktop/USA_csv/1998.csv','/Users/annettechiu/Desktop/USA_csv/1999.csv','/Users/annettechiu/Desktop/USA_csv/2000.csv','/Users/annettechiu/Desktop/USA_csv/2001.csv','/Users/annettechiu/Desktop/USA_csv/2002.csv','/Users/annettechiu/Desktop/USA_csv/2003.csv','/Users/annettechiu/Desktop/USA_csv/2004.csv','/Users/annettechiu/Desktop/USA_csv/2005.csv','/Users/annettechiu/Desktop/USA_csv/2006.csv','/Users/annettechiu/Desktop/USA_csv/2007.csv','/Users/annettechiu/Desktop/USA_csv/2008.csv','/Users/annettechiu/Desktop/USA_csv/2009.csv','/Users/annettechiu/Desktop/USA_csv/2010.csv','/Users/annettechiu/Desktop/USA_csv/2011.csv','/Users/annettechiu/Desktop/USA_csv/2012.csv','/Users/annettechiu/Desktop/USA_csv/2013.csv','/Users/annettechiu/Desktop/USA_csv/2014.csv','/Users/annettechiu/Desktop/USA_csv/2015.csv','/Users/annettechiu/Desktop/USA_csv/2016.csv']
for f in filelist:
    if data is None:
        data = pd.read_csv(f, index_col='LIBNAME')
    else:
        data = pd.merge(data,pd.read_csv(f))
        print data
        


# In[38]:

data.to_csv('Big.csv')


# In[28]:




# In[13]:

data = None
filelist = ['/Users/annettechiu/Desktop/USA_csv/1992.csv','/Users/annettechiu/Desktop/USA_csv/1993.csv','/Users/annettechiu/Desktop/USA_csv/1994.csv']
for f in filelist:
    if data is None:
        data = pd.read_csv(f, index_col='LIBNAME')
    else:
        data = data.join(pandas.read_csv(f, index_col='LIBNAME'))


# In[ ]:



