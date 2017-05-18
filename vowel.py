"""
@file : vowel.py
@brief: the program to print vowels and consonant letters from 'gnulinux
@authore: deepti
@date:18-may-17
"""





string = 'gnulinux'

for vowel in range(len(string)) :
    if ((string[vowel] =='a') or (string[vowel] =='A') or (string[vowel] =='e') or 
        (string[vowel] =='E') or (string[vowel] =='i') or (string[vowel] =='I') or 
        (string[vowel] =='o') or (string[vowel] =='O') or (string[vowel] =='u') or (string[vowel] =='U')):
        print "%c is vowel"%(string[vowel])
    else:
        print "%c is not a vowel"%(string[vowel])


#consonant letters
string = 'gnulinux'

for consonant in range(len(string)) :
    if ((string[consonant] !='a') or (string[consonant] !='A') or (string[consonant] !='e') or
        (string[consonant] !='E') or (string[consonant] !='i') or (string[consonant] !='I') or
        (string[consonant] !='o') or (string[consonant] !='O') or (string[consonant] !='u') or (string[consonant] !='U')):
        print "%c is consonant "%(string[consonant])
    else:
        print "%c is not a consonant"%(string[consonant])
                                                            

