def get_word_score(word):
        
    alphabet_dict = {chr(65 + i): i + 1 for i in range(26)}
    score = sum([alphabet_dict[letter] for letter in word.upper()])
    return score