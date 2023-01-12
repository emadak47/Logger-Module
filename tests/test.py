import unittest
from utils.Log import LogComponent
from datetime import datetime, timedelta
import time

def read_file_content(file):
    content = []
    with open(file, "r") as f:
        content = f.readlines()
    return content


class TestLogComponent(unittest.TestCase):

    current_date = datetime.today()

    def test_writing(self):
        """
        Test content of log file before and after writing to it.
        """
        log = LogComponent()
        msg = "Y-intercept's test is nice"

        content_before = read_file_content(
            f"./{self.current_date.strftime('%Y-%m-%d')}_log.txt")

        log.write(msg)
        time.sleep(0.1)

        content_after = read_file_content(
           f"./{self.current_date.strftime('%Y-%m-%d')}_log.txt" 
        )

        last_msg = list(set(content_after) - set(content_before))[0]

        self.assertEqual(
            msg, 
            last_msg[last_msg.rfind(":") + 2:].strip())


    def test_new_file_after_midnight(self):
        """
        LogComponent instance is created before midnight.
        Msg arrived after midnight.
        New log file with new timestamp is created
        """

        fake_date = datetime(2023, 1, 12, 23, 59, 59, 99999)
        log = LogComponent(fake_date)

        log._present += timedelta(1)

        msg = "test new log file is created after midnight"
        
        log.write(msg)
        time.sleep(0.1)

        content = read_file_content(
           "./2023-01-13_log.txt")

        last_msg = content[-1]

        self.assertEqual(
            msg, 
            last_msg[last_msg.rfind(":") + 2:].strip())

        


if __name__ == '__main__':
    unittest.main()