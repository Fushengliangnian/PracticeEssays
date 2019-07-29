#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :
import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest


async def run():
    apns_cert_client = APNs(
        client_cert='/path/to/apns-cert.pem',   # 令牌
        use_sandbox=False,
    )
    apns_key_client = APNs(
        key='/path/to/apns-key.p8',         # 私钥
        key_id='<KEY_ID>',          # 10个字符的密钥标识符（kid）密钥
        team_id='<TEAM_ID>',        # 您的10个字符的团队ID
        topic='com.okmusician.ios',  # 远程通知的主题，通常是应用程序的软件包ID。您在开发人员帐户中创建的证书必须包含此主题的功能。
        use_sandbox=False,
    )
    request = NotificationRequest(
        device_token='<DEVICE_TOKEN>',  # user token
        message = {
            "aps": {
                "alert": "Hello from APNs",
                "badge": "1",
            }
        },
        notification_id=str(uuid4()),  # optional
        time_to_live=3,                # optional
    )
    await apns_cert_client.send_notification(request)
    await apns_key_client.send_notification(request)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
