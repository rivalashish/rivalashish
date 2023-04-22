"""
###### Single underscores ######

1.  A single leading underscore in front of a variable, a function,
or a method name means that these objects are used internally.
    This is more of a syntax hint to the programmer and is not enforced by the Python interpreter ,
which means that these objects can still be accessed in one way on another from another script.
    However, there’s a situation where a variable that has a leading underscore cannot be accessed directly,
possible if module is imported and then variable is called..--Private Variable


2.  A Single trailing underscores : There are some situations where you want to use a variable name that is actually
a reserved keyword in Python such as class, def , type , object , etc.
    To avoid this conflict, you can add a trailing underscore as a naming convention.

3.  A Single underscores : To define temporary or unused variables.

###### Double underscores ######

1.  Double leading and trailing underscores are used to define special universal class methods called
dunder methods (short for Double Underscore methods).
    Dunder methods are reserved methods that you can still overwrite.
They have special behavior and are called differently. For example:
    __init__ is used as a constructor of the class
    __call__ is used to make the object callable
    __str__ is used to define what’s printed on the screen when we pass the object to the print function.
As you see, Python introduces this naming convention to differentiate between the module’s core methods and
the user-defined ones.

 """
