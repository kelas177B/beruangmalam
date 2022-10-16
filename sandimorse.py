# '/' sebagai pemisah huruf abjad

def to_morse_code(text):
  code = {' ':'|', 'a':'/.-/', 'b':'/-.../', 'c':'/-.-./', 'd':'/-../',  'e':'/./', 'f':'/..-./', 'g':'/--./, 'h':'/..../', 'i':'/../', 'j':'/.---/', 'k':'/-.-/', 'l':'/.-../', 'm':'/--/', 'n':'/-./', 'o':'/---/', 'p':'/.--./', 'q':'/--.-/', 'r':'/.-./', 's':'/.../', 't':'/-/', 'u':'/..-/', 'v':'/...-/', 'w':'/.--/', 'x':'/-..-/', 'y':'/-.--/', 'z':'/--...'}
          
  morse_code = ""
          
  for x in text :
      morse_code += code[x.lower()]
  
  return morse_code
          
text = input("Masukkan huruf: ")
print(to_morse_code(text))
          
