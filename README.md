# Wags

[![Build Status](https://travis-ci.com/amaksymov/wags.svg?branch=master)](https://travis-ci.com/amaksymov/wags)

Web Framework

## Example:
```python
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
```

To start server and go to [http://localhost:8000](http://localhost:8000/):
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --debug
```