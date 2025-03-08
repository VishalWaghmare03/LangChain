from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'vishal','age':'23'}

print(new_person)




##### simple TypedDict
##### Annotated TypeDict --> give instruction for each value for don't model give wrong answer. 
##### Literal  --> only give the specific output ex. positive or negative
##### optional --> If the specific information is available then only show, else don't response this variable.
##### More Complex -> pros and cons