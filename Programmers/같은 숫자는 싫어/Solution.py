def solution(arr):
    a=[]
    b=-1
    for i in range(len(arr)):
        if i > 0:
            b=arr[i-1]
        if arr[i] is not b:
            a.append(arr[i])
    return a