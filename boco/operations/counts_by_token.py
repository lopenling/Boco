def counts_by_token(corpus, n=100):

    '''Returns a dictionary of the most frequent segments in the corpus.
    
    corpus | CorpusBuilder | corpus to search
    n | int | number of results to return
    '''

    import signs
    from itertools import islice
    
    tokens = []

    # combine all the tokens from all the texts
    for text in corpus.data['texts'].keys():
        tokens = tokens + [i for ii in corpus.data['texts'][text]['tokens'] for i in ii]
    
    # do the counting
    describe = signs.Describe(tokens)
    counts = describe.get_counts()
    items = counts.items()
    counts = dict(islice(items, n))

    return counts
