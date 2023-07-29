def _add_pos(tokenizer_output):

    '''Helper function for adding various meta 
    values to the corpus from the tokenizer output.
    
    tokenizer_output | list | output from tokenizer
    '''

    # iterate through the tokenizer output for each string in a text
    text_level = []

    for segment in tokenizer_output:
        
        segment_level = []
        
        for token in segment:

            # if no pos tag is available, add NOT_AVAILABLE            
            if len(token['pos']) == 0:
                segment_level.append('NOT_AVAILABLE')
            # otherwise add the pos tag
            else:
                segment_level.append(token['pos'])

        text_level.append(segment_level)

    return text_level
