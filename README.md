# Timer

A python class to keep a schedule of events (plain strings) in the future.
Get the time till the first event.
Retrieve the first event.
Reschedule an event to a new time.
Events can be scheduled at an absoulte time, relative time and with a periodic interval
Note that each event can only appear once. Adding a second event with the same name will result in a reschedule of the initial event. 
