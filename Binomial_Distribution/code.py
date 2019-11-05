'''
Task
The ratio of boys to girls for babies born in Russia is 1.09: 1 .
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).
'''

import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += bi_dist(i, n, p)
print("%.3f" %b)

