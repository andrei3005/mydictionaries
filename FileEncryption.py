codes={'A':'%','a':'9','B':'@','b':'#','C':'1','c':'2','D':'3','d':'4','E':'5','e':'6','F':'7','f':'8','G':')'
    ,'g':'(','H':'-','h':'*','I':'&','i':'^','J':'$','j':'#','K':'!','k':'@','L':'}','l':'{','M':'[','m':']','N':'?'
    ,'n':'/','O':'>','o':'<','P':'.','p':',','Q':'=','q':'+','R':'_','r':'|','S':'\\','s':'$','T':'€',
    't':'¢','U':'₹','u':'₱','V':'฿','v':'α','W':'β','w':'γ','X':'ε','x':'θ','Y':'κ','y':'μ','Z':'ξ',
    'Z':'π'}

#fname to File_Name
def main():
    Filename=input("Enter Filename:")
    with open(Filename) as f:
      fw=open("encrypted.txt","w")
      for line in f:
        etxt=convert(line)
        fw.write(etxt)
      fw.close()

def convert(s):
    encrypted=""
    for c in s:
        e=codes.get(c,None)
        if e is None:
            
            encrypted+=c
        else:
            
            encrypted+=e
    return encrypted
    
main()


