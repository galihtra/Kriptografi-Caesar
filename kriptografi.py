import string

# ciphertext = (plaintext + key) % 26
def encrypt(data,key):    
    result = ""    
    for x in range(len(data)):        
       if data[x].isupper():            
          caesar = string.ascii_uppercase.index(data[x]) + key            
          caesar = caesar % 26            
          result += string.ascii_uppercase[caesar]        
       elif data[x].islower():            
          caesar = string.ascii_lowercase.index(data[x]) + key            
          caesar = caesar % 26            
          result += string.ascii_lowercase[caesar]        
       else:            
          result += data[x]    
    return result

# plaintext = (ciphertext - key) % 26
def decrypt(data,key):    
    result = ""    
    for x in range(len(data)):        
       if data[x].isupper():            
          caesar = string.ascii_uppercase.index(data[x]) - key            
          caesar = caesar % 26            
          result += string.ascii_uppercase[caesar]        
       elif data[x].islower():            
          caesar = string.ascii_lowercase.index(data[x]) - key            
          caesar = caesar % 26            
          result += string.ascii_lowercase[caesar]        
       else:            
          result += data[x]    
    return result

print(encrypt("Galih!", 3))    
print(decrypt("Jdolk!", 3))    
            