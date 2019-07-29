import os, sys, time
import requests
import json


class RabbitMQTool(object):
    def __init__(self, host, vhost, queue, user, passwd):
        self.host = host
        self.vhost = vhost
        self.queue = queue
        self.user = user
        self.passwd = passwd

    # 返回3种消息数量：ready, unacked, total
    def getMessageCount(self):
        url = 'http://%s:15672/api/queues/%s/%s' % (self.host, self.vhost, self.queue)
        r = requests.get(url, auth=(self.user, self.passwd))
        print(r)
        if r.status_code != 200:
            return -1

        dic = json.loads(r.text)

        return dic['messages_ready'], dic['messages_unacknowledged'], dic['messages']


if __name__ == '__main__':
    mqTool = RabbitMQTool(host='192.168.1.254',
                          vhost='vhost_walker',
                          queue='delay-buffer-queue',
                          user='musician',
                          passwd='buluowo134679')

    ready, unacked, total = mqTool.getMessageCount()

    print('ready: %d' % ready)
    print('unacked: %d' % unacked)
    print('total: %d' % total)