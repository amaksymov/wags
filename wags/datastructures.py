import typing

from wags.types import Scope


class ImmutableScope(typing.Mapping):
    def __init__(self, scope: Scope) -> None:
        self._dict = scope

    def __getitem__(self, key: typing.Any) -> typing.Any:
        return self._dict[key]

    def __iter__(self) -> typing.Iterator[typing.Any]:
        return iter(self._dict.keys())

    def __len__(self) -> int:
        return len(self._dict)
