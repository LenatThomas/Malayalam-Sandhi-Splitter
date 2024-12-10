class CompoundWordSplitter:
    def __init__(self, lexicon):
        """Takes the lexicon as the input. Uses the lexicon to find the individual composing the compound word

        Args:
            lexicon (list): Lexicon contatining the base words in malayalam.
        """

        from Rules import SandhiRules
        self._lexicon = lexicon  
        self._rules = SandhiRules()      
        self._components = []

    def isValidWord(self, word):
        """Checks if the word is in the Lexicon

        Args:
            word (str): Word to check

        Returns:
            bool: returns True if valid
        """

        return word in self._lexicon

    def split(self , word):
        """Splits the compound word into individual words

        Args:
            word (str): The word to be split

        Returns:
            list: List containing the individual words composing the compound word. Returns the word itself if the word is a valid word.
        """
        
        self._components = []
        w = word
        if w in self._lexicon :
            return [w]
        while True :
            self._rules.updateWord(w)
            flag = False
            for i in range(1, len(w)):
                results = self._rules[i]
                if len(results) == 0:
                    continue
                for r in results :
                    c , s = r
                    if self.isValidWord(c):
                        self._components.append(c)
                        if self.isValidWord(s):
                            self._components.append(s)
                            return self._components
                        else :
                            w = s
                            flag = True
                            break
                if flag :
                    flag = False
                    break
        
            if i == len(w) - 1:
                self._components.append(s)
                break

        return self._components


