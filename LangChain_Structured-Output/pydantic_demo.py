from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # can pass default value
    name: str = 'Vishal'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa fo the student")


new_strudent = {'age':"23", 'email':'vishal@gmail.com'} #, 'cgpa':8.4

student = Student(**new_strudent)

student_dict = dict(student)  ## previous it's pydantic object can convert it to dict and JSON
student_json = student.model_dump_json()
print(student_dict['age'])
print(student_json)
# print(type(student))


## ** field function  ** ##
# default value 
# name='Vishal' age=23 email='vishal@gmail.com' cgpa=5
# constrant
#   Input should be less than 10 [type=less_than, input_value=12, input_type=int]
























### Basic Example ##############
# from pydantic import BaseModel

# class Student(BaseModel):

#     name: str

# new_strudent = {'name':23}

# student = Student(**new_strudent)

# print(student)
# print(type(student))



### Assigne Default Value // Optional Field // Coerce(Automatically Type Conversion) ##############
# from pydantic import BaseModel
# from typing import Optional

# class Student(BaseModel):
#     # can pass default value
#     name: str = 'Vishal'
#     age: Optional[int] = None


# new_strudent = {'age':"23"}

# student = Student(**new_strudent)

# print(student)
# # print(type(student))




######## Builtin Validation (ex. Check Valid email) ###############################
# If no valid email through an error ---> value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='abc', input_type=str]
# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class Student(BaseModel):
#     # can pass default value
#     name: str = 'Vishal'
#     age: Optional[int] = None
#     email: EmailStr


# new_strudent = {'age':"23", 'email':'abc'}

# student = Student(**new_strudent)

# print(student)