from wags.responses import Response
from wags.routing import Handle, Route, Routing
from wags.applications import Wags

async def handle_func(request):
    return Response(content='Hello, world!', content_type='text/plain')

app = Wags(
    Routing([
        Route('/', Handle(
            handle_func
        ))
    ])
)
