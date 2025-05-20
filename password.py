from dataclasses import dataclass, InitVar
from string import ascii_uppercase
from string import digits
 
 
@dataclass  # a)
class User:
     _name: InitVar[str]
     _age: InitVar[int]
     _password: InitVar[str]
 
     def __post_init__(self, _name: str, _age: int, _password: str):
         assert len(_name) >= 2, 'name muss mindestens zwei Zeichen lang sein'
         assert _age >= 13, 'age muss mindestens 13 sein'
         assert len(_password) >= 6, 'password mss mindestens 6 Zeichen lang sein'
         assert sum(ch.isupper() for ch in _password) >= 1, 'password muss mindestens einen Großbuchstaben enthalten'
         assert sum(ch.isdigit() for ch in _password) >= 2, 'password muss mindestens zwei Zifferen (0-9) besitzen'
         self.__name = _name
         self.__age = _age
         self.__password = _password
