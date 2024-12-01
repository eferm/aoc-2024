from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from typing import Any


def lprint(iterable: Iterable[Any]) -> None:
    for value in iterable:
        print(str(value))


def lzip(*iterables: Iterable[Any]) -> list[Any]:
    return list(zip(*iterables, strict=True))


def lmap[T](func: Callable[[T], Any], *iterables: Iterable[T]) -> list[Any]:
    return list(map(func, *iterables))
