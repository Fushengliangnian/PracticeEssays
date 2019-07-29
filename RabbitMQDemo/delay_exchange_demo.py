import pika
import time
import json

credentials = pika.PlainCredentials("musician", "buluowo134679")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', port=5672, virtual_host='/', credentials=credentials
))

if connection.is_open is False:
    print("fail")

channel = connection.channel()

if channel.is_open is False:
    print("2 fail")

# 延迟交换机
delay_exchange = "delay.test.exchange"

# 延迟队列
delay_queue = "delay_test_queue"

# 是否是延迟队列
is_delay = True

# 延迟交换机死信收容交换机
exchange = "test.exchange"

# 延迟队列死信收容队列
queue = "test.queue"

if is_delay is True:
    # 声明收容交换机
    channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)
    # 声明收容队列
    channel.queue_declare(queue=queue, durable=True)
    # 收容队列和收容交换机绑定
    channel.queue_bind(exchange=exchange, queue=queue)
    # 设置延迟队列参数
    arguments = {
        'x-message-ttl': 1000 * 10,  # 延迟时间 （毫秒）
        'x-dead-letter-exchange': exchange,  # 延迟结束后指向交换机（死信收容交换机）
        'x-dead-letter-routing-key': queue,  # 延迟结束后指向队列（死信收容队列）
    }

# 声明队列
channel.exchange_declare(exchange=delay_exchange, exchange_type='fanout', durable=True)
# 声明交换机
channel.queue_declare(queue=delay_queue, durable=True, arguments=arguments)
# 队列和交换机绑定
channel.queue_bind(exchange=delay_exchange, queue=delay_queue)

data = {
    'date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
}
# 加入队列
channel.basic_publish(
    routing_key=delay_queue, body=json.dumps(data),
    properties=pika.BasicProperties(delivery_mode=2),
    exchange=delay_exchange
)
