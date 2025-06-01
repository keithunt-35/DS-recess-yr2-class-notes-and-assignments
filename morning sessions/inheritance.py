#father motherr skills
class Father:
    def skills(self):
        print('Coding. fishing')
        
class Mother:
    def skills(self):
        print('Cooking, cleaning')
        
class Child(Father, Mother):
    # in order to use both t he methods, i define a method
    def skills(self):
        Father.skills(self)
        Mother.skills(self)


c = Child()
c.skills()