from operator import attrgetter
li = (9,1,8,2,7,3,6,4,5)
slist = sorted(li)
#slist = sorted(li, reverse=True)
#print(slist)

di = {"name":"Tina", "job":"Sales", "age":28, "os":"Mac"}

sdi = sorted(di)
print(f"Dictionary:\t{sdi}")

class Employee:
    def __init__(self,name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return "({},{},${})".format(self.name,self.age,self.salary)
    
e1 = Employee("Carl",37,700000)
e2 = Employee("Sarah",29,800000)
e3 = Employee("John", 43,900000)
def e_sort(employee):
    return employee.name

employees = [e1, e2, e3]

s_employees = sorted(employees, key = attrgetter("age"), reverse=True)

print(s_employees)