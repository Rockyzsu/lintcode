#-*-coding=utf-8-*-
__author__ = 'xda'
'''
wrong alghim:
a='aac'
b='acc'
def anagram(s,t):
    for i in s:
        if i not in t:
            return False
    return True
'''
a='abcc'
b='cba'
c='aaa'

def anagram(s,t):
    s=list(s)
    t=list(t)
    print s
    print t
    #x= s.pop()
    if len(s)!=len(t):
        return False
    while s :

        x=s.pop()
        if x in t:
            t.remove(x)

        if len(s)==0 and len(t)==0:
            return True


    return False

print anagram(a,b)