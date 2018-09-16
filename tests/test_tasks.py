from pytest import raises, mark
from celery.exceptions import Retry
from task_manager.tasks import drink_beer
from task_manager import decorators
import time


def test_success(mocker):
    mocked_acquire = mocker.MagicMock()
    mocked_acquire.acquire.return_value = True
    mocked_redis = mocker.patch("task_manager.decorators.REDIS_CLIENT")
    mocked_redis.lock.return_value = mocked_acquire

    mocked_time_start = mocker.patch("task_manager.tasks.get_time_since_start")
    start_time = time.time()

    drink_beer(1, "dave", start_time)

    mocked_time_start.assert_called_once()
    mocked_time_start.assert_called_with(start_time)
    mocked_redis.lock.called_once()
