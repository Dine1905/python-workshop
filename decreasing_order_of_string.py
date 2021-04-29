def descOrder(s):
    s.sort(reverse = True)
    str1 = ''.join(s)
    print(str1)
 
def main():
    s = list('dineshkumar')
     
    # function call
    descOrder(s)
 
if __name__=="__main__":
    main()
