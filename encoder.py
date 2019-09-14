class Encoder:
    def __init__(self, text: str):
        self.text = text

    def text_to_ascii(self):
        RGB = []
        currentSequence = []

        for letter in self.text:
            if len(currentSequence) is 3:
                RGB.append(currentSequence)
                currentSequence = []

            try:
                if ord(letter) <= 255:
                    currentSequence.append(ord(letter))
                else:
                    print(f'Not a valid ascii character: {letter}')
            except Exception as e:
                pass

        if currentSequence is not []:
            RGB.append(currentSequence)

        while len(RGB[-1]) is not 3:
            RGB[-1].append(0)

        return RGB