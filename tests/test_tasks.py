import time

import pytest
from celery.exceptions import Retry
from task_manager.tasks import drink_beer, smoke_cigarette, go_to_toilet


@pytest.mark.parametrize("task_func", (drink_beer, smoke_cigarette, go_to_toilet))
def test_success_one_task(mocker, task_func):
    mocked_acquire = mocker.MagicMock()
    mocked_acquire.acquire.return_value = True
    mocked_redis = mocker.patch("task_manager.decorators.REDIS_CLIENT")
    mocked_redis.lock.return_value = mocked_acquire

    mocked_time_start = mocker.patch("task_manager.tasks.get_time_since_start")
    start_time = time.time()

    task_func(1, "dave", start_time)

    mocked_time_start.assert_called_once()
    mocked_time_start.assert_called_with(start_time)
    mocked_redis.lock.called_once()


@pytest.mark.parametrize("task_func", (drink_beer, smoke_cigarette, go_to_toilet))
def test_retry_one_task(mocker, task_func):
    mocked_acquire = mocker.MagicMock()
    mocked_acquire.acquire.return_value = False
    mocked_redis = mocker.patch("task_manager.decorators.REDIS_CLIENT")
    mocked_redis.lock.return_value = mocked_acquire

    mocked_time_start = mocker.patch("task_manager.tasks.get_time_since_start")
    start_time = time.time()

    with pytest.raises(Retry):
        task_func(1, "dave", start_time)

    assert not mocked_time_start.called
    mocked_redis.lock.called_once()
