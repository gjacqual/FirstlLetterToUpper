s = str(input('Enter string: '))
subs = s.split(' ')
newstr = ''
for sub in subs:
   first = sub[:1].upper()
   end = sub[1:]
   sub = first + end
   space = ' '
   newstr = space.join([newstr, sub])
print(newstr)
