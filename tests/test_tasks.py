from pytest import raises
from celery.exceptions import Retry
from task_manager.tasks import drink_beer
import time


def test_success(self, mocker):
    import pdb; pdb.set_trace()
    mocked_time_start = mocker.patch(
        "task_manager.tasks.drink_beer.get_time_since_start"
    )
    mocked_self = mocker.Mock()
    start_time = time.time()
    drink_beer(mocked_self, 1, "dave", start_time)
    mocked_time_start.assert_called_with(start_time)
