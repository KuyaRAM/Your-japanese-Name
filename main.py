inp = input("What's your name? ")

name = inp.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

double_letter = tuple([i*2 for i in alphabet])

consonant = tuple([i for i in alphabet if i not in "aiueo"])

abc = tuple(alphabet)

exc = ("wi","vi","ph","ds","uc","l","ck","v","sch","ing","ny","ä","ü","ö","q","j","c","tz","gh","th")

ins = ("bi","bi","f","ts","us","r", "k", "w","sh","in","nu","e","u","o","k","y","k","z","h","s")

combination_exc = ("nb","sh","nd","nt","np","ts","ya","yu","yo")

for i in double_letter:
  if i in name:
    name = name.replace(i,i[0])

end_exc = ("er","de","ke")
end_ins = ("a","d","k")
end_u_exc = ("h","n")


for i, exc_ in enumerate(end_exc):
  if name.endswith(exc_):
    name = name.replace(exc_,end_ins[i])


for i, exc_ in enumerate(exc):
  if exc_ in name:
    name = name.replace(exc_, ins[i])


def get_pos(combination):
  pos = name.index(combination) + 1
  return pos


def y_combo_tester(y_combo,name):  
  if y_combo in name:
    pos = get_pos(y_combo)
    try:
      y_combo_test = name[pos] + name[pos+1]
    except:
      y_combo_test = y_combo
    
    return y_combo_test


for i in abc:
  y_combo = i + "y"
  y_combo2 = "y" + i
  
  if y_combo_tester(y_combo,name) not in combination_exc:
    while y_combo in name:
      pos = get_pos(y_combo)
      name = name[:pos]+"i"+name[(pos+1):]
  
  elif y_combo2 not in combination_exc:
    while y_combo2 in name:
      pos = get_pos(y_combo)
      name = name[:(pos)-1]+"i"+name[pos:]


for _ in range(2):
  for combination_1 in range(len(consonant)):
    for i in consonant:
      combination = i + consonant[combination_1 ]
      
      if combination not in combination_exc:
        while combination in name:
          if combination.endswith("h"):
            pos = get_pos(combination)
            name = name[:pos] + name[(pos+1):]
          
          elif combination.startswith("h"):
            pos = get_pos(combination)
            name = name[:(pos-1)] + name[pos:]
          
          else:
            pos = get_pos(combination)
            name = name[:pos] + "u" + name[pos:]


if name.endswith(consonant):
  if not name.endswith(end_u_exc):
    name += "u"


print()
print("Your name in English:",inp)
print("Your name in Japanese:",name)