from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

input_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize', 'possibly', 'provision', 'hospital', 'kept', 'scratchy',
'code']

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

stemmer_names = ['PORTER', 'LANCASTER', 'SNOWBALL']
formatted_text = '{:>16}' * (len(stemmer_names)+1)
print('\n', formatted_text.format('INPUT WORD', *stemmer_names), '\n', '='*68)

for word in input_words:
    output=[word, porter.stem(word), lancaster.stem(word), snowball.stem(word)]
    print(formatted_text.format(*output))

    
###########결과###############
    INPUT WORD          PORTER       LANCASTER        SNOWBALL 
 ====================================================================
         writing           write            writ           write
          calves            calv            calv            calv
              be              be              be              be
         branded           brand           brand           brand
           horse            hors            hors            hors
       randomize          random          random          random
        possibly         possibl            poss         possibl
       provision          provis          provid          provis
        hospital          hospit          hospit          hospit
            kept            kept            kept            kept
        scratchy        scratchi        scratchy        scratchi
            code            code             cod            code

            
