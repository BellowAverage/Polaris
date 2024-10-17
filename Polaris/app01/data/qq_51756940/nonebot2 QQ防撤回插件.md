
--- 
title:  nonebot2 QQ防撤回插件 
tags: []
categories: [] 

---
## 代码如下：

```
import json
from nonebot import on_notice, Bot
from nonebot.adapters.onebot.v11 import GroupRecallNoticeEvent, FriendRecallNoticeEvent

def extract_message_info(message_list):
    extracted_messages = []
    
    for msg in message_list:
        if msg['type'] == 'text':
            extracted_messages.append(f"文本: {msg['data']['text']}")
        elif msg['type'] == 'image':
            extracted_messages.append(f"图片: {msg['data']['url']}")
    
    return "\n".join(extracted_messages)

group_recall = on_notice(rule=lambda bot, event: isinstance(event, GroupRecallNoticeEvent), priority=50)
friend_recall = on_notice(rule=lambda bot, event: isinstance(event, FriendRecallNoticeEvent), priority=50)

@group_recall.handle()
async def handle_group_recall(bot: Bot, event: GroupRecallNoticeEvent):
    msg = await bot.call_api('get_msg', **{"message_id": event.message_id})
    mesg = msg['message']
    extracted_mesg = extract_message_info(mesg)
    # await bot.call_api('send_group_msg', **{"group_id": event.group_id,
    #                                         "message": f"{event.user_id} 撤回了一条消息:\n{extracted_mesg}"})
    await bot.call_api('send_private_msg', **{"user_id": 你的QQ号,
                                              "message": f"群 {event.group_id} 的 {event.user_id} 撤回了一条消息:\n{extracted_mesg}"})

@friend_recall.handle()
async def handle_friend_recall(bot: Bot, event: FriendRecallNoticeEvent):
    msg = await bot.call_api('get_msg', **{"message_id": event.message_id})
    mesg = msg['message']
    extracted_mesg = extract_message_info(mesg)
    await bot.call_api('send_private_msg', **{"user_id": event.user_id,
                                              "message": f"你撤回了一条消息:\n{extracted_mesg}"})

```

注释部分为直接在群里发出撤回信息，不太好，还是偷偷转发给某人吧。



## 效果如下：

<img alt="" height="200" src="https://img-blog.csdnimg.cn/593b82af8c7942c980791a03c8350cc6.png" width="580">
