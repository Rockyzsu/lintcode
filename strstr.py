#-*-coding=utf-8-*-
__author__ = 'xda'
def strstsrQ(source,target):
    for s in range(len(source)):
        cur=0
        for t in range(len(target)):
            if s+t>=len(source):
                return -1

            if target[t] == source[t+s]:
                cur=cur+1
            else:
                break
            if cur==(len(target)-1):
                return s

    return -1


a='I like China!'
b='China'
c='adcde'
d='e'
print strstsrQ(c,d)
