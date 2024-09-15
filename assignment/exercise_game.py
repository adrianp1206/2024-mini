"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import urequests
import network

FIREBASE_URL = "https://miniproject-c7ea8-default-rtdb.firebaseio.com/response_times.json"


N: int = 10
sample_ms = 10.0
on_ms = 500

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            time.sleep(1)
    
    print("Connected! Network config:", wlan.ifconfig())

connect_wifi('dawgs on three', 'bumen10s')

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    data: dict
        Dictionary data to write to the file.
    """
    
    try:
        response = urequests.post(FIREBASE_URL, json=data)
        
        if response.status_code == 200:
            print("Data successfully written to Firebase!")
        else:
            print(f"Failed to write data to Firebase. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"Error uploading data to Firebase: {e}")


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]
    
    if t_good:
        min_time = min(t_good)
        max_time = max(t_good)
        avg_time = sum(t_good) / len(t_good)
    else:
        min_time, max_time, avg_time = None, None, None
        
    print(f"Average response time: {avg_time} ms")
    print(f"Minimum response time: {min_time} ms")
    print(f"Maximum response time: {max_time} ms")
    
    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    data = {"total_flashes": len(t),
        "misses": misses,
        "min_response_time": min_time,
        "max_response_time": max_time,
        "avg_response_time": avg_time,
        "score": (len(t_good) / len(t))}

    # %% make dynamic filename and write JSON

    write_json(data)

if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)


