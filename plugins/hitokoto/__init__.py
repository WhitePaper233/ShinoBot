# -*- coding: utf-8 -*-
import aiohttp

from nonebot import on_command, CommandSession


@on_command('一言', aliases=('来句骚话', '来句废话', '说句骚话', '说句费话', '发句骚话', '发句废话'))
async def hitokoto(bot_session: CommandSession):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://v1.hitokoto.cn/') as resp:
            result = await resp.json()
            await bot_session.send(f'{result["hitokoto"]}\n——{result["from"]}')


@on_command('一言动画', aliases=('来句动画名言', '说句动画名言', '发句动画名言'))
async def hitokoto_anime(bot_session: CommandSession):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://v1.hitokoto.cn/', params=[('c', 'a')]) as resp:
            result = await resp.json()
            await bot_session.send(f'{result["hitokoto"]}\n——{result["from"]}')
