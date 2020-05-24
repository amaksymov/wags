from wags.datastructures import ImmutableScope


class Request:
    def __init__(self, scope: ImmutableScope) -> None:
        self._path = scope['path']
        self._method = scope['method']

    def match_path(self, path) -> bool:
        return self._path == path

    def match_method(self, methods) -> bool:
        return self._method in methods

    def __str__(self) -> str:
        return f'Request(path=\'{self._path}\', method=\'{self._method}\')'

    def __repr__(self) -> str:
        return f'Request(path=\'{self._path}\', method=\'{self._method}\')'