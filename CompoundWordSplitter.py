class CompoundWordSplitter:
    def __init__(self, lexicon):
        """Takes the lexicon as the input. Uses the lexicon to find the individual composing the compound word

        Args:
            lexicon (list): Lexicon contatining the base words in malayalam.
        """

        from Rules import SandhiRules
        self._lexicon = lexicon  
        self._MORPHEMES = [

        ]
        self._rules = SandhiRules()      
        self._components = []
        self._componentTree = {}

    def isValidWord(self, word):
        """Checks if the word is in the Lexicon

        Args:
            word (str): Word to check

        Returns:
            bool: returns True if valid
        """

        return word in self._lexicon or word in self._MORPHEMES
    
    def split(self , word):
        self.word = word
        self._components = []
        self._componentTree = {}
        if word in self._lexicon or word in self._MORPHEMES:
            return [word]
        self._constructTree()
        self._BackTraceTree([word])
        return self._components

    def _constructTree(self):
        """Splits the compound word into individual words

        Args:
            word (str): The word to be split

        Returns:
            list: List containing the individual words composing the compound word. Returns the word itself if the word is a valid word.
        """
        stack = []
        word = self.word
        stack.append(word)
        while len(stack) > 0:
            segment = stack.pop()
            self._componentTree[segment] = []   
            self._rules.updateWord(word = segment)
            for i in range(len(segment)):
                results = self._rules[i]
                for r in results:
                    c , s = r
                    if self.isValidWord(c):
                        self._componentTree[segment].append([c , s])
                        if not self.isValidWord(s) and len(s) > 3:
                            stack.append(s) 
        
    def _BackTraceTree(self, splits):
        ss = splits[-1]
        keys = self._componentTree.keys()
        if ss not in keys:
            self._components.append(splits)
            return None
        results = self._componentTree[ss]
        for r in results:
            c , s = r 
            newSplit = splits[:-1] + [c , s]
            self._BackTraceTree(newSplit)
            
