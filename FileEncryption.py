codes = {'A':'%','a':'9','B':'@','b':'#','C':'8','c':'*','D':'1','d':'!','E':'2','e':'$','F':'3','f':'^','G':'4','g':'(',
'H':'5','h':')','I':'6','i':'-','J':'7','j':'_','K':'+','k':'=','L':'{','l':'}','M':'[','m':']','N':'<','n':'>','O':',',
'o':'.','P':'?','p':'/','Q':'|','q':':','R':';','r':'€','S':'π','s':'ξ','T':'μ','t':'θ','U':'ε','u':'γ','V':'β','v':'α',
'W':'฿','w':'₱','X':'₹','x':'¢','Y':'~','y':'`','Z':'ᑓ','z':'ᑱ'}

def main():
    Filename = input("Enter Filename of data that needs to be encrypted:")

    with open(Filename) as read_file:
      
      outfile=open("encrypted.txt","w")

      for text in read_file:
        encrypted_text=convert(text)
        outfile.write(encrypted_text)

      outfile.close()

def convert(info_security):
    Encryption=""
    for character in info_security:
        encrypt=codes.get(character,None)
        if encrypt is None:
            
            Encryption+=character
        else:
            
            Encryption+=encrypt
    return Encryption
    
main()


