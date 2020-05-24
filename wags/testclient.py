import asyncio

from wags.datastructures import Scope


class TestClient:
    __test__ = False  # For pytest to not discover this up.
    _receive_queue: asyncio.Queue
    _send_queue: asyncio.Queue

    def __init__(self, app) -> None:
        self._app = app
        self._receive_queue = asyncio.Queue()
        self._send_queue = asyncio.Queue()

    async def _receive(self):
        return await self._receive_queue.get()

    async def _send(self, message):
        return await self._send_queue.put(message)

    async def request(self, scope: Scope) -> asyncio.Queue:
        await self._app(
            scope,
            self._receive,
            self._send
        )
        return self._send_queue
