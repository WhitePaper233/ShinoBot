# -*- coding: utf-8 -*-
import aiohttp
import nonebot

from aiocqhttp.exceptions import Error as CQHttpError


status = True


@nonebot.scheduler.scheduled_job('cron', second='10')
async def bili_live_pusher():
    bot = nonebot.get_bot()
    target_group_id = 14295996
    room_id = 865022
    global status
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.live.bilibili.com/room/v1/Room/room_init', params=[('id', room_id)]) as res:
            result = await res.json()
            if result['code'] == 0 and result['data']['live_status'] == 1:
                if status:
                    async with session.get('https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo',
                                           params=[('uids', result['data']['uid']), ('req_biz', 'video')]) as resp:
                        data = await resp.json()
                        uid = str(result["data"]["uid"])
                        msg = f'直播已经开始辣~\n' \
                              f'[CQ:image,file={data["data"]["by_uids"][uid]["cover"]}]\n' \
                              f'{data["data"]["by_uids"][uid]["title"]}\n' \
                              f'{data["data"]["by_uids"][uid]["parent_area_name"]}: ' \
                              f'{data["data"]["by_uids"][uid]["area_name"]}\n' \
                              f'{data["data"]["by_uids"][uid]["description"]}\n' \
                              f'https://live.bilibili.com/{room_id}'
                    try:
                        await bot.send_group_msg(group_id=target_group_id, message=msg)
                    except CQHttpError:
                        pass
                    status = False
            else:
                status = True
