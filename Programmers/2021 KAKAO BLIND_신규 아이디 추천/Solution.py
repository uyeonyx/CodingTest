import string
def solution(new_id):
    def process1(str):
        return str.lower()
    def process2(str):
        filt=[i for i in string.ascii_lowercase]+['0','1','2','3','4','5','6','7','8','9']+['-','_','.']
        return "".join([x for x in str if x in filt])
    def process3(str):
        ret = []
        flag = False
        for s in str:
            if s!='.':
                flag=False
                ret.append(s)
            else:
                if flag == True:
                    continue
                flag=True
                ret.append(s)
        return "".join(ret)
    def process4(str):
        ret=str
        if str[0] =='.':
            ret = ret[1:]
        if str[-1]=='.':
            ret = ret[0:-1]
        return ret
    def process5(str):
        if str=="":
            return "a"
        return str
    def process6(str):
        ret=str
        if len(str)>15:
            ret = ret[0:15]
        if ret[-1]=='.':
            ret = ret[0:-1]
        return ret
    def process7(str):
        ret=str
        if len(ret)<3:
            last=ret[-1]
            while len(ret)<3:
                ret=ret+last
        return ret
    answer=process1(new_id)
    answer=process2(answer)
    answer=process3(answer)
    answer=process4(answer)
    answer=process5(answer)
    answer=process6(answer)
    answer=process7(answer)
    return answer
