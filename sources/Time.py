
import time


class Time:
    fps = 30
    deltaTime = 0
    over_deltaTime = 0
    prev_time = 0
    current_time = 0

    @staticmethod
    def Init():
        Time.prev_time = time.time()
        Time.current_time = time.time()

    @staticmethod
    def UpdateTime():
        Time.current_time = time.time()
        Time.deltaTime = Time.current_time - Time.prev_time
        Time.prev_time = Time.current_time


