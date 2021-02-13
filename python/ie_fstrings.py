#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2

#   %-formatting
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
output_str = "Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation)
print(output_str)
print()

#   str.format()
name = "Eric"
age = 74
print("Hello, {}. You are {}.".format(name, age))
print("Hello, {1}. You are {0}.".format(age, name))
print("Hello, {name}. You are {age}.".format(name=name, age=age))
person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(**person))
print()

#   f-strings (python3.6+)
print(f"Hello, {name}. You are {age}.")
print(f"{2 * 37}")

def to_lowercase(input):
    return input.lower()
name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")
print(f"{name.lower()} is funny.")
print()

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")
print(f"{new_comedian!r}")
print()

print(f'{"Eric Idle"}')
print(f"{'Eric Idle'}")
print()

comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")
print()

print(f"{{70 + 4}}")
print(f"{{{70 + 4}}}")
print(f"{{{{70 + 4}}}}")
print(f"{{{{{70 + 4}}}}}")
print()


#   }}}1
