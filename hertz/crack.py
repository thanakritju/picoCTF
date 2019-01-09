import sys
with open(sys.argv[1], 'r') as f:
    ciphertext = f.read()

sub={
    'u':'E',
    'b':'T',
    'm':'H',
    'c':'R',
    'i':'S',
    'y':'F',
    'w':'L',
    'g':'A',
    'n':'G',
    't':'U',
    'v':'B',
    'l':'C',
    'h':'I',
    'e':'P',
    's':'O',
    'a':'N',
    'd':'Y',
    'x':'V',
    'q':'D'

}
text=''
ciphertext = ciphertext.replace("Let's decode this now!","").lower()
for c in ciphertext:
    if c in sub:
        c = c.replace(c,sub[c])
    text += c
print(text.lower())


sub_history ={
        'c':'V',
        'w':'Y',
        'a':'F',
        'n':'L',
        'j':'E',
        'q':'T',
        'l':'O',
        'k':'S',
       's':'I',
       'd':'A',
       'f':'N',
       'v':'R',
       'r':'H',
       'p':'C',
       'g':'P',
       'h':'U',
       't':'B',
       'x':'G',
        }
