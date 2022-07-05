# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i
# Example 2:

# Input:
# S = pqr.mno
# Output: mno.pqr
# Explanation: After reversing the whole
# string , the input string becomes
# mno.pqr

data = input("Enter a stentence without spacing seperated by "." (dots), eg: what.is.your.name")

class Reverser:
    
    def reversed1(self,string):
        
        split_string = string.split(".")
        print(split_string) 
        reversed_string = split_string[::-1]
        print(reversed_string)
        joined = reversed_string[0]
        for i in range(1, len(reversed_string)):
            joined += "."+reversed_string[i]
        print(joined)
        
        
        
if __name__ == '__main__':
    obj1 = Reverser()
    obj1.reversed1(data)
     
        
