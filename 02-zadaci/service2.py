import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

async def random_user(x):
    async with x.get("https://randomuser.me/api/") as res:
        json = await res.json()
        json = json ["res"][0]
        return json

@routes.post("/filterUser")
async def filter_user(request):
    try: 
        tasks = []
        json_data = await request.json()
        async with aiohttp.ClientSession() as session:
            user = await random_user(session)
            tasks.append({"name": user["name"]["first"], "surname": user["name"]["last"], "city": user["location"]["city"], "email": ["email"]})
        return web.json_response({"status": "success"})
    except Exception as e:
        return web.json_response({"failed":str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)