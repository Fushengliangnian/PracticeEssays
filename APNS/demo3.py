#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

import asyncio
import logging

import uvloop

from aioapns import APNs, NotificationRequest


def setup_logger(log_level):
    log_level = getattr(logging, log_level)
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)8s %(module)6s:%(lineno)03d %(message)s',
        level=log_level
    )


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    setup_logger('INFO')

    client_cert = '/Users/mac/musician/apps/push_serverice/cert/apns_dev.pem'
    device_token = '69-FC-04-3F-20-C6-02-91-2B-87-AA-B7-EA-19-BF-78-38-32-82-B6-0C-BF-33-A6-2C-CB-A1-EA-B2-79-0F-85'
    message = {
        "aps": {
            "alert": "Hello from APNs Tester.",
            "badge": "1",
            "sound": "default",
        }
    }

    apns = APNs(client_cert, use_sandbox=True)

    async def send_request():
        request = NotificationRequest(
            device_token=device_token,
            message=message
        )
        await apns.send_notification(request)

    async def main():
        send_requests = [send_request() for _ in range(1000)]
        import time
        t = time.time()
        ret = await asyncio.wait(send_requests)
        print(ret)
        print('Done: %s' % (time.time() - t))
        print()
    try:
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(main())
        loop.run_forever()
    except KeyboardInterrupt:
        pass