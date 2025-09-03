class StringTools:
    
    @staticmethod
    def is_palindrome(word):
        if word == word[::-1]:
            return True
        else:
            return False


    @classmethod
    def from_sentence(cls, text)-> list:
        words = text.split()
        return cls(words)

print(StringTools.is_palindrome('level'))
txt = StringTools.from_sentence('I love Python')
print(txt.words)
