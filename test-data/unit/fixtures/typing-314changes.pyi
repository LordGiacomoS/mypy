Any = object()
Generic = 0
Protocol = 0
Tuple = 0
Type = 0
TypeVar = 0

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)

class Iterable(Protocol[T_co]): pass
class Iterator(Iterable[T_co], Protocol): pass
class Sequence(Iterable[T_co]): pass
class Mapping(Iterable[T], Generic[T, T_co]): pass

class _SpecialForm: pass

class Union:
    def __class_getitem__(cls, item) -> Union: pass
    def __getitem__(self, parameters: Any, /) -> object: pass
