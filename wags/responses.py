from wags.types import Send


class Response:
    def __init__(self, content: str, content_type: str, status_code: int = 200) -> None:
        self._content = content
        self._content_type = content_type
        self._status_code = status_code

    async def send(self, send: Send):
        await send({
            'type': 'http.response.start',
            'status': self._status_code,
            'headers': [
                [b'content-type', self._content_type.encode('utf-8')],
            ]
        })

        await send({
            'type': 'http.response.body',
            'body': self._content.encode('utf-8'),
        })