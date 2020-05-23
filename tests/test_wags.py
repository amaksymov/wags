import asyncio

import pytest

from wags import __version__
from wags.applications import Wags 


def test_version():
    assert __version__ == '0.1.0'


class MockServer:
    queue: asyncio.Queue

    def __init__(self):
        self._receive_queue = asyncio.Queue()
        self._send_queue = asyncio.Queue()

    async def receive(self):
        return await self._receive_queue.get()

    async def send(self, message):
        return await self._send_queue.put(message)
    
    def get_scope(self):
        return {
            'type': 'http',
            'method': 'GET',
        }


@pytest.mark.asyncio
async def test_applications():
    server = MockServer()
    app = Wags()

    await app(
        server.get_scope, 
        server.receive, 
        server.send
    )
    
    message = await server._send_queue.get()
    assert message == {
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    }

    second_message = await server._send_queue.get()
    assert second_message == {
            'type': 'http.response.body',
            'body': b'Hello, world!',
        }
