answers = []
wordle = "steak"
for x in range(4):
    n = ""
    word = input("\033[37mwordle: \033[37m")
    if word == wordle:
        for x, y in zip(word, wordle):
            if x == y:
                n += '\033[92m' + x + '\033[0m'
            elif x in wordle:
                n += "\033[34m" + x + "\033[34m"
            else: n+=x
        print(n)
        break
    elif len(word) == len(wordle):
        for x, y in zip(word, wordle):
            if x == y:
                n += '\033[92m' + x + '\033[0m'
            elif x in wordle:
                n += "\033[34m" + x + "\033[34m"
            else: n+=x
    else: print("Answer must be 5 letters")
    answers.append(n)
    for s in answers:
        print(s,"")
