word = input()
word_count = int(input())


def repeat(text, text_count):
    return text * text_count


result = repeat(word, word_count)

print(result)

# With LAMBDA
#
# word = input()
# word_count = int(input())
#
# repeated_string = lambda x, y: x * y
#
# result = repeated_string(word, word_count)
#
# print(result)
