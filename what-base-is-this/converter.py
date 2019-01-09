
def bta(text):
    list_text = text.split(" ")
    ans =""
    for c in list_text:
        ans+=chr(int(c,2))
    return ans

def hta(text):
    ans=""
    lst = stl(text)
    for c in lst:
        ans+=chr(int(c,16))
    return ans

def dta(text):
    ans=""
    lst= text.split(" ") 
    for c in lst:
        ans+=chr(int(c,10))
    return ans

def ota(text):
    ans=""
    lst=text.split(" ")
    for c in lst:
        ans+=chr(int(c,8))
    return ans

def stl(string):
    tmp=""
    lst=[]
    for c in string:
        tmp+=c
        if len(tmp)==2:
            lst.append(tmp)
            tmp=""
    return lst
