# builtins stub used in type-related test cases.

from typing import Any, Generic, List, Sequence, TypeVar
import types

T = TypeVar("T")
S = TypeVar("S")

Self = TypeVar("Self")
class object:
    def __init__(self) -> None: pass

class type:
    __name__: str
    def __call__(self, *args: Any, **kwargs: Any) -> Any: pass
    def __or__(self: Self, other: T) -> Self | T: pass
    def __ror__(self: Self, other: T) -> Self | T: pass
    def mro(self) -> List['type']: pass

class tuple(Generic[T]): pass
class dict(Generic[T, S]): pass
class list(Sequence[T]): pass
class function: pass
class bool: pass
class int: pass
class str: pass
class ellipsis: pass
class float: pass
