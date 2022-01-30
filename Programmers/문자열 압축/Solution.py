def solution(s):
    answer = []
    list = slicer(s)
    for element in list:
        answer.append(counter(element))
    return min(answer)

def slicer(string):
    list = []
    for index in range(1, len(string)//2+2):
        element = []
        tempStr = string
        while len(tempStr):
            element.append(tempStr[0:index])
            tempStr=tempStr[index:]
        list.append(element)
    return list

def counter(list):
    unit = len(list[0])
    count=1
    length=0
    for index in range(0, len(list)-1):
        if list[index] == list[index+1]:
            count+=1
        else:
            if count!=1:
                length+=len(str(count))
            length += unit
            count=1
    length += (len(list[-1]))
    if count!=1:
        length+=len(str(count))
    return length