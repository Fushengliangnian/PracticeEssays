import aioredis
import asyncio

loop = asyncio.get_event_loop()


async def run():
    conn = await aioredis.create_connection(("127.0.0.1", 6379), loop=loop)
    ret = await conn.sadd("demo", 3)
    print(ret)


loop.run_until_complete(run())
