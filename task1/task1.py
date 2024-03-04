import nltk

# nltk.download('punkt')

# text = """NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project."""

text = input("Enter the text: ")


print("""
    Choice number 1: print tokenized words
    Choice number 2: print tokenized sentences
    Choice number 3: print output using split function 
""")

user_input = input("Enter your choice: ")

if user_input == "1":
    words = nltk.word_tokenize(text)
    print(words)
elif user_input == "2":
    sentences = nltk.sent_tokenize(text)
    print(sentences)
elif user_input == "3":
    print(text.split())
else:
    print("Enter a valid choice 1, 2 or 3")
