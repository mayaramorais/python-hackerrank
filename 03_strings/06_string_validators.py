string = input()

def isalnum_string(s):
  count = 0
  for i in s: 
    if (i.isalnum()) == True: 
        count+=1
  if count > 0:
    return True
  else: return False

print(isalnum_string(string))

def isalpha_string(s):
  count = 0
  for i in s: 
    if (i.isalpha()) == True: 
        count+=1
  if count > 0:
    return True
  else: return False

print(isalpha_string(string))

def isdigit_string(s):
  count = 0
  for i in s: 
    if (i.isdigit()) == True: 
        count+=1
  if count > 0:
    return True
  else: return False

print(isdigit_string(string))

def islower_string(s):
  count = 0
  for i in s: 
    if (i.islower()) == True: 
        count+=1
  if count > 0:
    return True
  else: return False

print(islower_string(string))

def isupper_string(s):
  count = 0
  for i in s: 
    if (i.isupper()) == True: 
        count+=1
  if count > 0:
    return True
  else: return False

print(isupper_string(string))