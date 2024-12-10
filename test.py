from rules import SandhiRules

rule     = SandhiRules()
compound = 'പണിക്കൂലി'

file = open('output.txt' , 'w' , encoding = 'utf-8')

rule.updateWord(compound)
for i in range(len(compound)):
    file.write(str(i) + "\n")
    splits = rule[i]
    for k in splits:
        file.write("\n" + k[0])
        file.write("\n" + k[1])
        file.write("\n")

