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

VOWELS       = ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ']
VOWELSYMBOLS = ['ാ', 'ി', 'ീ', 'ു', 'ൂ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ']


def checkBound(word , pos):
    if pos < 0 or pos > len(word):
        raise ValueError('position out of bound')

# Lopa Sandhi 

def sandhi_1(word , pos):
    return word[pos - 1] in VOWELSYMBOLS

def transi_1(word , pos):
    checkBound(word , pos)
    first = word[:pos - 1] + '്'
    second = vowel(word[pos - 1]) + word[pos:]
    return [first , second]

# Sandhi for handling ല്ല്

def sandhi_2(word , pos) :
    return word[:pos - 1] == 'അല്ല' or word[:pos -1] == 'ഇല്ല'

def transi_2(word , pos) :
    checkBound(word , pos)
    first = word[:pos - 1]
    second = vowel(word[pos - 1]) + word[pos:]
    return [first , second]

# Aagama Sandhi 1

def sandhi_3(word , pos):
    return (word[pos - 1] not in ['ു' , 'ൂ'] and word[pos] == 'യ') or (word[pos - 1] in ['ു' , 'ൂ'] and word[pos] == 'വ')

def transi_3(word , pos):
    checkBound(word , pos)
    first = word[:pos]
    second = vowel(word[pos+1]) + word[pos+2:]
    return [first , second]

# Sandhi for handling ാ

def sandhi_4(word , pos):
    return word[pos- 1] == 'ാ'

def transi_4(word , pos):
    checkBound(word , pos)
    first = word[:pos-1]
    second = word[pos:]
    return [first , second]

# Aagama Sandhi 2

def sandhi_5(word , pos):
    return word[pos- 1] == 'മ'

def transi_5(word , pos):
    checkBound(word , pos)
    first = word[:pos-1] + 'ം'
    second = vowel(word[pos]) + word[pos+1:]
    return [first , second]

def sandhi_6(word , pos):
    return word[pos-1] == 'ത' and word[pos] == '്' and word[pos+1] == 'ത'
    
def transi_6(word , pos):
    checkBound(word , pos)
    first = word[:pos-1] + 'ം'
    second = vowel(word[pos+2]) + word[pos+3:]
    return [first , second]

word = 'മരത്തിൽ'
checkRule = Rule(sandhi_6 , transi_6)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(word)
    f.write('\n')
    for i in range(len(word)):
        result = checkRule.split(word = word , position = i)
        if result:
            f.write("\n".join(result))  # Write each part on a new line
            f.write("\n")
        else :
            print(i , None)
print("Output written to output.txt")



# 3. Aadesha Sandhi (Substitution)
def aadesha_precondition(word, position):
    return word[position - 1] == "ത" and word[position] == "മ"

def aadesha_transformation(word, position):
    return word[:position - 1] + "ത", word[position:]

# 4. Dwitwa Sandhi (Gemination)
def dwitwa_precondition(word, position):
    return word[position - 1] == word[position]

def dwitwa_transformation(word, position):
    return word[:position], word[position:]

# 5. Guna Sandhi (Strengthening)
def guna_precondition(word, position):
    return word[position - 1] in "അഇ" and word[position] in "ഇ"

def guna_transformation(word, position):
    return word[:position - 1] + "എ", word[position:]

# 6. Vriddhi Sandhi (Enhancement)
def vriddhi_precondition(word, position):
    return word[position - 1] in "അഉ" and word[position] in "ഇ"

def vriddhi_transformation(word, position):
    return word[:position - 1] + "ഓ", word[position:]

# 7. Ayaadi Sandhi
def ayaadi_precondition(word, position):
    return word[position - 1] in "ആ" and word[position] in "അ"

def ayaadi_transformation(word, position):
    return word[:position], word[position:]

# 8. Yan Sandhi
def yan_precondition(word, position):
    return word[position - 1] in "യ" and word[position] in "ഇ"

def yan_transformation(word, position):
    return word[:position], word[position:]

# 9. Antargata Lopa Sandhi
def antargata_lopa_precondition(word, position):
    return word[position - 1] in "അ" and word[position] in "ഉ"

def antargata_lopa_transformation(word, position):
    return word[:position - 1], word[position:]

# 10. Antargata Aagama Sandhi
def antargata_agama_precondition(word, position):
    return word[position - 1] in "അ" and word[position] in "ഋ"

def antargata_agama_transformation(word, position):
    return word[:position], word[position:]

# 11. Antargata Aadesha Sandhi
def antargata_aadesha_precondition(word, position):
    return word[position - 1] == "ദ" and word[position] == "ആ"

def antargata_aadesha_transformation(word, position):
    return word[:position - 1] + "ദ", word[position:]

# 12. Dheerga Sandhi (Elongation)
def dheerga_precondition(word, position):
    return word[position - 1] in "അഇ" and word[position] in "ആഇ"

def dheerga_transformation(word, position):
    return word[:position - 1] + word[position - 1], word[position:]

# 13. Samprasaara Sandhi
def samprasaara_precondition(word, position):
    return word[position - 1] in "ന" and word[position] in "അ"

def samprasaara_transformation(word, position):
    return word[:position], word[position:]

# 14. Sakaara Sandhi
def sakaara_precondition(word, position):
    return word[position - 1] == "സ" and word[position] in "അഇഉ"

def sakaara_transformation(word, position):
    return word[:position], word[position:]

# 15. Jihvamuliya Sandhi
def jihvamuliya_precondition(word, position):
    return word[position - 1] == "ങ" and word[position] == "ക"

def jihvamuliya_transformation(word, position):
    return word[:position], word[position:]

# 16. Upadhmaaniya Sandhi
def upadhmaaniya_precondition(word, position):
    return word[position - 1] == "പ" and word[position] in "അ"

def upadhmaaniya_transformation(word, position):
    return word[:position], word[position:]

# 17. Chandassu Sandhi
def chandassu_precondition(word, position):
    return word[position - 1] == "അ" and word[position] == "ഇ"

def chandassu_transformation(word, position):
    return word[:position - 1] + "ഐ", word[position:]

# 18. Ardhachandra Sandhi
def ardhachandra_precondition(word, position):
    return word[position - 1] == "പ" and word[position] == "അ"

def ardhachandra_transformation(word, position):
    return word[:position], word[position:]

# 19. Paarshvika Sandhi
def paarshvika_precondition(word, position):
    return word[position - 1] == "ദ" and word[position] == "അ"

def paarshvika_transformation(word, position):
    return word[:position], word[position:]

# 20. Anunasika Sandhi
def anunasika_precondition(word, position):
    return word[position - 1] == "ം" and word[position] == "ജ"

def anunasika_transformation(word, position):
    return word[:position], word[position:]

