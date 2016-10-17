#How Local and Global Vaiables work.
#This variable can be accessed by this entire script.
global_var = "I am a global variable"

def a_function():
    #Variable can only be accessed within this function
    #Could also use Global keyword e.g. Global local_var
    #global local_var
    local_var = "I am a local variable"
    return local_var

#when using glboal I will need to call the function to print the variable.
print(global_var)
print(local_var)

#A function is not attached to an object.
#function(argument_0), e.g. print().

#A method is a function attached to an object.
#object.method(argument_0, argument_1).
