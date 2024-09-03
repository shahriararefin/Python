list = ["why are you here?"]

def stringOddorEven(string):
    """
    Purpose: 
    """
    for i in string:
        if(len(i)%2==0):
            print("even", len(i))
        else:
            print("odd", len(i))
# end def

stringOddorEven(list)