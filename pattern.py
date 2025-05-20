from typing import Optional
from enum import Enum
from typing import Any
from dataclasses import dataclass
 
 
def ask(question: str) -> Optional[bool]:
    question = input("Are you here?")
 
    match question:
        case "yes" | "Yes":
            return True
     match question:
         case "no" | "No":
            return False
     match question:
         case _:  # wildcard pattern
             return None
 
 
 class Operator(Enum):
    ADD = 'Addition'
    MUL = 'Multiplication'
 
 
 def eval(t: tuple) -> int | str | None:
     match t:
         case (Operator.ADD, int_1, int_2):
             return int_1 + int_2
         case (Operator.ADD, str_1, str_2):
             return str_1 + str_2
         case (Operator.MUL, int_1, int_2):
             return int_1 * int_2
         case (Operator.MUL, str_1, str_2):
             return str_1 * str_2
         case _:
             return None
 
 
 @dataclass
 class Cons[T]:
     head: T
     tail: Optional['Cons[T]'] = None
 
 
 type LList[T] = None | Cons[T]
 
 
 def tail(xs: LList) -> LList:
     match xs:
         case None:
             return None
         case Cons(_, tail):
             return tail
 
 
 def len(xs: LList) -> Any:
     match xs:
         case None:
             return 0
         case Cons(_, tail):
             return 1 + len(tail)
