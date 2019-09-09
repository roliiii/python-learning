#http://www.pythonchallenge.com/pc/return/bull.html
#a = [1, 11, 21, 1211, 111221, 
#len(a[30])=?

def lookAndSay(nth = 1):
    if(nth == 1):
        return '1'
    elif(nth == 2):
        return '11'

    prevSeqItem='11'
    counter=0
    for i in range(3,nth+1):
        prevSeqItem = prevSeqItem + ' '
        actSeqItem=''
        for j in range(len(prevSeqItem)-1):
            counter += 1
            if(prevSeqItem[j] != prevSeqItem[j+1]):
                actSeqItem=actSeqItem + str(counter) + prevSeqItem[j]
                counter=0 
        prevSeqItem = actSeqItem
    return prevSeqItem

print(len(lookAndSay(31)))
#5808