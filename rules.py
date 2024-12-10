# rules.py
class Rule:
    """Class representing a splitting rule."""
    def __init__(self, precondition, transformation):
        self.precondition = precondition  # Condition to apply the rule
        self.transformation = transformation  # Function to transform the word

    def matches(self, word, position):
        """Check if the rule is applicable at the given position."""
        return self.precondition(word, position)

    def apply(self, word, position):
        """Apply the rule to split the word."""
        return self.transformation(word, position)
    
    def split(self , word, position):
        if self.matches(word = word, position = position):
            return self.apply(word = word , position = position)
        return None

def vowel(symbol):
    mapping = {
        'ാ'   : 'ആ',
        'ി'   : 'ഇ',
        'ീ'   : 'ഈ',
        'ു'   : 'ഉ',
        'ൂ'   : 'ഊ',
        'െ'  : 'എ',
        'േ'  : 'ഏ',
        'ൈ' : 'ഐ',
        'ൊ' : 'ഒ',
        'ോ' : 'ഓ',
        'ൌ' : 'ഔ',
    }
    return mapping.get(symbol, '')

def geminate(sound):
    if len(sound) == 1:
        return sound + '്' + sound

def singlify(sound):
    if len(sound) ==3 :
        if sound[0] == sound[2]:
            return sound[0]
        
def rootify(sound):
    if len(sound) > 0 :
        return sound[-1]
    return sound
            
def extractCombiSounds(word , pos):
    sound = word[pos -2 : pos +1 ]
    return sound

def isGeminate(sound):
    if len(sound) == 3:
        return sound[0] == sound[2] and sound[1] == '്'
    return False

VOWELS       = ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ']
VOWELSYMBOLS = ['ാ', 'ി', 'ീ', 'ു', 'ൂ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ']
TENSESOUNDS  = ['ക' , 'ച' , 'ട' , 'ത' , 'പ']
MIXEDSOUNDS  = ['ങ്ക' , 'ഞ്ച' , 'ണ്ട' , 'ന്ത' , 'മ്പ' , 'ങ്ങ']


def checkBound(word , pos):
    if pos < 0 or pos > len(word):
        raise ValueError('position out of bound')








def sandhi_1(word , pos):
    return word[pos - 1] in VOWELSYMBOLS

def transi_1(word , pos):
    checkBound(word , pos)
    first = word[:pos - 1] + '്'
    second = vowel(word[pos - 1]) + word[pos:]
    return [first , second]

def sandhi_2(word , pos) :
    return word[:pos - 1] == 'അല്ല' or word[:pos -1] == 'ഇല്ല'

def transi_2(word , pos) :
    checkBound(word , pos)
    first = word[:pos - 1]
    second = vowel(word[pos - 1]) + word[pos:]
    return [first , second]

def sandhi_3(word , pos):
    return (word[pos - 1] not in ['ു' , 'ൂ'] and word[pos] == 'യ') or (word[pos - 1] in ['ു' , 'ൂ'] and word[pos] == 'വ')

def transi_3(word , pos):
    checkBound(word , pos)
    first = word[:pos]
    second = vowel(word[pos+1]) + word[pos+2:]
    return [first , second]

def sandhi_4(word , pos):
    return word[pos- 1] == 'ാ'

def transi_4(word , pos):
    checkBound(word , pos)
    first = word[:pos-1]
    second = word[pos:]
    return [first , second]

def sandhi_5(word , pos):
    return word[pos- 1] == 'മ'

def transi_5(word , pos):
    checkBound(word , pos)
    first = word[:pos-1] + 'ം'
    second = vowel(word[pos]) + word[pos+1:]
    return [first , second]

def sandhi_6(word , pos):
    sound = extractCombiSounds(word , pos)
    return sound == 'ത്ത'
    
def transi_6(word , pos):
    checkBound(word , pos)
    first = word[:pos-2] + 'ം'
    second = vowel(word[pos+1]) + word[pos+2:]
    return [first , second]

def sandhi_7(word , pos):
    sound = extractCombiSounds(word , pos)
    return isGeminate(sound) and word[pos-3] in TENSESOUNDS

def transi_7(word , pos):
    checkBound(word , pos)
    sound = extractCombiSounds(word , pos)
    first = word[:pos-2]
    second = singlify(sound) + word[pos + 1:]
    return [first , second]

def sandhi_8(word , pos):
    sound = extractCombiSounds(word , pos)
    return isGeminate(sound) and word[pos-3] not in TENSESOUNDS

def transi_8(word , pos):
    checkBound(word , pos)
    sound = extractCombiSounds(word , pos)
    first = word[:pos-2] + 'ം'
    second = singlify(sound) + word[pos + 1:]
    return [first , second]

def sandhi_9(word , pos):
    sound = extractCombiSounds(word , pos)
    return sound in MIXEDSOUNDS

def transi_9(word, pos):
    checkBound(word , pos)
    sound = extractCombiSounds(word , pos)
    first = word[:pos-2] + 'ം'
    second = rootify(sound) + word[pos+1:]
    return [first , second]

def sandhi_10(word , pos):
    sound = extractCombiSounds(word , pos)
    return sound == 'ട്ട' or sound == 'റ്റ'

def transi_10(word, pos):
    checkBound(word, pos)
    sound = extractCombiSounds(word, pos)
    first = word[:pos-2] + rootify(sound) + '്'
    second = vowel(word[pos+1]) + word[pos+2:]
    return [first , second]

def sandhi_11(word , pos):
    return word[pos - 1] == 'ോ'

def transi_11(word , pos):
    checkBound(word , pos)
    first = word[:pos-1] + 'സ്'
    second = word[pos:]
    return [first , second]

def sandhi_12(word, pos):
    sound = extractCombiSounds(word , pos)
    return isGeminate(sound) and word[pos - 3] in VOWELS

def transi_12(word , pos):
    checkBound(word, pos)
    sound = extractCombiSounds(word , pos)
    first = word[pos-3]
    second = singlify(sound) + word[pos+1:]
    return [first , second]

def sandhi_13(word , pos) :
    return word[:pos - 1] == 'ആയി' or word[:pos -1] == 'പോയി'

def transi_13(word , pos) :
    checkBound(word , pos)
    first = word[:pos - 1]
    second = vowel(word[pos - 1]) + word[pos:]
    return [first , second]

def sandhi_14(word , pos) :
    return word[:pos - 1] == 'ഒരാ'

def transi_14(word , pos) :
    checkBound(word , pos)
    first = word[:pos - 2] + 'ു'
    second = vowel(word[pos - 1]) + word[pos:]
    return [first , second]