import pytest
import time

@pytest.mark.timeout(2)
def test_long_running_operation():
    # Perform a long-running operation
    time.sleep(20)  # Simulate a time-consuming operation that exceeds the timeout
    # ...