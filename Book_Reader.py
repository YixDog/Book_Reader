
import string
'''Stopword list.'''
stopwords =['able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', "can't", 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', "c's", 'currently', 'dare', "daren't", 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', "hadn't", 'half', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm", 'immediate', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime', 'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', "mustn't", 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', "needn't", 'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', "one's", 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that's", "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore', 'therein', "there'll", "there're", 'theres', "there's", 'thereupon', "there've", 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's", 'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", 'welcome', 'well', "we'll", 'went', 'were', "we're", "weren't", "we've", 'what', 'whatever', "what'll", "what's", "what've", 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd", 'whoever', 'whole', "who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't", 'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've", 'zero', 'a', "how's", 'i', "when's", "why's", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'I', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 'itse”', 'mill', 'move', 'myse”', 'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah', 'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent', 'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date', 'ed', 'effect', 'et-al', 'ff', 'fix', 'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately', 'importance', 'important', 'index', 'information', 'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line', "'ll", 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref', 'refs', 'related', 'research', 'resulted', 'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state', 'states', 'stop', 'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto', 'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til', 'tip', 'ts', 'ups', 'usefully', 'usefulness', "'ve", 'vol', 'vols', 'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words', 'world', 'youd', 'youre']
'''Controlling input parameters.'''
def Word_Order_Frequency_One_Book(Book,Word_Order,File_Output): 
    try:
        f = open(Book,"r",encoding='utf8')
    except: 
        print("The file is lacking.")
    else:
        '''Reading,removing punctuations,lowering and splitting the book.'''
        f = open(Book,"r",encoding='utf8')
        book_1string = f.read()
        f.close()            
        book_1string = book_1string.translate(str.maketrans('', '', string.punctuation))                
        book_1string = book_1string.lower()
        book_1string = book_1string.split()
        '''Defining important lists and dictionary to keep data.'''
        usedwords =[]
        counters=[]
        wordsandcounters = {}
        output_file = open(File_Output,"w",encoding='utf8')
        '''Finding words and counter numbers for the Word_Order=1 and Word_Order=2.'''
        if(Word_Order==1): 
            for i in range(len(book_1string)):
                counter =1        
                if(book_1string[i] not in usedwords and book_1string[i] not in stopwords):
                    for j in range(i+1,len(book_1string)):  
            
                        if(book_1string[i]==book_1string[j]):
                            counter+=1
                
                    counters.append(counter)
                    usedwords.append(book_1string[i])                        
        elif(Word_Order==2):
            for i in range(len(book_1string)-1):             
                counter =1        
                if(book_1string[i]+" "+book_1string[i+1] not in usedwords and book_1string[i] not in stopwords and book_1string[i+1] not in stopwords):
                    for j in range(i+1,len(book_1string)-1):  
                    
                        if(book_1string[i]+" "+book_1string[i+1]==book_1string[j]+" "+book_1string[j+1]):
                            counter+=1
                
                    counters.append(counter)
                    usedwords.append(book_1string[i]+" "+book_1string[i+1])
        else:
            print("You can just enter 1 or 2.")
        '''Updating and sorting the dictionary which we need.'''                
        for m in range(len(usedwords)): 
            wordsandcounters.update({usedwords[m]:counters[m]})
        wordsandcounters = sorted(wordsandcounters.items(),key=lambda x: x[1],reverse =True)
        '''Printing outputs to output file.
           It can take about 5 minutes for Word_Order=1.
           It can take about 30 minutes for Word_Order=2.'''
        writecounter=0
        output_file.write("| WORD      | WORD     |\n")
        output_file.write("| ORDER     | ORDER    |\n")
        output_file.write("| FREQUENCY | SEQUENCE |\n")
        output_file.write("------------------------\n")
        for n in wordsandcounters:
            output_file.write(n[0])
            if(len(n[0])<17):
                for i in range(17-len(n[0])):
                    if(i+len(n[0])==12):
                        output_file.write("|")
                    else:    
                        output_file.write(" ")
            output_file.write(str(n[1])+"\n")
            writecounter+=1
            if(writecounter==100):            
                break
        output_file.close()
def Word_Order_Frequency_Two_Book(Book_1,Book_2,Word_Order,File_Output):
    '''Controlling input parameters.'''
    try:
        f = open(Book_1,"r",encoding='utf8')
        f_2=open(Book_2,"r",encoding='utf8')
    except: 
        print("The files are lacking.")
    else:
        '''Reading two books and combining them.'''
        f = open(Book_1,"r",encoding='utf8')
        book1_string = f.read()
        f.close()
    
        f_2 = open(Book_2,"r",encoding='utf8')
        book2_string = f_2.read()
        f_2.close()
        combinedbook = book1_string +" "+ book2_string
        ''''Reading,removing punctuations,lowering and splitting the combined book.''' 
        combinedbook = combinedbook.translate(str.maketrans('', '', string.punctuation+"“"))                
        combinedbook = combinedbook.lower()
        combinedbook = combinedbook.split()
        '''Defining important lists and dictionary to keep data.'''
        usedwords =[]
        counters=[]
        wordsandcounters = {}
        output_file = open(File_Output,"w",encoding='utf8')
        '''Finding words and counter numbers for the Word_Order=1 and Word_Order=2.'''
        if(Word_Order==1): 
            for i in range(len(combinedbook)):
                counter =1        
                if(combinedbook[i] not in usedwords and combinedbook[i] not in stopwords):
                    for j in range(i+1,len(combinedbook)):  
            
                        if(combinedbook[i]==combinedbook[j]):
                            counter+=1
                
                    counters.append(counter)
                    usedwords.append(combinedbook[i])   
        elif(Word_Order==2):
            for i in range(len(combinedbook)-1):             
                counter =1        
                if(combinedbook[i]+" "+combinedbook[i+1] not in usedwords and combinedbook[i] not in stopwords and combinedbook[i+1] not in stopwords):
                    for j in range(i+1,len(combinedbook)-1):  
                    
                        if(combinedbook[i]+" "+combinedbook[i+1]==combinedbook[j]+" "+combinedbook[j+1]):
                            counter+=1
                
                    counters.append(counter)
                    usedwords.append(combinedbook[i]+" "+combinedbook[i+1])
        else:
            print("You can just enter 1 or 2.")
        '''Updating and sorting the dictionary which we need.'''                
        for m in range(len(usedwords)): 
            wordsandcounters.update({usedwords[m]:counters[m]})
        wordsandcounters = sorted(wordsandcounters.items(),key=lambda x: x[1],reverse =True)
        book1_string=book1_string.lower()
        book1_string=book1_string.split()
        book1_counter=[]
        hundredwords =0
        '''Finding words which we found in the combined book
           for the Word_Order=1 and Word_Order=2 in the Book1.'''
        if(Word_Order==1): 
            for i in wordsandcounters:
                counter =0       
                
                for j in range(len(book1_string)):  
            
                    if(i[0]==book1_string[j]):
                        counter+=1
                hundredwords+=1
                book1_counter.append(counter)
                if(hundredwords==100):
                    break
        elif(Word_Order==2):
            for i in wordsandcounters:           
                counter =0        
                
                for j in range(len(book1_string)-1):  
                    
                    if(i[0]==book1_string[j]+" "+book1_string[j+1]):
                        counter+=1
                hundredwords+=1
                book1_counter.append(counter)
                if(hundredwords==100):
                    break
        book2_string=book2_string.lower()
        book2_string=book2_string.split()
        book2_counter=[]
        hundredwords =0
        '''Finding words which we found in the combined book
           for the Word_Order=1 and Word_Order=2 in the Book2.'''
        if(Word_Order==1): 
            for i in wordsandcounters:
                counter =0       
                
                for j in range(len(book2_string)):  
                   
                    if(i[0]==book2_string[j]):
                        
                        counter+=1
                        
                hundredwords+=1               
                book2_counter.append(counter)
               
                if(hundredwords==100):
                    break
        elif(Word_Order==2):
            for i in wordsandcounters:           
                counter =0        
                
                for j in range(len(book2_string)-1):  
                    
                    if(i[0]==book2_string[j]+" "+book2_string[j+1]):
                        counter+=1
                hundredwords+=1
                book2_counter.append(counter)
                
                if(hundredwords==100):
                    break
        '''Printing outputs to output file.
           It can take about 20-25 minutes for Word_Order=1.
           It can take about 45 minutes for Word_Order=2.'''
        writecounter=0
        output_file.write("| TOTAL               | BOOK 1    | BOOK 2    | WORD     |\n")
        output_file.write("| ORDER               | ORDER     | ORDER     | ORDER    |\n")
        output_file.write("| FREQUENCY           | FREQUENCY | FREQUENCY | SEQUENCE |\n")
        output_file.write("------------------------------------------------\n")
        for n in wordsandcounters:
            output_file.write(n[0])
            if(len(n[0])<28):
                for i in range(25-len(n[0])):
                    if(i+len(n[0])==22):
                        output_file.write("|")
                    else:    
                        output_file.write(" ")
                        
            output_file.write(str(book1_counter[writecounter]))
            for i in range(15-len(str(book1_counter[writecounter]))):
                if(i+len(str(book1_counter[writecounter]))==8):
                    output_file.write("|")
                else:    
                    output_file.write(" ")
            output_file.write(str(book2_counter[writecounter]))
            
            for i in range(12-len(str(book1_counter[writecounter]))):
                if(i+len(str(book2_counter[writecounter]))==8):
                    output_file.write("|")
                else:    
                        output_file.write(" ")
            output_file.write(str(n[1])+"\n")
            writecounter+=1
            if(writecounter==100):            
                break
        output_file.close()        
                   
                
        
   
    
   

Word_Order_Frequency_Two_Book("C:/Users/yigit/Desktop/hihi.txt","C:/Users/yigit/Desktop/haha.txt",2,"C:/Users/yigit/Desktop/words.txt")
