'''
Given an array,X, ofN integers and an array,W , representing the respective weights of X's elements, calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e.,12.3 format).
'''

x = [10,40,30,50,20]
w = [1,2,3,4,5]

max_w = sum(w)

t = list(zip(x,w))

count = 0
for x, w in t:
    count = count + (x*w)

print(format((count / max_w),'.1f'))

