"""magiclip class file"""
import logging
import time
from collections.abc import Callable
from itertools import count
import signal

import pyperclip


class MagiClip:
    """class for magic clip"""

    def __init__(self,
                 lambda_fn: Callable,
                 dt: float = 0.25,
                 n: int or None = None):
        """constructor"""
        self.dt = dt
        self.original_clip = ""
        self.processed_clip = ""
        self.n = n
        self.ctrl_c_is_detected = False
        # catch the interruption
        signal.signal(signal.SIGINT, self.ctrl_detection)

        self.lambda_fn = lambda_fn

    def ctrl_detection(self, signum, frame):
        """detect when ctrl+c is hit"""
        self.ctrl_c_is_detected = True
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        msg = f"ctrl+c detected, exiting with signum={signum} and frame={bool(frame)}"
        logging.warning(msg)

    def load_original_clip(self) -> bool:
        """update text from clipboard"""
        text = pyperclip.paste()
        updated_flag = False
        if text != self.processed_clip:
            self.original_clip = text
            updated_flag = True

        return updated_flag

    def update_processed_clip(self) -> str:
        """process original clip to processed clip"""
        self.processed_clip = self.lambda_fn(self.original_clip)
        pyperclip.copy(self.processed_clip)
        return self.processed_clip

    def run(self):
        """run the magic clip function"""
        last_value = ""

        it = range(self.n) if self.n else count()
        for _ in it:
            self.load_original_clip()
            if last_value != self.original_clip:
                last_value = self.original_clip
                self.update_processed_clip()
                print(f"\"{self.original_clip}\" -> \"{self.processed_clip}\"")
                print("")

            if self.ctrl_c_is_detected:
                break

            time.sleep(self.dt)
