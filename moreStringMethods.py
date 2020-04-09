# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:11:57 2020

@author: hsn
"""

sherlock = '''Mr. Sherlock Holmes

IN THE year 1878 I took my degree of Doctor of Medicine of the University of London, 
and proceeded to Netley to go through the course prescribed for surgeons in the Army. 
Having completed my studies there, I was duly attached to the Fifth Northumberland 
Fusiliers as assistant surgeon. The regiment was stationed in India at the time, 
and before I could join it, the second Afghan war had broken out. On landing at Bombay, 
I learned that my corps had advanced through the passes, and was already deep in the enemy's 
country. I followed, however, with many other officers who were in the same situation 
as myself, and succeeded in reaching Candahar in safety, where I found my regiment, 
and at once entered upon my new duties.

The campaign brought honours and promotion to many, but for me it had nothing but 
misfortune and disaster. I was removed from my brigade and attached to the Berkshires,
with whom I served at the fatal battle of Maiwand. There I was struck on the shoulder 
by a Jezail bullet, which shattered the bone and grazed the subclavian artery. 
I should have fallen into the hands of the murderous Ghazis had it not been for 
the devotion and courage shown by Murray, my orderly, who threw me across a 
packhorse, and succeeded in bringing me safely to the British lines.
'''
newPassage = sherlock.split()
print(newPassage)

for i in range(len(newPassage)):
    newPassage[i] = newPassage[i].strip('.')    # strip() method removes all char in paranthesis
print(newPassage)

print('Sherlock' in newPassage) # Searching string
