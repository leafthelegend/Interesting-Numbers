from dataclasses import dataclass
from typing import Optional

@dataclass
class InterestingNumber:
    number: int
    printed_number: str #how to print the number
    description: Optional[str] = None #what is the number interesting for
    base: Optional[int] = None #in which base is the number interesting (None if every base is interesting)
