# -*- coding: utf-8 -*-
import os

import nonebot

from utils.config import config


class Shino:
    def __init__(self):
        pass

    @staticmethod
    def run():
        nonebot.init(config)
        nonebot.load_builtin_plugins()
        nonebot.load_plugins('./plugins', 'plugins')
        nonebot.run()
