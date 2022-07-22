# data = "112ToI!device1#!device1:1:2:2##aa#aa!!!aaaa!::!device2:1:100:100#!device1:1:100:100#!device2:3:100,100,1:201#"
data = "!ID002:3:20,50,10:80#!aaabbb###!aaa@@1111!:2:!ID02:3:20,50,0:70#"


data = data.split('!')
arr = []


def lookupDevice(name, count):
    for ele in arr:
        if ele['name'] == name and ele['val_count'] == count:
            return True
        if ele['name'] == name and ele['val_count'] != count:
            return False
    return True


def validateData(string):
    sum = 0
    string = string.split(':')
    if len(string) == 4:
        if '#' in string[0]:
            string[0] = string[0].split('#')[0]
            print(string[0] + ' ' + 'error')
            return

        check_device = lookupDevice(string[0], int(
            string[1])) if string[1].isnumeric() else False
        if not check_device:
            print(string[0] + ' ' + 'error')
            return

        string[3] = string[3].split('#')[0]
        if string[0] and string[0][0].isalpha() and string[0][len(string[0]) - 1].isnumeric():
            pass
        else:
            if not string[0]:
                print('error')
            else:
                print(string[0] + ' ' + 'error')
            return False

        listValue = string[2].split(',') if string[2] != '' else []
        if string[1].isnumeric():
            if int(string[1]) != len(listValue):
                print(string[0] + ' ' + 'error')
                return False
        else:
            print(string[0] + ' ' + 'error')
            return False

        for i in listValue:
            if i[0] == '-':
                if not i[1:].isnumeric():
                    print(string[0] + ' ' + 'error')
                    return False
            else:
                if not i.isnumeric():
                    print(string[0] + ' ' + 'error')
                    return False
            sum += int(i)

        if string[3][0] == '-':
            if string[3][1:].isnumeric():
                if sum != int(string[3]):
                    print(string[0] + ' ' + 'error')
                    return False
            else:
                print(string[0] + ' ' + 'error')
                return False
        else:
            if string[3].isnumeric():
                if sum != int(string[3]):
                    print(string[0] + ' ' + 'error')
                    return False
            else:
                print(string[0] + ' ' + 'error')
                return False

        ele = {}
        ele['name'] = string[0]
        ele['val_count'] = len(listValue)
        arr.append(ele)

        return True
    else:
        if string[0] == '' or string[0][0] == '#':
            print('error')
        elif string[0] != '':
            if string[0][0] == '#':
                return False
            print(string[0].split('#')[0] + ' ' + 'error')
        return False


idx = 1
if data[0] == '' and data[1] != '':
    if data[1][0] != '#':
        if not ':' in data[1]:
            print(data[1].split('#')[0] + ' ' + 'error')
            idx = 2

for i in data[idx:]:
    temp = i[:-1].split(':')
    flag = validateData(i)
    if flag:
        print('client.sent(' + temp[0] + ',' + temp[2] + ')')
