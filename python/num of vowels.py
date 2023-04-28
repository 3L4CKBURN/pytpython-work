def count_vowels(string):
    
    vowels = set("aeiouAEIOU")
   
    count = 0
  
    for char in string:
      
        if char in vowels:
           
            count += 1
    return count


string = "Hello World"
print(count_vowels(string)) 
