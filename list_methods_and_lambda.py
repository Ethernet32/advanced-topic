from functools import reduce
mylist = [ 4, 6, 8, 1.5, 5, 10, 7]
newlist = ["", "Argentina", "", "Brazil","", "Chile","","Colombia", "", "Ecuador", "", "Venezela"]
 
def increase(num):
    return num+1

def multiple(num):
    if num % 3 == 0:
        return num
#print(list(map(increase, mylist)))
#lamda is for one line funtions Use for one line conditional. Do not use for long complicated functions
#print(list(filter(lambda num: num % 3==0, mylist)))
#Be careful when using none as a filter because it also removes Zeros
#print(list(filter(None, newlist)))
multiplier = lambda x, y: x*y

print(reduce(multiplier, mylist))