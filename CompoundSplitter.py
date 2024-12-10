class CompoundWordSplitter:
    def __init__(self, lexicon):
        from Rules import SandhiRules
        self._lexicon = lexicon  
        self._rules = SandhiRules()      
        self._components = []

    def isValidWord(self, word):
        return word in self._lexicon

    def split(self , word):
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


