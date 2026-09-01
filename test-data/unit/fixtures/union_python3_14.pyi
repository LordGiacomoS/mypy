# builtins stub used in test cases related to 3.14's union changes.

from typing import Generic,  Sequence, TypeVar
from types import UnionType
T = TypeVar("T")
S = TypeVar("S")

class object:
    def __init__(self) -> None: pass
class type:
    def __call__(self, *a: object) -> object: pass
    def __or__(self: S, other: T) -> S | T: pass
    def __ror__(self: S, other: T) -> S | T: pass

class ellipsis: pass

class int: pass
class bool(int): pass
class float: pass

class list(Sequence): pass
class tuple(Generic[T]): pass
class str: pass
class bytes: pass

class dict: pass
