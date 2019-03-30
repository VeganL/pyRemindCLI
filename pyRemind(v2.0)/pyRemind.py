#!/usr/bin/python
import cgi

def dispPg():
    print('Content-type:text/html\r\n\r\n')
    print('<!DOCTYPE html><html><title>pyRemind</title><head><style>h1{font-family:"Trebuchet MS", Helvetica, sans-serif; color:#ffffff; background: #1e5799; background: -moz-linear-gradient(top, #1e5799 0%, #207cca 69%, #2989d8 99%, #7db9e8 100%); background: -webkit-linear-gradient(top, #1e5799 0%,#207cca 69%,#2989d8 99%,#7db9e8 100%); background: linear-gradient(to bottom, #1e5799 0%,#207cca 69%,#2989d8 99%,#7db9e8 100%); filter: progid:DXImageTransform.Microsoft.gradient( startColorstr="#1e5799", endColorstr="#7db9e8",GradientType=0 ); text-align: center;} h2{font-family:"Trebuchet MS", Helvetica, sans-serif; text-align:center;} p{font-family:"Trebuchet MS", Helvetica, sans-serif; text-align: center;}</style><meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"></head><body>')
    print('<h1><br>pyRemind<br>by Vegan Lroy<hr></h1><form action="/cgi-bin/pyRemind.py" method="post">')
    with open('list.txt', mode = 'r') as data:
        L = []
        for line in data:
            l = line.split(';')
            if l[0] == '--------':
                l[0] == int(99999999)
            l[0] = int(l[0])
            L.append(l)
        L.sort()
        for i in range(0,len(L)):
            if L[i][0] == 99999999:
                date = '--------'
            else:
                date = str(L[i][0])

#        for item in L:
#            for i in item:
#                print('<input type="text" name="' + '" value="' + i + '">')
#            print('<br>')

    #Insert for loop section to display textboxes per item in list.txt
    print('</form></body>')

def chgLs():
    pass

dispPg()
