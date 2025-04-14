
def word_intersection():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    # Convert each word to a set of characters and compute the intersection
    common_letters = set(word1.lower()) & set(word2.lower())
    print("Common letters between the two words:", common_letters)

if __name__ == "__main__":
    word_intersection()