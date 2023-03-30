def main():
   text = input ("Word: ")
   

def shorten(word):
    AEIOU = ("AEIOU").lower()
    
    for char in word:
        if char in AEIOU:
            word = word.replace(char, "")
    return word
        
            

if __name__ == "__main__":
    main()


