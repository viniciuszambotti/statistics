'''
Task 
Given an array,X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3).
It is guaranteed that Q1, Q2, and Q3  are integers.
'''

l = [3,7,8,5,12,14,21,13,18]



def median(l):
    l.sort()
    l_len = len(l)

    if l_len % 2 ==0:
        m1 = l[l_len // 2]
        m2 = l[l_len // 2 - 1]
        median = (m1 + m2)/ 2
    else:
        median = l[l_len // 2]

    return int(median)


q2_median = median(l)

q1_median = median([x for x in l if x < q2_median])

q3_median = median([x for x in l if x > q2_median])

print(q1_median)
print(q2_median)
print(q3_median)
