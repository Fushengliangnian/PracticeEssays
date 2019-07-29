import pika

credentials = pika.PlainCredentials("musician", "buluowo134679")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', port=5672, virtual_host='/', credentials=credentials
))

if connection.is_open is False:
    print('connection fail')

channel = connection.channel()

if channel.is_open is False:
    print('connection channel fail')

# 延迟交换机
delay_exchange = 'delay.test.exchange'
# 延迟队列
delay_queue = 'delay_test_queue'

# 是否延迟队列
is_delay = True

# 延迟交换机死信收容交换机
exchange = 'test.exchange'
# 延迟队列死信收容队列
queue = 'test.queue'


def methods(ch, method, properties, body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


print(type(channel))
channel.basic_consume(on_message_callback=methods, queue=queue)
channel.start_consuming()
