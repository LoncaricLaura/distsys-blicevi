import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def get_jokes(request):
    try:
        async with aiohttp.ClientSession() as session:
            for _ in range(6):
                tasks = []
                tasks2 = []
                for i in range(10):
                    tasks.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
                    tasks2.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
                res = await asyncio.gather(*tasks)
                res2 = await asyncio.gather(*tasks2)
                res = [await x.json() for x in res]
                res2 = [await x.json() for x in res]
                tasks = []
                tasks2 = []
                async with aiohttp.ClientSession() as session:
                    for i in range(len(res)):
                        tasks.append(asyncio.create_task(session.post("https://0.0.0.0:8082/filterJoke", json=res[i])))
                        tasks2.append(asyncio.create_task(session.post("http://0.0.0.0:8081/filterUser", json=res[i])))
                    res = await asyncio.gather(*tasks)
                    res = await asyncio.gather(*tasks2)
                    res = [await x.json() for x in res]
                return web.json_response({"status":"ok", "message":res, "message2":res2}, status=200)
    except Exception as e:
        return web.json_response({"failed":str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)