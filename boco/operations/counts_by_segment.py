def counts_by_segment(corpus, n=100):

    '''Returns a dictionary of the most frequent tokens in the corpus.
    
    corpus | CorpusBuilder | corpus to search
    n | int | number of results to return
    '''

    import signs
    from itertools import islice
    
    segments = []

    for key in corpus.data['texts'].keys():
        segments = segments + corpus.data['texts'][key]['segments']
    
    describe = signs.Describe(segments)
    counts = describe.get_counts()
    items = counts.items()
    counts = dict(islice(items, n))

    return counts
