#method overloading
def sum(w,r):
    print("The sum of", w, "and", r, "is", w + r)
def sum(w, r, t):
    print("The sum of", w, ",", r, "and", t, "is", w + r + t)
    
sum(5, 10)  # This will call the first sum function
sum(5, 10, 15)  # This will call the second sum function
    