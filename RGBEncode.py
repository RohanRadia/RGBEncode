from Utils.Decode import *
from Utils.Encode import *


class RGBEncode:  # generate class
    def __init__(self, raw_data: str, encryption_key: str = " "):  # constructor setup - runs basic code when class is instantiated
        self.decode = Decode()  # initiate Decode class
        self.encode = Encode(raw_data, encryption_key)  # initiate Encode class
