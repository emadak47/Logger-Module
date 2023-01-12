from typing import Union, Dict, Optional
from utils.Worker import Worker
from type import Stop
from datetime import datetime, timedelta


class LogComponent:
    def __init__(self, _date: Optional[datetime] = None) -> None:
        self._present = _date if _date != None else datetime.today()
        self._tomorrow = self._present + timedelta(1)


    def write(self, msg: Union[str, Dict]) -> None:
        task = Worker(self._write, 0, [msg])
        task.cancel()


    def _write(self, msg: Union[str, Dict]) -> None:
        try:
            now = datetime.today() 

            if now.strftime('%Y-%m-%d') != self._present.strftime('%Y-%m-%d'):
                with open(f"./{self._tomorrow.strftime('%Y-%m-%d')}_log.txt", "a") as f: 
                    f.write(f"{self._tomorrow}: {msg} \n") 

            else: 
                with open(f"./{self._present.strftime('%Y-%m-%d')}_log.txt", "a") as f:
                    f.write(f"{self._present}: {msg} \n")

        except Exception as e:
            print(f"""
                Error occured while attempting to write a log. See error below: \n 
                {e} \n
                """)


    def exit(self, mode: Stop) -> None:
        try: 
            if mode == Stop.INSTANT:
                print("string 1")

            elif mode == Stop.WAIT:
                print("string 2")

        except Exception as e: 
            print(f"""
                Error occured while attempting to stop the log. See error below: \n 
                {e} \n
                """)

        
        # return self._exit(mode)


    def _exit(self, mode: Stop) -> None: 
        pass