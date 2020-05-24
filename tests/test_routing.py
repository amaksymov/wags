import asyncio

import pytest

from wags.responses import Response
from wags.requests import Request
from wags.routing import Route, Handle, RouteNoMatch
from wags.datastructures import ImmutableScope


class IndexHandle(Handle):
    async def map(self, request):
        return Response(content='Mock response', content_type='text/plain')


@pytest.mark.asyncio
async def test_route_match():
    route = Route('/', IndexHandle())

    request = Request(
        ImmutableScope({
            'path': '/',
            'method': 'GET'
        })
    )
    assert route.match_path(request) == True
    assert route.match_method(request) == True

    request_same_path = Request(
        ImmutableScope({
            'path': '/',
            'method': 'POST'
        })
    )
    assert route.match_path(request_same_path) == True
    assert route.match_method(request_same_path) == False

    request_same_method = Request(
        ImmutableScope({
            'path': '/test',
            'method': 'GET'
        })
    )
    assert route.match_path(request_same_method) == False
    assert route.match_method(request_same_method) == True


    request_map_route_no_match = Request(
        ImmutableScope({
            'path': '/test',
            'method': 'GET'
        })
    )
    with pytest.raises(RouteNoMatch):
        await route.map(request_map_route_no_match)


@pytest.mark.asyncio
async def test_route_response():
    route = Route('/', IndexHandle())
    request = Request(
        ImmutableScope({
            'path': '/',
            'method': 'GET'
        })
    )
    response = await route.map(request)

    queue = asyncio.Queue()

    await response.send(queue.put)
    assert await queue.get() == {
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    }
    assert await queue.get() == {
        'type': 'http.response.body',
        'body': b'Mock response',
    }
