#exception handling
try:
    raise IndexError
except IndexError:
    print("The program produces IndexError")
finally:
    print("Program finished")
#end of code