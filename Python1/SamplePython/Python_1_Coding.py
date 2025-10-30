
a="rat"
b="tar"

if len(a)==len(b):
    x=0
    for i in a:
        if i in b:
         x=x+1
        else:
         x=x-1
    if x==len(b):
         print(f"Anagram by words {x}")
else: 
    print("Not Anagram")