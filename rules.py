# rules.py
class Rule:
    """Class representing a splitting rule."""
    def __init__(self, precondition, transformation):
        self.precondition = precondition  # Condition to apply the rule
        self.transformation = transformation  # Function to transform the word

    def matches(self, position):
        """Check if the rule is applicable at the given position."""
        return self.precondition(position)

    def apply(self, position):
        """Apply the rule to split the word."""
        return self.transformation(position)
    
    def split(self , position):
        if self.matches(position):
            return self.apply(position)
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


class SandhiRules :
    def __init__(self):
        self._VOWELS       = ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ']
        self._VOWELSYMBOLS = ['ാ', 'ി', 'ീ', 'ു', 'ൂ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ']
        self._TENSESOUNDS  = ['ക' , 'ച' , 'ട' , 'ത' , 'പ']
        self._MIXEDSOUNDS  = ['ങ്ക' , 'ഞ്ച' , 'ണ്ട' , 'ന്ത' , 'മ്പ' , 'ങ്ങ']
        self._word = None
        self._Rules = [
            Rule( self._sandhi_1  , self._transi_1  ),
            Rule( self._sandhi_2  , self._transi_2  ),
            Rule( self._sandhi_3  , self._transi_3  ),
            Rule( self._sandhi_4  , self._transi_4  ),
            Rule( self._sandhi_5  , self._transi_5  ),
            Rule( self._sandhi_6  , self._transi_6  ),
            Rule( self._sandhi_7  , self._transi_7  ),
            Rule( self._sandhi_8  , self._transi_8  ),
            Rule( self._sandhi_9  , self._transi_9  ),
            Rule( self._sandhi_10 , self._transi_10 ),
            Rule( self._sandhi_11 , self._transi_11 ),
            Rule( self._sandhi_12 , self._transi_12 ),
            Rule( self._sandhi_13 , self._transi_13 ),
            Rule( self._sandhi_14 , self._transi_14 ),
            Rule( self._sandhi_15 , self._transi_15 ),
            Rule( self._sandhi_16 , self._transi_16 ),
        ]



    def updateWord(self , word):
        self._word = word

    def _checkBound(self , pos):
        if pos < 0 or pos > len(self._word):
            raise ValueError('position out of bound')

    def __getitem__(self, index):
        self._checkBound(index)
        results = []
        for r in self._Rules:
            spilts = r.split(index)
            if spilts is not None :
                results.append(spilts)
        if results :
            return results
        return []

    def _sandhi_1(self, pos):
        return self._word[pos - 1] in self._VOWELSYMBOLS
    
    def _transi_1(self, pos):
        first = self._word[:pos - 1] + '്'
        second = vowel(self._word[pos - 1]) + self._word[pos:]
        return [first , second]
    
    def _sandhi_2(self, pos) :
        return self._word[:pos - 1] == 'അല്ല' or self._word[:pos -1] == 'ഇല്ല'
    
    def _transi_2(self, pos) :
        first = self._word[:pos - 1]
        second = vowel(self._word[pos - 1]) + self._word[pos:]
        return [first , second]
    
    def _sandhi_3(self, pos):
        return (self._word[pos - 1] not in ['ു' , 'ൂ'] and self._word[pos] == 'യ') or (self._word[pos - 1] in ['ു' , 'ൂ'] and self._word[pos] == 'വ')
    
    def _transi_3(self, pos):
        first = self._word[:pos]
        second = vowel(self._word[pos+1]) + self._word[pos+2:]
        return [first , second]
    
    def _sandhi_4(self, pos):
        return self._word[pos- 1] == 'ാ'
    
    def _transi_4(self, pos):
        first = self._word[:pos-1]
        second = self._word[pos:]
        return [first , second]
    
    def _sandhi_5(self, pos):
        return self._word[pos- 1] == 'മ'
    
    def _transi_5(self, pos):
        first = self._word[:pos-1] + 'ം'
        second = vowel(self._word[pos]) + self._word[pos+1:]
        return [first , second]
    
    def _sandhi_6(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return sound == 'ത്ത'
        
    def _transi_6(self, pos):
        first = self._word[:pos-2] + 'ം'
        second = vowel(self._word[pos+1]) + self._word[pos+2:]
        return [first , second]
    
    def _sandhi_7(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return isGeminate(sound) and self._word[pos-3] in self._TENSESOUNDS
    
    def _transi_7(self, pos):
        sound = extractCombiSounds(self._word , pos)
        first = self._word[:pos-2]
        second = singlify(sound) + self._word[pos + 1:]
        return [first , second]
    
    def _sandhi_8(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return isGeminate(sound) and self._word[pos-3] not in self._TENSESOUNDS
    
    def _transi_8(self, pos):
        sound = extractCombiSounds(self._word , pos)
        first = self._word[:pos-2] + 'ം'
        second = singlify(sound) + self._word[pos + 1:]
        return [first , second]
    
    def _sandhi_9(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return sound in self._MIXEDSOUNDS
    
    def _transi_9(self, pos):
        sound = extractCombiSounds(self._word , pos)
        first = self._word[:pos-2] + 'ം'
        second = rootify(sound) + self._word[pos+1:]
        return [first , second]
    
    def _sandhi_10(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return sound == 'ട്ട' or sound == 'റ്റ'
    
    def _transi_10(self , word, pos):
        sound = extractCombiSounds(self._word, pos)
        first = self._word[:pos-2] + rootify(sound) + '്'
        second = vowel(self._word[pos+1]) + self._word[pos+2:]
        return [first , second]
    
    def _sandhi_11(self, pos):
        return self._word[pos - 1] == 'ോ'
    
    def _transi_11(self, pos):
        first = self._word[:pos-1] + 'സ്'
        second = self._word[pos:]
        return [first , second]
    
    def _sandhi_12(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return isGeminate(sound) and self._word[pos - 3] in self._VOWELS
    
    def _transi_12(self, pos):
        sound = extractCombiSounds(self._word , pos)
        first = self._word[pos-3]
        second = singlify(sound) + self._word[pos+1:]
        return [first , second]
    
    def _sandhi_13(self, pos) :
        return self._word[:pos - 1] == 'ആയി' or self._word[:pos -1] == 'പോയി'
    
    def _transi_13(self, pos) :
        first = self._word[:pos - 1]
        second = vowel(self._word[pos - 1]) + self._word[pos:]
        return [first , second]
    
    def _sandhi_14(self, pos) :
        return self._word[:pos - 1] == 'ഒരാ'
    
    def _transi_14(self, pos) :
        first = self._word[:pos - 2] + 'ു'
        second = vowel(self._word[pos - 1]) + self._word[pos:]
        return [first , second]
    
    def _sandhi_15(self, pos) :
        sound = extractCombiSounds(self._word,pos-2)
        return self._word[pos - 1] in self._VOWELSYMBOLS and not isGeminate(sound)
    
    def _transi_15(self, pos) :
        first  = self._word[:pos]
        sound = extractCombiSounds(self._word , pos+2)
        if isGeminate(sound):
            second = self._word[pos+2:]
        else : 
            second = self._word[pos:]
        return [first, second]
    
    def _sandhi_16(self, pos):
        sound = extractCombiSounds(self._word , pos)
        return isGeminate(sound) and self._word[pos - 3] in self._VOWELSYMBOLS
    
    def _transi_16(self, pos):
        sound = extractCombiSounds(self._word , pos)
        first = self._word[:pos-2]
        second = singlify(sound) + self._word[pos + 1:]
        return [first , second]

