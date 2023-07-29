def filter_by_pos(tokens, posses, part_of_speech):
    
    '''Takes in tokens and pos data for a given text
    from the corpus object.
    
    tokens | list of lists | the text presented as tokens
    posses | list of lists | the text presented as pos information
    part_of_speech | str | the part of speech to filter with (e.g. 'NOUN')
    '''

    out = []

    # iterate through set of posses
    for segment_i, segment_posses in enumerate(posses):

        out_temp = []

        for token_i, token_pos in enumerate(segment_posses):
            
            if token_pos == part_of_speech:
                out_temp.append(tokens[segment_i][token_i])
            
            else:
                out_temp.append('')

        out.append(out_temp)
        
    return out