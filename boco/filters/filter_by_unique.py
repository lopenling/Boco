def filter_by_unique(results):

    '''Takes in results and gives just the uniques in return.
   
    results | list | list of lists, where each list is a result from a search
    '''

    temp = []

    for i in results:

        temp.append(','.join(i))

    return [i.split(',') for i in set(temp)]