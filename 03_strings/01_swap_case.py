def swap_case(s):
  
    result_string = ""
    len_string = len(s)
    
    for i in range(len_string):
        if s[i].islower():
            result_string = result_string + s[i].upper()
        else:
            result_string = result_string + s[i].lower()
            
    return result_string