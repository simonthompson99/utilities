# function to quickly generate frequency table from list of items on clipboard
from collections import Counter
from xerox import copy, paste
from re import split

# get data from clipboard
def getClipboardData():
    return paste()

# send data to clipboard
def setClipboardData(data):
    copy(data)

# make intro to program
def hello():
    print("-" * 61)
    print("#-" * 13 + " QUICKTAB " + "#-" * 13)
    print("-" * 61)
    print("." * 61)

# split the data which comes in as a long string with linebreaks into separate list elements
# removes quotes and tabs from either side of string too
def splitData(string, delim):
    l = split(delim, string)
    return list(filter(None, [o.strip(' \r\n\t"\',') for o in l]))

# prints a little preview of a list
def prListHead(data, nrows):
    print(str(len(data)) + " rows read from clipboard:")
    print('\n'.join(data[0:nrows]))
    print('...')

# makes a frequency table of an input list of data, most common elements at top of table
def freqTab(data):
    d = Counter(data)
    return d.most_common(len(d))

# writes out the table from freqTab to clipboard
def formatTab(l):
    return 'value\tcount\n'+'\n'.join(['\t'.join(str(j) for j in i) for i in l])

# sequence of events
def process():
    a = splitData(getClipboardData(), '\r|\n')
    prListHead(a, 10)
    t = formatTab(freqTab(a))
    print("-" * 61)
    print("#-" * 13 + " RESULTS " + "#-" * 13)
    print("-" * 61)
    print(t)
    setClipboardData(t)
    print("Table written to clipboard")

# function to check whether we want to continue
def carryOn():
    while True:
        choice  = input("Ready for another? y/n: ").upper()
        if choice not in ('Y', 'N'):
            print("Invalid entry, y or n please")
        if choice == 'Y':
            input("Copy new data to clipboard then press <Enter>")
            return True
        if choice == 'N':
            quit()

while True:
    hello()
    process()
    carryOn()
