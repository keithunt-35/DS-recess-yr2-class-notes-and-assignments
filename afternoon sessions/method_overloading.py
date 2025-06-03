#method overloading

# focus on dispatch

from multiple_dispatch import dispatch
@dispatch(int, int, int)

def sum(w,r):
    print("The sum of", w, "and", r, "is", w + r)
    
@dispatch(float)    
def sum(w, r, t):
    print("The sum of", w, ",", r, "and", t, "is", w + r + t)
    
sum(5, 10)  # This will call the first sum function
sum(5, 10, 15.5)  # This will call the second sum functionju 

#same number of decisional parameters
    
    
    
#pip
#prefered installer programm
#helps you install python packages
#standard package manager for python

#how to install pip
#pip install <package_name>

