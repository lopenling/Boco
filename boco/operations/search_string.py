def search_string(corpus, string, padding=None, unique=False):

    '''Performs a string search in the entire corpus.
    
    string | str | string to search for
    padding | int | pads the segment with n segments before and after
    unique | bool | if True, returns only unique results
    '''

    out = []
    
    # iterate through all the texts in the corpus
    for text in corpus.data['texts'].keys():
        
        # iterate through all the segments in the text
        segments = corpus.data['texts'][text]['segments']
        for i, segment in enumerate(segments):
            
            if string in segment:

                if padding is None:
                    out.append([segments[i], text])
                
                else:
                    out.append(['་ '.join(segments[i-padding:i+padding+1]), text])

    if unique:

        from corpus_manager.filters.filter_by_unique import filter_by_unique
        return filter_by_unique(out)

    return out
