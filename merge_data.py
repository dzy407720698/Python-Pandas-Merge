data = None
filelist = ['CSV1.csv', 'otherfile.csv', ..., 'Lastfile.csv']
for f in filelist:
    if data is None:
        data = pandas.read_csv(f, index_col='A')
    else:
        data = data.join(pandas.read_csv(f, index_col='A'))

data.to_csv('Big.csv')