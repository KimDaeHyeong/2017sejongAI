from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer

input_text = "Do you know how tokenization works? It's actually quite interesting! Let's analyze a couple of sentences and figure it out."

print("\nSentence Tokenizer:")
print(sent_tokenize(input_text))

####결과####
Sentence Tokenizer:
['Do you know how tokenization works?', "It's actually quite interesting!", "Let's analyze a couple of sentences and figure it out."]


print("\nWord tokenizer : ")
print(word_tokenize(input_text))
#########결과########
['Do', 'you', 'know', 'how', 'tokenization', 'works', '?', 'It', "'s", 'actually', 'quite', 'interesting', '!', 'Let', "'s", 'analyze', 'a', 'couple', 'of', 'sentences', 'and', 'figure', 'it', 'out', '.']



print("\nWord Punct Tokenizer : ")”)
print(WordPunctTokenizer().tokenize(input_text))
######결과######
Word Punct Tokenizer :
['Do', 'you', 'know', 'how', 'tokenization', 'works', '?', 'It', "'", 's', 'actually', 'quite', 'interesting', '!', 'Let', "'", 's', 'analyze', 'a', 'couple', 'of', 'sentences', 'and', 'figure', 'it', 'out', '.']

