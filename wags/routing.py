import copy
import typing

from wags.requests import Request
from wags.responses import Response


class RouteNoMatch(Exception):
    pass


class Handle:
    def __init__(self, func):
        self._func = func

    async def map(self, request) -> Response:
        return await self._func(request)


class Route:
    def __init__(
        self,
        path: str,
        handle: Handle,
        methods: typing.Tuple[str] = ('GET',)
    ) -> None:
        self._path = path
        self._handle = handle
        self._methods = methods

    async def map(self, request) -> Response:
        if self.match_path(request) and self.match_method(request):
            print('-'*50)
            return await self._handle.map(request)
        raise RouteNoMatch()

    def match_path(self, request) -> bool:
        if request.match_path(self._path):
            return True
        return False

    def match_method(self, requst) -> bool:
        if requst.match_method(self._methods):
            return True
        return False

    def __str__(self) -> str:
        return f'Response(path=\'{self._path}\', method=\'{self._methods}\', handle=\'{self._handle}\')'

    def __repr__(self) -> str:
        return f'Response(path=\'{self._path}\', method=\'{self._methods}\', handle=\'{self._handle}\')'



class Routing:
    def __init__(self, routes: typing.Sequence[Route]):
        self._routes = routes

    async def map(self, request) -> Response:
        match_path = False
        for route in self._routes:
            if route.match_path(request):
                match_path = True
                if route.match_method(request):
                    return await route.map(request)
        if match_path:
            return Response(content='Method Not Allowed', content_type='text/plain')  # TODO: Method Not Allowed refactor
        return Response(content='Page Not Found', content_type='text/plain')  # TODO: Page Not Found refactor
