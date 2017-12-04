class Palindrome:

    @staticmethod
    def is_palindrome(word):
        s=''
        stack = []
        for char in word.lower():
            stack.append(char)
        for i in range(len(word)):
            s = s+stack.pop()
        return s==word.lower()    
            
            

print(Palindrome.is_palindrome('Deleveled'))