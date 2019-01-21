class Person():
    species = 'Human'
print(Person.species) # Human
Person.alive = True  # Added dynamically!
print(Person.alive) # True
man = Person()
print(man.species) # Human (inherited)
print(man.alive) # True (inherited)
Person.alive = False
print(man.alive) # False (inherited)
man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)  # Darth Vader

# class는 instance의 변화에 영향을 받지 않는다.
# instance는 class의 변화에 영향을 받는다.
