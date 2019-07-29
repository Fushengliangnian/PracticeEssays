import aioamqp
import asyncio


async def connect():
    transport, protocol = await aioamqp.connect(port=5672, virtual_host='/', login="musician", password="buluowo134679")
    print(transport, protocol)
    channel = await protocol.channel()

    # 死信收容交换机
    exchange = 'test.exchange'
    # 死信收容队列
    queue = 'test.queue'

    # 设置延迟队列的参数
    arguments = {
        'x-message-ttl': 1000 * 10,  # 延迟时间 （毫秒）
        'x-dead-letter-exchange': exchange,  # 延迟结束后指向交换机（死信收容交换机）
        'x-dead-letter-routing-key': queue,  # 延迟结束后指向队列（死信收容队列）
    }

    await channel.queue_declare(queue_name=queue, durable=True)
    await channel.exchange_declare(exchange_name=exchange, type_name='fanout')
    await channel.queue_bind(exchange=exchange, queue=queue)

    # 延迟交换机
    delay_exchange = 'delay.test.exchange'
    # 延迟队列
    delay_queue = 'delay_test_queue'
    await channel.queue_declare(queue_name=delay_queue, durable=True, arguments=arguments)
    await channel.exchange_declare(exchange_name=delay_exchange, type_name='fanout')

    # 队列和交换机 进行绑定
    await channel.queue_bind(exchange_name=delay_exchange, queue_name=delay_queue, routing_key='')




    # 发消息到该队列
    await channel.basic_publish(
        payload='Hello World!',
        exchange_name='',
        routing_key='hello'
    )

    # close using the `AMQP` protocol
    await protocol.close()
    # ensure the socket is closed.
    transport.close()


asyncio.get_event_loop().run_until_complete(connect())

