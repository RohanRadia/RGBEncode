import cv2
from PIL import Image

from Misc import from_ascii, from_three, decrypt


class Decode:  # generate class
    def __init__(self, video_name: str, encryption_key: str = " "):  # constructor setup - runs basic code when
        # class is instantiated
        self.video_name = video_name
        self.key = encryption_key  # class variable defined and assigned

        self.raw_data = None  # class variable defined and assigned
        self.frames = []  # class variable defined and assigned
        self.three_list = []
        self.ascii_list = []
        self.encrypted_chars = ''
        self.decrypted_chars = ''

    """
    def from_video(self):  # define required arguments
        video = cv2.VideoCapture(f"{self.video_name}.mp4")

        success, image = video.read()

        count = 0
        while success:
            self.frames.append(f"frame{count}.png")
            cv2.imwrite(f"frame{count}.png", image)
            success, image = video.read()
            count += 1
    """

    def from_frames(self):  # define required arguments
        for frame in self.frames:
            current_frame = Image.open(frame)
            pixels = current_frame.load()

            width, height = current_frame.size

            for x in range(width):
                for y in range(height):
                    self.three_list.append(pixels[x, y])

    def run(self):
        """Deconstruct Video To Frames"""
        self.from_video()

        """Deconstruct Frames To Ascii"""
        self.from_frames()
        self.ascii_list = from_three(self.three_list)

        """Ascii To Letters"""
        self.encrypted_chars = from_ascii(self.ascii_list)

        """Decrypt"""
        self.decrypted_chars = decrypt(self.encrypted_chars, self.key)

        """Save Text To Local .txt File"""

        """Delete Frames"""


a = Decode("encoded", "rohan")
a.from_video()
a.from_frames()
print(from_three(a.three_list))
print(from_ascii(from_three(a.three_list)))
print(decrypt(from_ascii(from_three(a.three_list)), "rohan"))

"""
a = Decode("frame", "rohan")
a.frames.append("frame0.png")
a.from_frames()
print(a.three_list)"""
