import pickle

#http://www.pythonchallenge.com/pc/def/peak.html
something = pickle.load(open('pythonChallange\\banner.p', 'rb'))
for row in something:
    for column in row:
        print(column[0]*column[1], end = '')
    print('')