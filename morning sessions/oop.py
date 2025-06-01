#object oriented programming(00p)
#contains data in form of attributes

#class and object
#a class is a blue print for creating objects 
#an object is an instance of a class

#key principles

#inheritance
#super class: base class, parent class.
#sub class: derived class, child class.

#example 1: inheritence

#super class
class Animal:
    def speak(self):
        print('Animal makes a sound')

#sub class
class Cat (Animal):
    def sound(self):
        print('cat makes a souund meoeeewww')

#crearing an object of the cat
cat1 = Cat()

#callmg the inherited method
cat1.sound()


#polymorphism 


#method overriding and method over loading



#abstraction



#encapsulation

