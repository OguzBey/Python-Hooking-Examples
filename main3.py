class BaseModel(object):

    def save(self):
        print('Saved !')


class MyBaseModel(BaseModel):

    # override
    def save(self):

        for key, value in vars(self).items():
            
            if value is None:

                if type(vars(type(self))[key]) == str:
                    vars(self)[key] = "Turkey"
                
                elif type(self.__class__.__dict__[key]) == int:
                    self.__dict__[key] = 1111
                
                elif type(vars(self.__class__)[key]) == bool:
                    vars(self)[key] = True
                
                else: pass
        
        return super(MyBaseModel, self).save() # call parent class save method


class Person(MyBaseModel):

    country = "" # Field 1
    age = 0 # Field 2
    is_alive = False # Field 3


p = Person()

p.country = None
p.age = None
p.is_alive = None

p.save()

print(p.country)
print(p.age)
print(p.is_alive)



