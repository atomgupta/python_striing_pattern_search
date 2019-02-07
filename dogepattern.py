{
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1
        
if __name__=='__main__':
    main()
}
def doge_count(str):
    count=0
    alphabet = []
    for letter in range(97,123):
        alphabet.append(chr(letter))
 
    for i in range(0,len(str)-3):
        if(str[i]=='d' and str[i+1]=='o' and str[i+2] in alphabet and str[i+3]=='e'):
            count+=1                   
    return count