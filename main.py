from CompoundSplitter import CompoundWordSplitter


if __name__ == "__main__":

    with open('lexicon.txt', 'r' , encoding = 'utf-8') as f:
        lines = f.readlines()
        lexicon = {word.strip() for line in lines for word in line.split()}

    with open('tests.txt', 'r' , encoding = 'utf-8') as f:
        lines = f.readlines()
        tests = [word.strip() for line in lines for word in line.split()]

    print(len(lexicon))
    print(len(tests))

    splitter = CompoundWordSplitter(lexicon)

    with open('output.txt' , 'w' , encoding = 'utf-8') as f:
        for word in tests:
            result = splitter.split(word)
            f.write(word + "\t=\t")
            f.write(" + ".join(result))
            f.write("\n")
