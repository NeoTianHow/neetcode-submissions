# Question: Maximum Number of Words in a Sentence
#
# You would like to find the sentence containing the largest number of words
# in some given text.
#
# The text is specified as a string S consisting of N characters:
# letters, spaces, dots (.), question marks (?) and exclamation marks (!).
#
# The text can be divided into sentences by splitting it at dots, question
# marks and exclamation marks. A sentence can be divided into words by
# splitting it at spaces.
#
# A sentence without words is valid, but a valid word must contain at least
# one letter.
#
# Example 1:
# S = "We test coders. Give us a try?"
#
# Sentences:
# "We test coders"  -> 3 words
# " Give us a try" -> 4 words
# ""                -> 0 words
#
# Output: 4
#
# Example 2:
# S = "Forget  CVs..Save time . x x"
#
# Sentences:
# "Forget  CVs" -> 2 words
# ""            -> 0 words
# "Save time "  -> 2 words
# " x x"        -> 2 words
#
# Output: 2
#
# Write a function that, given a string S, returns the maximum number of
# words found in a single sentence.
#
# Constraints:
# - 1 <= len(S) <= 100
# - S contains only:
#   - lowercase and uppercase letters
#   - spaces
#   - dots
#   - question marks
#   - exclamation marks
#
# Focus on correctness. Performance is not the main focus.


def splitSolution(text):
    # Standardise all sentence-ending punctuation.
    text = text.replace("?", ".")
    text = text.replace("!", ".")

    # Divide the text into individual sentences.
    sentences = text.split(".")

    maximumWordCount = 0

    for sentence in sentences:
        # split() ignores leading, trailing and repeated spaces.
        words = sentence.split()
        wordCount = len(words)

        # Alternative manual approach:
        # words = sentence.split(" ")
        # wordCount = 0
        #
        # for word in words:
        #     if word != "":
        #         wordCount += 1

        maximumWordCount = max(maximumWordCount, wordCount)

    return maximumWordCount


def scanSolution(text):
    currentWordCount = 0
    maximumWordCount = 0
    insideWord = False

    for char in text:
        if char.isalpha():
            # A letter starts a new word only when we are
            # currently outside a word.
            if not insideWord:
                currentWordCount += 1
                insideWord = True

        elif char == " ":
            # A space ends the current word.
            insideWord = False

        elif char in ".?!":
            # Sentence-ending punctuation ends the current sentence.
            maximumWordCount = max(maximumWordCount, currentWordCount)

            # Reset the counters for the next sentence.
            currentWordCount = 0
            insideWord = False

    # Handle a final sentence without punctuation.
    maximumWordCount = max(maximumWordCount, currentWordCount)

    return maximumWordCount


def testCase(text, expected):
    actual = scanSolution(text)
    result = "PASS" if actual == expected else "FAIL"

    print(result)
    print(f"Input:    {text!r}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print()


testCase("We test coders. Give us a try?", 4)
testCase("Forget  CVs..Save time . x x", 2)

# Extra test cases
testCase("Hello", 1)
testCase("One two three!", 3)
testCase("Hi!A B C?D E.", 3)
testCase(" . ! ?", 0)
testCase("A  B   C. D", 3)
testCase("What? Really! Yes.", 1)
testCase("One sentence without punctuation", 4)
