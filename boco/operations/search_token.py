def search_token(corpus, token, unique=False):

    '''Performs a token search in the entire corpus.
    
    token | str | token to search for
    unique | bool | if True, returns only unique results
    '''

    out = []
    
    # iterate through all the texts in the corpus
    for text in corpus.data['texts'].keys():
    
        # iterate through all the segments in the text
        for segment in corpus.data['texts'][text]['tokens']:
            if token in segment:
                out.append([''.join(segment), text])

    if unique:

        from boco.filters.filter_by_unique import filter_by_unique
        return filter_by_unique(out)

    return out