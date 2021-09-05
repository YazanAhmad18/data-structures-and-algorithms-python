from hash_table.hash_table import Hashtable

def repeated_word(string):
    """
    Write a function called repeated word that finds the first word to occur more than once in a string
    Arguments:
        string: a string
    Returns: string
    """

    if not string  :
        return "there is no string (empty)"

    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("-", "")
    string = string.lower()

    list_sample_words = string.split()

    new_hashtable = Hashtable()

    for word_smaple in list_sample_words:

        if new_hashtable.contains(word_smaple):
            return word_smaple

        else:
            new_hashtable.add(word_smaple, word_smaple)

    return "there is no duplicate word or reapeted word"


if __name__ == "__main__":
    string_test1 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."
    print(f"{repeated_word(string_test1)}")

    string_test2 = "Once upon a time, there was a brave princess who..."
    print(f"{repeated_word(string_test2)}")

    string_test3 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print(f" {repeated_word(string_test3)}")

