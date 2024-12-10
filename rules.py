# rules.py
class Rule:
    """Rule class that checks for the condition and applies transformation to it.
    """
    def __init__(self, precondition, transformation):
        self.precondition = precondition  
        self.transformation = transformation  

    def matches(self, position):
        """Check if the rule is applicable at the given position."""
        return self.precondition(position)

    def apply(self, position):
        """Apply the transformation to split the word at the given position."""
        return self.transformation(position)
    
    def split(self , position):
        """Checks the rule at the given position and applies transformation to the given position if the rule holds true.

        Args:
            position (int): position to check and apply the rule

        Returns:
            list: List contaning the first and second words after applying the rule. Returns None if no rule can be applied at the given position
        """
        if self.matches(position):
            return self.apply(position)
        return None

def vowel(symbol):
    """For a given vowel symbol gives the corresponding vowel.

    Args:
        symbol (str): vowel symbol string

    Returns:
        str: vowel str
    """
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
    """Doubles the given sound, making it a geminate

    Args:
        sound (str): The sound to be doubled

    Returns:
        str: A string of length 3 containing the geminate sound.
    """
    if len(sound) == 1:
        return sound + '്' + sound

def singlify(sound):
    """Strips the geminate sound and gives the base sound

    Args:
        sound (str): The geminate sound

    Returns:
        str: The stripped base sound
    """
    if len(sound) ==3 :
        if sound[0] == sound[2]:
            return sound[0]
        
def rootify(sound):
    """For the given compound sound, gives the root sound

    Args:
        sound (str): The string if length 3 contatining the mixed sound

    Returns:
        str: The root sound of the compound sound
    """
    if len(sound) > 0 :
        return sound[-1]
    return sound
            
def extractCombiSounds(word , pos):
    """Extracts the combinations sounds from the word. The sound of length 3 is extracted from positions before pos.

    Args:
        word (str): The word from which the sound is to be extracted
        pos (int): The position from where the sound is to be extracted.

    Returns:
        str: A string of length 3 containing the sound
    """
    if pos < 0 or pos + 1 > len(word):
        return ''
    sound = word[pos -2 : pos +1 ]
    return sound

def isGeminate(sound):
    """Checks if the given sound is a geminate sound.

    Args:
        sound (str): The string of length 3 to be checked.

    Returns:
        bool: Returns True if given sound is geminate sound.
    """
    if len(sound) == 3:
        return sound[0] == sound[2] and sound[1] == '്'
    return False


class SandhiRules :
    """SandhiRules containes all the sandhi rules requires to split a compound word into individual words
    """
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
        """Update the object with a new word to apply the rules

        Args:
            word (str): The word to be split
        """
        self._word = word

    def _checkLowerBound(self , pos):
        return pos - 1 < 0

    def _checkUpperBound(self , pos):
        return pos + 2 > len(self._word) 

    def __getitem__(self, index):
        """Tries to split the compound word at the given index by applying all the Sandhi rules one by one.

        Args:
            index (nt): The index of the word to apply the rules

        Returns:
            list: list containing list of individual splits by applying each Sandhi Rules. Return empty list if no rules apply.
        """
        if self._checkLowerBound(index):
            return []
        if self._checkUpperBound(index):
            return []
        results = []
        for r in self._Rules:
            spilts = r.split(index)
            if spilts is not None :
                results.append(spilts)
        if results :
            return results
        return []

    """From here onwards are all the functions for Sandhi Rules and Transformations
    """



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
    
    def _transi_10(self, pos):
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

