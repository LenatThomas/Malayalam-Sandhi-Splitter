class Syllable:
    def __init__(self, word):
        self._boundaries = []
        self._word = word
        self._wordLen = len(word)
        self._VOWELS = [
            "അ", "ആ", "ഇ", "ഈ", "ഉ", "ഊ", "ഋ", "എ", "ഏ", "ഐ", "ഒ", "ഓ", "ഔ", "അം", "അഃ"
        ]
        self._CONSONENTS = [
            "ക", "ഖ", "ഗ", "ഘ", "ങ",
            "ച", "ഛ", "ജ", "ഝ", "ഞ",
            "ട", "ഠ", "ഡ", "ഢ", "ണ",
            "ത", "ഥ", "ദ", "ധ", "ന",
            "പ", "ഫ", "ബ", "ഭ", "മ",
            "യ", "ര", "ല", "വ",
            "ശ", "ഷ", "സ", "ഹ",
            "ള", "ഴ", "റ"
        ]
        self._BASESOUNDS = self._VOWELS + self._CONSONENTS
        self._createBoundaries()
        self._len = len(self._boundaries) + 1

    def _createBoundaries(self):
        word = self._word
        for i in range(len(word)) :
            if word[i] in self._BASESOUNDS and word[i-1] != '്':
                self._boundaries.append(i)

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        if index > self._len :
            raise ValueError("Index out of bound")
        start = self._boundaries[index]
        end   = index + 1 if index + 1 < self._len else self._len - 1
        sound = self._word[start:end]
        return sound 
        