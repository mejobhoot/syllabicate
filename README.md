# syllabicate
Python code for rule based syllabication of English words 

How to call:  
import syllabicator   
syllables = syllabicator.fSyllabicate(text)   

where text is a word that you want to syllabicate. With text = 'guru', the response (syllables) is a list of syllables ['gu', 'ru'].


Rules to syllabicate:   
Rules were considered from this --> https://stackoverflow.com/questions/10565544/how-to-understand-and-add-syllable-break-in-this-example 
1. Two consonants between two vowels VCCV - split between them VC-CV as in cof-fee, pic-nic, except the "cluster consonant" that represents a single sound: meth-od, Ro-chester, hang-out.  
2. Three or more consonants between the vowels VCCCV - split keeping the blends together as in mon-ster or child-ren (this seems the most difficult as you cannot avoid a dictionary).  
3. One consonant between two vowels VCV - split after the first vowel V-CV as in ba-con, a-rid. 
4. The rule above also has an exception based on blends: cour-age, play-time  
5. Two vowels together VV - split between, except they represent a "cluster vowel": po-em, but glacier, earl-ier  
