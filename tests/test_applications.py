import asyncio
from wags.datastructures import ImmutableScope
from wags.routing import Routing

import pytest

from wags import __version__
from wags.applications import Wags
from wags.testclient import TestClient


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.asyncio
async def test_applications():
    client = TestClient(Wags(Routing([])))
    send_queue = await client.request({
        'type': 'http',
        'method': 'GET',
        'path': '/'
    })

    assert await send_queue.get() == {
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    }

    assert await send_queue.get() == {
        'type': 'http.response.body',
        'body': b'Page Not Found',
    }
