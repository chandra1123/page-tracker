# src/page_tracker/app.py

import os
from functools import lru_cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")  # pylint: disable=E1101
        return "Sorry, something went wrong \N{pensive face}", 500
    return f"This page has been seen {page_views} times."


@lru_cache(maxsize=None)
def redis():
    return Redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:9736"),
        socket_connect_timeout=10,
        socket_timeout=10,
    )
