class BaseModel(object):
    
    def save(self):
        print("Saved !")


class Person(BaseModel):

    country = ""
    age = 0
    is_alive = False


def on_save(save_function):
    def run(*args, **kwargs):
        self = args[0]
        
        for key, value in vars(self).items():
            if value is None:

                if type(vars(type(self))[key]) == str:
                        vars(self)[key] = "Turkey"
                    
                elif type(self.__class__.__dict__[key]) == int:
                    self.__dict__[key] = 1111
                
                elif type(vars(self.__class__)[key]) == bool:
                    vars(self)[key] = True
                
                else: pass
        
        return save_function(*args, **kwargs)

    return run

BaseModel.save = on_save(BaseModel.save) # BaseModel.save ? Person.save ?

p = Person()

p.country = None
p.age = None
p.is_alive = None

p.save()

print(p.country)
print(p.age)
print(p.is_alive)