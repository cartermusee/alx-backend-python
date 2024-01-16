#!/usr/bin/env python3
"""module for compresions"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Async Comprehensions
    collect 10 random numbers using an async comprehensing
    Returns:  10 random numbers.
    """
    rand_nums = [i async for i in async_generator()]
    return rand_nums
