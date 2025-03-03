def score_words(words):
    score = 0
    array = ["a", "e", "i", "o", "u", "y"]
    for word in words:
        letra = 0
        for letter in word:
            if letter in array:
                letra += 1
        if letra % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))