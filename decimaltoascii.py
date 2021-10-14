#create ascii to number dictionary
#create script that takes a list of numbers as parameter and converts list to list of ascii characters

#create ascii to number dictionary:

asciilist = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[',"\\",']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
decasciidict = {}

def dict():
    for n in range(32,126):
        decasciidict[str(n)]=asciilist[n-33]
    return decasciidict

def dectoascii(list):
    flag = ""
    for n in list:
        flag = flag + decasciidict[str(n)]
    print(flag)

dict()
dectoascii([112,105,99,111,67,84,70,123,103,48,48,100,95,107,49,116,116,121,33,95,110,49,99,51,95,107,49,116,116,121,33,95,57,98,51,98,55,51,57,50,125])