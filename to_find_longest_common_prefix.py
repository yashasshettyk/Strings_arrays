class longestprefixsolution:
    def prefixsolution(self,array):
        if len(array)==0:
            return -1
        final = ""
        minlen = len(array[0])
        for i in range(len(array)):
            minlen = min(len(array[i]), minlen)
        for i in range(minlen):
            char = array[0][i]
            for j in range(len(array)):
                if char != array[j][i]:
                    return -1
            final+=char
            
        return final
    
    
if __name__ == "__main__":
    object1 = longestprefixsolution()
    print(object1.prefixsolution([input("Enter strings : ") for i in range(4)]))
        
        
        
