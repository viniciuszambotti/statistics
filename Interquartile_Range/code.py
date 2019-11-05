'''
Task 
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e.,Q3 - Q1 ).
Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, 
construct a data set,S, where each x1 occurs at frequency f1. Then calculate and print S's interquartile range, 
rounded to a scale of 1 decimal place (i.e.,12.3  format).
'''

def median(list):
    if len(list)%2 == 0:
        median = (list[(len(list)//2)]+list[(len(list)//2-1)])/2
    else:
        median = list[(len(list)//2)]
    return(median)

X = [6,12,8,10,20,16]
F = [5,4,3,2,1,5]
S=[]
for i in range(len(X)):
    S += [X[i]] * F[i]
S.sort()
Q1, Q2, Q3 = median(S[:(sum(F)//2)]), median(S), median(S[(sum(F)//2):] if len(S)%2==0 else S[(1+sum(F)//2):])

print("{0:0.1f}".format(Q3-Q1))
