import typing

from wags.datastructures import ImmutableScope
from wags.types import Scope, Receive, Send


class Wags:
    def __init__(self):
        pass

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        immutable_scope = ImmutableScope(scope)

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ]
        })

        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })
