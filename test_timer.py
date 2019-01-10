from timer import Timer
from datetime import timedelta

def test_timer_initialize():
    clock = Timer()
    assert clock.empty() is True
def test_timer_add_event():
    clock = Timer()
    clock.schedule(event='start', timespec=timedelta(milliseconds=5))
    assert clock.empty() is False
def test_timer_get_event():
    clock = Timer()
    clock.schedule(event='start', timespec=timedelta(milliseconds=5))
    event = clock.get()
    assert event == 'start'
def test_timer_get_first_event():
    clock = Timer()
    clock.schedule(event='two', timespec=timedelta(milliseconds=15))
    clock.schedule(event='one', timespec=timedelta(milliseconds=7))
    event = clock.get()
    assert event == 'one'
def test_timer_get_time_till_first_event():
    clock = Timer()
    clock.schedule(event='two', timespec=timedelta(milliseconds=15))
    clock.schedule(event='one', timespec=timedelta(milliseconds=7))
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.007
def test_timer_reschedule_event():
    clock = Timer()
    clock.schedule(event='start', timespec=timedelta(milliseconds=5))
    clock.schedule(event='stop', timespec=timedelta(milliseconds=20))
    clock.schedule(event='start', timespec=timedelta(milliseconds=10))
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.010
def test_timer_interval_create():
    clock = Timer()
    clock.interval(deltat=timedelta(milliseconds=10),event='tick')
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.010
def test_timer_interval_with_initialtime():
    clock = Timer()
    clock.interval(deltat=timedelta(milliseconds=10),event='tick',initialtime=timedelta(milliseconds=5))
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.005
def test_timer_interval_period():
    clock = Timer()
    clock.interval(deltat=timedelta(milliseconds=5),event='tick')
    clock.get()
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.005
def test_timer_interval_with_initialtime():
    clock = Timer()
    clock.interval(deltat=timedelta(milliseconds=10),event='tick',initialtime=timedelta(milliseconds=5))
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.005
    clock.get()
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.010
def test_timer_get_non_block():
    clock = Timer()
    clock.schedule(timespec=timedelta(milliseconds=5),event='start')
    clock.get(block=False)
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.005
    clock.get(block=True)
    time_till_first_event = clock.nextdelay()
    assert round(time_till_first_event,3) == 0.000

