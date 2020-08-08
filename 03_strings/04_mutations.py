def mutate_string(string, position, character):
    
    position = int(position)
    
    l = list(string)
    l[position] = character
    string = ''.join(l)

    return string