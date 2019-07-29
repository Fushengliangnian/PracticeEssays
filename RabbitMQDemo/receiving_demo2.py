import aioamqp
import asyncio


async def connect():
    transport, protocol = await aioamqp.connect(port=5672, virtual_host='/', login="musician", password="buluowo134679")
    channel = await protocol.channel()

    await channel.queue_declare(queue_name='hello')
    await channel.basic_consume(callback, queue_name='hello', no_ack=True)


async def callback(channel, body, envelope, properties):
    print(body)


asyncio.get_event_loop().run_until_complete(connect())
