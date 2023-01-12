import time
import threading
from typing import Iterable, Optional

class Worker:
    def __init__(
        self, 
        _func: str,
        _interval: int = 0, 
        _args: Iterable = ()
    ) -> None:
        self._interval = _interval
        self._func = _func
        self._args = _args
        self._stop_event = threading.Event()
        thread = threading.Thread(target=self.__set_interval, args=self._args)
        thread.start()

    def __set_interval(self, args: Iterable = ()) -> None:
        next = time.time() + self._interval
        while not self._stop_event.wait(next - time.time()):
            next += self._interval
            if args: self._func(args)
            else: self._func()

    def cancel(self) -> None:
        self._stop_event.set()