#Decorators have the @ symbol before them
def cough(function):
    def function_wrapper():
        #stf that hapens before the function
        print("*cough*")
        function()
        #any stuff that happns after our function
        print("*cough*")
    return function_wrapper



@cough
def awkward():
    print("Can I get a discount?")

@cough
def answer():
    print("Sir this is a dolar tree. . .")

awkward()
answer()