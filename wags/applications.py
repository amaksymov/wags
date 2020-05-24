from wags.requests import Request
from wags.routing import Routing
from wags.datastructures import ImmutableScope
from wags.types import Scope, Receive, Send


class Wags:
    def __init__(self, routing: Routing):
        self._routing = routing

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send
    ) -> None:
        response = await self._routing.map(Request(
            ImmutableScope(scope),
        ))
        await response.send(send)
