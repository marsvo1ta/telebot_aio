
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, world!")

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)
