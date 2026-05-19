text = "aabbcddee"
freq = {}
for  ch in  text:
    freq[ch] = freq.get(ch, 0) + 1
for ch in text:
    if freq[ch] == 1:
        print(ch)
        break
else:
    print("No non-repeating character found")