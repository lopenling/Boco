class CorpusBuilder:
    
    '''For creating a corpus object with ability to load a corpus from file,
    save corpus to a file, add texts to corpus, and remove texts from corpus.'''
    
    def __init__(self):

        '''Creates an empty corpus structure.'''

        self.data = {}
        self.data['texts'] = {}
        self.data['meta'] = {}

    def load_corpus_from_file(self, dir_path):

        '''Load corpus from file
        
        load_from_dir | None or str | if None, creates empty corpus

        NOTE: if load_from_dir is not None, the given path is expected
        to contain both corpus.texts.pkl and corpus.meta.pkl files.
        '''

        import pickle

        if dir_path.endswith('/') is False:
            dir_path = dir_path + '/'

        with open(dir_path + 'corpus.texts.pkl', 'rb') as f:    
            self.data['texts'] = pickle.load(f)
        
        with open(dir_path + '/corpus.meta.pkl', 'rb') as f:
            self.data['meta'] = pickle.load(f)

    def save_corpus_to_file(self, corpus, dir_path):

        '''Saves corpus to file.
        
        corpus | CorpusBuilder | corpus to save
        dir_path | str | path to directory to save corpus to
        '''

        import pickle

        if dir_path.endswith('/') is False:
            dir_path = dir_path + '/'

        f = open(dir_path + 'corpus.texts.pkl', 'wb')
        pickle.dump(corpus.texts, f)
        f.close()
            
        f = open(dir_path + 'corpus.meta.pkl', 'wb')
        pickle.dump(corpus.meta, f)
        f.close()

    def add_texts_to_corpus(self, file_paths, labels=None):
        
        '''
        
        For adding one or more texts at a time to the corpus.
        Texts will be added with source strings and their tokens.
        
        text | str or list | a string or list with one or more file paths
        label | None, str or list | if None, labels will be taken from filenames
        
        NOTE: Filenames are expected to follow the pattern filename.txt

        '''

        if isinstance(file_paths, str):
            file_paths = [file_paths]

        if isinstance(labels, str):
            labels = [labels]

        if len(file_paths) != len(labels):
            raise ValueError("Number of texts and labels must be equal.")

        from tqdm import tqdm

        from bokit import Tokenize
        tokenize = Tokenize()

        # if labels are not provided, take from filenames
        if labels is None:
            labels = []

            # this assumes the file to be named like label.txt or issue might arise
            for text_path in file_paths:
                labels.append(text_path.split('/')[-1].split('.')[0].strip())

        # go through texts one-by-one
        for i, text in enumerate(tqdm(file_paths)):
        
            # add new text to corpus
            self.data['texts'][labels[i]] = {}
            self.data['meta'][labels[i]] = {}
            
            # read the text into a list
            data = open(text)
            data = data.read()

            from bokit.utils import clean_tibetan_string
            data = clean_tibetan_string(data, True, True, True)

            self.data['texts'][labels[i]]['segments'] = data

            # create place for tokens and tokenizer output
            self.data['texts'][labels[i]]['tokens'] = []
            self.data['meta'][labels[i]]['tokenizer_output'] = []

            for ii in range(len(self.data['texts'][labels[i]]['segments'])):

                tokenizer_output = tokenize.query(self.data['texts'][labels[i]]['segments'][ii], True, True)
                
                self.data['meta'][labels[i]]['tokenizer_output'].append(tokenizer_output)
            
                just_tokens = [ii['text'] for ii in tokenizer_output]

                # add tseg to last item of each list of tokens
                just_tokens[-1] = just_tokens[-1] + '་'

                # add to corpus
                self.data['texts'][labels[i]]['tokens'].append(just_tokens)
            
            from .utils._add_pos import _add_pos
            self.data['meta'][labels[i]]['pos'] = _add_pos(self.data['meta'][labels[i]]['tokenizer_output'])

    def remove_text_from_corpus(self, label):
        
        '''Removes text from corpus.

        label | str | label of text to remove
        '''
        
        self.data['texts'].pop(label)
        self.data['meta'].pop(label)
     
        return "Removed " + label
