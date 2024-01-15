#!/usr/bin/env python3
"""module for asyn"""
import asyncio
import random


async def wait_random(max_delay=0):
    """function of asyn basic
    Keyword arguments:
    max_delay: int arg with a default value 10
    Returns: random delay
    """
    ran_delay = random.uniform(0, max_delay)
    await asyncio.sleep(ran_delay)
    return ran_delay
