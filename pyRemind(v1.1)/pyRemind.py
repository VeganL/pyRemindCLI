import os

action = 0
newItm = ''
lnNum = -1
chDt = -1
toMod = -1
l = []
L = []
i = 1


print('pyRemind v1.1 (by Vegan Lroy)')
print('=================================')
print()
print('### Date Due  What is Due/To Be Done')
print('=== ========  =======================')

# Section for list
with open('list.txt', mode = 'r') as read:
    for line in read:
        l = line.split('  ')
        if l[0] == '--------':
            l[0] = int(99999999)
        l[0] = int(l[0])
        L.append(l)
    L.sort()
for item in L:
    print('%3d' % i, end = ' ')
    for x in range(0,len(item)):
        if x == 0:
            if item[x] == 99999999:
                print('--------', end = '  ')
            else:
                print(item[x], end = '  ')
        if x == 1:
            print(item[x], end = '')
    i += 1

# Main code starts here
term = 0
while term != 1:
    foo = 0
    while foo != 1:
        print('\nSelect action:\n 1) New item\n 2) Change item\n 3) Delete item\n 4) Exit')
        rawAction = input('\nEnter action selection number here: ')
        try:
            action = int(rawAction)
            foo = 1
        except:
            print('ERROR: PLEASE ENTER A NUMBER.\n')

    # NEW ITEM
    if action == 1:
        newItm = input('Enter new "thing to do":\n')
        newItm = newItm + '\n'
        elfHalf = 0
        while elfHalf != 1:
            dueDateRaw = input('Enter due date in YYYYMMDD format (leave blank if no due date): ') + '\n'
            if dueDateRaw == '\n':
                dueDate = 99999999
                elfHalf = 1
            elif dueDateRaw != '\n':
                if len(dueDateRaw) == 9:
                    try:
                        dueDate = int(dueDateRaw)
                        elfHalf = 1
                    except:
                        print('ERROR: PLEASE ENTER A DATE IN YYYYMMDD FORMAT.\n')
                else:
                    print('ERROR: PLEASE ENTER A DATE IN YYYYMMDD FORMAT.\n')
                    
                    
        # Code for adding input to list.txt
        l = [dueDate, newItm]
        L.append(l)
        L.sort()
        i = 1
        print()
        print('### Date Due  What is Due/To Be Done')
        print('=== ========  =======================')
        for item in L:
            print('%3d' % i, end = ' ')
            for x in range(0,len(item)):
                if x == 0:
                    if item[x] == 99999999:
                        print('--------', end = '  ')
                    else:
                        print(item[x], end = '  ')
                if x == 1:
                    print(item[x], end = '')
            i += 1
            with open('listTmp.txt', mode = 'w') as edit:
                for item in L:
                    if item[0] == 99999999:
                        output = str('--------  ' + item[1])
                        edit.write(output)
                    else:
                        output = str(str(item[0]) + '  ' + item[1])
                        edit.write(output)
        os.remove('list.txt')
        os.rename('listTmp.txt', 'list.txt')

    #CHANGE ITEM
    elif action == 2:
        elf = 0
        while elf != 1:
            lnNumRaw = input('Enter item element number to change: ')
            try:
                lnNum = int(lnNumRaw)
                elf = 1
            except:
                print('ERROR: PLEASE ENTER A NUMBER.\n')
        elf = 0
        while elf != 1:
            toModRaw = input('Choose what you want to modify\n 1) Due Date\n 2) What is Due/To Be Done\n Enter selection here: ')
            try:
                toMod = int(toModRaw)
                dummy = 1 + 1
            except:
                print('ERROR: PLEASE ENTER A NUMBER.\n')
            if toMod == 1 or toMod == 2:
                elf = 1
            else:
                print('ERROR: PLEASE ENTER A VALID SELECTION.\n')
        elfHalf = 0
        while elfHalf != 1:
            if toMod == 1:
                dueDateRaw = input('Enter new Due Date in YYYYMMDD format (leave blank for no due date: ') + '\n'
                if dueDateRaw == '\n':
                    chDt = 99999999
                    elfHalf = 1
                elif dueDateRaw != '\n':
                    if len(dueDateRaw) == 9:
                        try:
                            chDt = int(dueDateRaw)
                            elfHalf = 1
                        except:
                            print('ERROR: PLEASE ENTER A DATE IN YYYYMMDD FORMAT.\n')
                    else:
                        print('ERROR: PLEASE ENTER A DATE IN YYYYMMDD FORMAT.\n')
                L[lnNum-1][toMod-1] = chDt
            elif toMod == 2:
                chLn = input('Enter modified "thing to do":\n') + '\n'
                L[lnNum-1][toMod-1] = chLn
                elfHalf = 1
        L.sort()
        i = 1
        print()
        print('### Date Due  What is Due/To Be Done')
        print('=== ========  =======================')
        for item in L:
            print('%3d' % i, end = ' ')
            for x in range(0,len(item)):
                if x == 0:
                    if item[x] == 99999999:
                        print('--------', end = '  ')
                    else:
                        print(item[x], end = '  ')
                if x == 1:
                    print(item[x], end = '')
            i += 1
            with open('listTmp.txt', mode = 'w') as edit:
                for item in L:
                    if item[0] == 99999999:
                        output = str('--------  ' + item[1])
                        edit.write(output)
                    else:
                        output = str(str(item[0]) + '  ' + item[1])
                        edit.write(output)
        os.remove('list.txt')
        os.rename('listTmp.txt', 'list.txt')

    # DELETE ITEM
    elif action == 3:
        elf2 = 0
        while elf2 != 1:
            lnNumRaw = input('Enter item element number for deletion: ')
            try:
                lnNum = int(lnNumRaw)
                elf2 = 1
            except:
                print('ERROR: PLEASE ENTER A NUMBER.\n')
        # Code for deleting line of line number specified in list.txt
        L.pop(lnNum-1)
        L.sort()
        i = 1
        print()
        print('### Date Due  What is Due/To Be Done')
        print('=== ========  =======================')
        for item in L:
            print('%3d' % i, end = ' ')
            for x in range(0,len(item)):
                if x == 0:
                    if item[x] == 99999999:
                        print('--------', end = '  ')
                    else:
                        print(item[x], end = '  ')
                if x == 1:
                    print(item[x], end = '')
            i += 1
            with open('listTmp.txt', mode = 'w') as edit:
                for item in L:
                    if item[0] == 99999999:
                        output = str('--------  ' + item[1])
                        edit.write(output)
                    else:
                        output = str(str(item[0]) + '  ' + item[1])
                        edit.write(output)
        os.remove('list.txt')
        os.rename('listTmp.txt', 'list.txt')

    # EXIT
    elif action == 4:
        term = 1
    else:
        print('ERROR: PLEASE ENTER VALID SELECTION\n')
