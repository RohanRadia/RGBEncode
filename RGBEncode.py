from Utils.Decode import *
from Utils.Encode import *


class RGBEncode:  # generate class
    def __init__(self, raw_data: str = None,
                 file_name: str = None,
                 encryption_key: str = " "):  # constructor setup - runs basic code when class is instantiated
        self.raw_data = raw_data
        self.file_name = file_name
        self.encryption_key = encryption_key

#        self.decode = Decode()  # initiate Decode class
#        self.encode = Encode(raw_data, encryption_key)  # initiate Encode class
