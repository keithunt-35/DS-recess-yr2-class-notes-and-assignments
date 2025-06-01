#object oriented programming(00p)
#contains data in form of attributes

#class and object
#a class is a blue print for creating objects 
#an object is an instance of a class

#key principles

#************inheritance*************
#example 1: inheritence

#super class: base class, parent class.
class Animal:
    def speak(self):
        print('Animal makes a sound')

#sub class: derived class, child class.
class Cat (Animal):
    def sound(self):
        print('cat makes a souund meoeeewww')

#crearing an object of the cat
cat1 = Cat()

#callmg the inherited method
cat1.speak()
#calling its own method
cat1.sound()




#******************polymorphism*****************
#allows objects of diff classes behave like they are from one class 

#parent
class Bird():
    def fly(self):
        print("birds fly in the sky")
        
class Eagle(Bird):
    def fly(self):
        print("eagle flies at a very hight altitude")
        
class Sparrow(Bird):
    def fly(self):
        print('Saprrow flies at a low altitube')
        
        
#how we use polymorphism
def flight_test(Bird):
    Bird.fly() #run respecrive class methid based in an object
    
    
#crearint the objects
eagle1 = Eagle()
sparrow1 = Sparrow()

#calling the flight test method with different objects

flight_test(eagle1)

#method overriding and method over loading



#************abstraction*****************
# aclass that contains one or more methods

#class and interfaces
#uses the symbol @ 
#import the ABc anf the abstract method formthe abc module
from abc import ABC, abstractmethod #abstraction

#starting an car engine and a bike

#define an abstract class

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # this method,start, has no implementatin

#child cass implementin the abstract method
class Car(Vehicle):
    def start(self):
        print('car engine started')
        
        
#derived class implementing an abstract method
class Bike(Vehicle):
    def start(self):
        print("bike engine starts")

#notes
#we canot create object of an abstracr class
#demo live
#vehicle1 = Vehicle() #this would raise an error cannot instantialte an abstract class vehicle without an  implementation for the abstracr method start

#the accepted version is:: create object of the subclass

car1 = Car()
bike1 = Bike()

#display output if the methods
car1.start()
bike1.start()


#encapsulation

