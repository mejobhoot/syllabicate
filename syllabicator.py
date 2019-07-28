from copy import deepcopy as dc

# Definitions ..
vowels = ['a','e','i','o','u']
blends = ['bl','br','sh','sk','sch','scr','ch','cl','cr','dr','fl','fr','gl', \
          'gr','pl','pr','sc','sk','sl','sm','sn','sp','st','sw','th','tr', \
          'tw','wh','wr','shr','sph','spl','spr','squ','str','thr']
vowelClusters = ['aa','ai','ea','ee','ie','oo','oa','oi','ou','ay','aw', \
                 'oy','ow']

# Functions ..
def fAdjust(rtext, text, splitPoint):
    rtext = dc(rtext[splitPoint:])
    split = dc(text[:splitPoint])
    text = dc(text[splitPoint:])
    return rtext, text, split

def fSyllabicate(text):
    ctext = []
    for x in text:
        if x in vowels:
            ctext.append('V')
        else:
            ctext.append('C')
    ctext = ''.join(ctext)
    
    # Next we write elementary rules to syllabicate texts
    rtext = dc(ctext)
    splits = []
    changeMade = True
    
    while changeMade:
        changeMade = False
        
        # Determine the rule to work on depending on which creates leftmost split
        potPoint = 100
        rule = 0

        ppoint = rtext.find('VCCV')
        if ppoint > -1 and ppoint < potPoint:
            potPoint = ppoint
            rule = 1
        
        ppoint = rtext.find('VCCCV')
        if ppoint > -1 and ppoint < potPoint:
            potPoint = ppoint
            rule = 2
            
        ppoint = rtext.find('VCV')
        if ppoint > -1 and ppoint < potPoint:
            potPoint = ppoint
            rule = 3

        ppoint = rtext.find('VV')
        if ppoint > -1 and ppoint < potPoint:
            potPoint = ppoint
            rule = 4
        
        if rule == 0:
            continue
        
        # Rule 1. Split on VCCV .. cof-fee, pic-nic
        #         EXCEPT 'cluster consonants' .. meth-od, ro-chester, hang-out
        if rule == 1:
            if text[potPoint+1 : potPoint+3] in blends:
                splitPoint = potPoint + 1
            else:
                splitPoint = potPoint + 2
            rtext, text, split = fAdjust(rtext, text, splitPoint)
            splits.append(split)
            changeMade = True
            continue
        
        # Rule 2. Split on VCCCV .. split keeping the blends .. mon-ster, chil-dren
        if rule == 2:
            splitPoint = potPoint + 2
            for w in blends:
                sPoint = text[potPoint+1:potPoint+4].find(w)
                if sPoint > -1:
                    splitPoint = potPoint + sPoint + 1
                    break
            rtext, text, split = fAdjust(rtext, text, splitPoint)
            splits.append(split)
            changeMade = True
            continue
        
        # Rule 3. Split on VCV .. ba-con, a-rid
        #         EXCEPT cour-age
        #         EXCEPT time should not be ti-me @@@ NOT CORRECTED YET
        if rule == 3:
            splitPoint = potPoint + 1
            rtext, text, split = fAdjust(rtext, text, splitPoint)
            splits.append(split)
            changeMade = True        
            continue
        
        # Rule 4. Split on VV .. po-em
        #         EXCEPT cluster vowels glacier,earl-ier
        if rule == 4:
            if text[potPoint:potPoint+2] in vowelClusters:
                continue
            splitPoint = potPoint + 1
            rtext, text, split = fAdjust(rtext, text, splitPoint)
            splits.append(split)
            changeMade = True        
            continue
        
    splits.append(text)
    return splits