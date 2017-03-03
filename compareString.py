#-*-coding=utf-8-*-
__author__ = 'xda'
'''
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

 注意事项

在 A 中出现的 B 字符串里的字符不需要连续或者有序。

您在真实的面试中是否遇到过这个题？ Yes
样例
给出 A = "ABCD" B = "ACD"，返回 true

给出 A = "ABCD" B = "AABC"， 返回 false
'''
def compareString(A,B):
    if 0==len(A):
        return True

    if len(A)!=0 and len(B)==0:
        return False


    for i in A:
        if i not in B:
            return False

    return True

A="A"
B=""


print compareString(A,B)