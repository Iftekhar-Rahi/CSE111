def vowel_counter(name):
    s=""
    final=""
    vowel="AEIOU"
    for i in name:
        if i.upper() in vowel:
            s+=i.lower()
    for j in s:
        final+=j
        final+=","
    really_final=final[: -1:]
    number=len(s)
    if number!=0:
      print(f"Vowels: {really_final}. Total number of vowels is {number}")
    else:
      print("No vowels in the name")
    return
vowel_counter("Ishrak Jahan Ema")