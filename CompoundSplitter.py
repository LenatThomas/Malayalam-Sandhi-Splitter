class CompoundWordSplitter:
    def __init__(self, lexicon):
        from Rules import SandhiRules
        self._lexicon = lexicon  
        self._rules = SandhiRules()      
        self._components = []
        self._tree       = []

    def isValidWord(self, word):
        return word in self._lexicon

    def split(self, word):
        self._rules.updateWord(word)
        splits = self._recursiveSplit(word)
        return splits if splits else [word]
    

    def temp(self, word):
        from Rules import SandhiRules
        self._tree.append(word)
        while len(self._tree) > 0:
            w = self._tree.pop()
            rule = SandhiRules
            rule.updateWord(w)
            for i in range(1 , len(w)):
                possibleSplits = rule[i]
                for split in possibleSplits:
                    first, second = split

                    if self.isValidWord(first):
                        self._components.append(first)
                        if self.isValidWord(second):
                            self._components.append(second)
                        else : 
                            self._tree.append(second)

                        return [first, second]

    def _recursiveSplit(self, word):
        for i in range(1, len(word)):
            possibleSplits = self._rules[i]
            for split in possibleSplits:
                first, second = split
                if self.isValidWord(first):
                    self._components.append(first)
                    if self.isValidWord(second):
                        self._components.append(second)
                        return None
                    else : 
                        self._tree

                    return [first, second]
        return None


