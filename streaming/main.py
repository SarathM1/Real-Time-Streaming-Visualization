from Visual import Visual
from Sensor import Sensor, threading


def threads(callbackFunc, running):
    # Set multiple threads
    # Instantiate the Sensor thread
    sensor = Sensor(callbackFunc=callbackFunc, running=running)
    # Start threads
    sensor.start()  # Run the thread to start collecting data


def main():
    # Set global flag
    event = threading.Event()  # Create an event to communicate between threads
    event.set()  # Set the event to True

    # Instantiate a Bokeh web document
    webVisual = Visual(callbackFunc=threads, running=event)
    threads(callbackFunc=webVisual, running=event)  # Call Sensor thread


# Run command:
# bokeh serve --show streaming
main()
