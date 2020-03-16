from Utils.Decode import Decode
from Utils.Encode import Encode


class RGBEncode:  # generate class
    def __init__(self,
                 raw_data: str = None,
                 file_name: str = None,
                 file_type: str = None,
                 encryption_key: str = " ",
                 output_frame_name: str = 'frame'):
        # constructor setup - runs basic code when class is instantiated
        self.raw_data = raw_data
        self.file_name = file_name
        self.file_type = file_type
        self.encryption_key = encryption_key
        self.output_frame_name = output_frame_name

    def check(self):
        process = None

        if self.file_type == "png":
            process = Decode(self.file_name, self.encryption_key)
        elif self.file_name is not None and self.file_name != "Enter what you would like the encoded frame to be named...":
            with open(self.file_name, 'r') as f:
                self.raw_data = f.read()

        if self.file_type != "png":
            process = Encode(self.raw_data, self.encryption_key, self.output_frame_name)
        return process

    def call_run(self):
        process = self.check()
        process.run()
