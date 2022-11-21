import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes("/filterJoke")
async def filter_joke(request):
    try:

    except Exception as e:
        return web.json_response({"failed":str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)