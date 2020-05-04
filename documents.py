import spacy
from collections import Counter, defaultdict

class DocumentWizard:
    
    def __init__(self, file_path:str):
       
        # Load english package
        self.nlp = spacy.load('en_core_web_sm')
        
        # Load document
        self.file_doc =self.load_document(file_path)


    def load_document(self, file_path:str):
        """
        Load file and create spacy nlp document
        """
        # Load the file
        file_text = open(file_path).read()
        
        # Create nlp instance
        file_doc = self.nlp(file_text)
        
        return file_doc

    def get_sentences(self) -> list:
        """
        Get all sentences of the document
        """
        # gell all sentences and return as list 
        sentences = list(self.file_doc.sents)
        
        return sentences

    def get_word_frequency(self, criteria:list) -> dict:
        """
        Get all interesting words (nouns) and its respective frequencies
        """
        # get frequency for all tokens which matches the criteria
        word_frequency = Counter([token.text for token in self.file_doc 
                if not token.is_stop and not token.is_punct and token.pos_ in criteria])
        
        # unpack results to a dictionary
        word_frequency_dict = {text: freq for text, freq in word_frequency.most_common()}
        
        return word_frequency_dict

    def get_words_frequency_and_sentences(self, word_frequency_dic:dict, text_sentences:list) -> list:
        """
        Match all words and frequencies with document sentences
        """
        word_frequency_sentences_list = []
        
        # join all words with it respective sentences
        for text, freq in word_frequency_dic.items():
            word_frequency_sentences = dict()    
            sentence_list = []
            for sentence in text_sentences:
                if text in sentence.text:
                    sentence_list.append(sentence.text)
            # create report dictionary for word
            word_frequency_sentences = {
                "word": text, "frequency": freq, "sentences": sentence_list }
            word_frequency_sentences_list.append(word_frequency_sentences)
            
        return word_frequency_sentences_list

    def find_interesting_words(self) -> None:
        """
        Find all interesting words (nouns) from document
        """
        
        # get all sentences from the document
        text_sentences = self.get_sentences()
        
        # get all interesting words and frequencies
        word_frequency = self.get_word_frequency(['PROPN', 'NOUN'])
        
        # joing words, frequencies and sentences into a list of dictionaries
        interesting_words = self.get_words_frequency_and_sentences(word_frequency, text_sentences)
                
        return interesting_words
