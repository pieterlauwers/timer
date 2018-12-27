from timer import Timer
from datetime import timedelta

def test_timer_initialize():
    clock = Timer()
    assert clock.empty() is True
def test_timer_add_event():
    clock = Timer()
    clock.schedule('start',timedelta(seconds=5))
    assert clock.empty() is False
def test_timer_get_event():
    clock = Timer()
    clock.schedule('start',timedelta(seconds=5))
    event = clock.pop()
    assert event == 'start'
def test_timer_get_first_event():
    clock = Timer()
    clock.schedule('two',timedelta(seconds=15))
    clock.schedule('one',timedelta(seconds=7))
    event = clock.pop()
    assert event == 'one'
def test_timer_get_time_till_first_event():
    clock = Timer()
    clock.schedule('two',timedelta(seconds=15))
    clock.schedule('one',timedelta(seconds=7))
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event) == 7
def test_timer_reschedule_event():
    clock = Timer()
    clock.schedule('start',timedelta(seconds=5))
    clock.schedule('stop',timedelta(seconds=20))
    clock.schedule('start',timedelta(seconds=10))
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event) == 10
