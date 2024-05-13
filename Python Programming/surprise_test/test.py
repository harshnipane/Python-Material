#steps:
#take all opening brackets in dict as keys
#take all closing brackets in dict as values

def valid_bracket(s):
    dict = {'(' : ')', '[' : ']', '{' : '}','<':'>'}
    s1=""
    for i in s:
        if(i in dict.keys() or i in dict.values()):
            s1 += i
    print(s1)        
    stack = []
    if len(s1) == 1:
        if(s1[0] in dict.values()):
            return "left side bracket missing"
        else:
            return "right side bracket missing"
    for i in s1:
        if(i in dict.keys()):
            stack.append(i)
        else:
            if stack == []:
                return "left side bracket missing"
                break
            a = stack.pop()
            if i!= dict[a]:
                return "right side bracket missing"
    if(stack == []):
        return "All Good"  

s =  "{(1+2+3)}+6}"
ot = valid_bracket(s)
print(ot)                

            


