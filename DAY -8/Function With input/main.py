# def greet():
#      print("Hello ")
#      print("How are you ?")
#      print("Isn't the Weather nice Today ?")
        
# greet()

def greet_with_name(name):
    print(f"Hello {name} ")
    print(f"How are you ? {name} ")
    print(f"Isn't the Weather nice Today ? {name} ")
    
greet_with_name("Saimon")


def greet_with_name(name,location):
    print(f"Hello {name} ")
    print(f"How are you ? {name} ")
    print(f"Isn't the Weather nice Today ? {name} ")
    print(f"How is it like to be in  {location} ?")
greet_with_name(name = "Shamirul" , location = "London")