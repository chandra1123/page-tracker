# test/conftest.py

import pytest
import redis

from page_tracker.app import app

def pytest_addoption(parser):
    parser.addoption("--flask-url", default="http://127.0.0.1:5000/" )
    parser.addoption("--redis-url", default="redis://localhost:9736")

@pytest.fixture(scope="session")
def flask_url(request):
    return request.config.getoption("--flask-url")

@pytest.fixture(scope="session")
def redis_url(request):
    return request.config.getoption("--redis-url")

@pytest.fixture
def http_client():
    return app.test_client()

@pytest.fixture(scope="module")
def redis_client(redis_url):
    if redis_url:
        return redis.Redis.from_url(redis_url)
    return redis.Redis()