#!/usr/bin/env python3
"""module for tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creating tasks
    Keyword arguments:
    max_delay: delay number
    Returns: the task created
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
