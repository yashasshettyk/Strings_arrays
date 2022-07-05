data = "what.is.your.name.please.tell.me"

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
     
        
