Tidskomplexiteten för mode-funktionen i uppgift3.2VG.py har förväntad tidskomplexitet <i>O(n)</i>, där n är antalet element i vektorn v. Algoritmen består av två
for-loopar. Den första konstruerar en
dictionary (standardimplementation av hashtabell i Python); count_dict, genom att iterera n gånger över vektorn v:s element.
Dictionary-operationerna i en enskild loop-iteration (ändra/lägga till nyckel-värde par, sökning) har förväntad tidskomplexitet <i>O(1)</i> och värstafallstidskomplexitet
<i>O(k)</i><sup>1</sup>, där <i>k &le; n</i> är antalet element i count_dict då operationen utförs. Detta ger en förväntad tidskomplexitet <i>O(n)</i> 
för hela for-loopen och därmed för konstruktionen av count_dict.

Den andra for-loopen jämför värdena i count_dict (som motsvarar
nyckelns frekvens i v) genom att iterera k gånger över count_dict's element. 
Dictionary-operationerna i en enskild loop-iteration (sökning) har förväntad tidskomplexitet <i>O(1)</i> och värstafallstidskomplexitet
<i>O(k)</i><sup>1</sup>. Då <i>k &le; n</i> ger detta en förväntad tidskomplexitet <i>O(n)</i> för hela for-loopen. 


Funktionen består alltså av två loopar vardera med förväntad tidskomplexitet <i>O(n)</i>, vilket medför att funktionen också har
förväntad tidskomplexitet <i>O(n)</i>.

Den förväntade tidskomplexiteten för dictionary-operationerna fås då dictionary hashfunktionen är tillräckligt robust så att
hashkollisioner undviks och vi antar att nycklarna är slumpmässigt valda. Om så ej är fallet kan mode-funktionen i värstafall få kvadratisk tidskomplexitet. 


### Källor:
1. https://wiki.python.org/moin/TimeComplexity

Anmärkning: Det som kallas average case i tabellerna på https://wiki.python.org/moin/TimeComplexity
tar jag som det förväntade fallet då man antar att nycklarna är slumpmässigt valda (trots att det inte finns någon inbyggd
randomisering i algoritmen). Detta bör vara korrekt
då det i övningsinstruktionen står:

    Vi har sett två exempel på expected time hittils i kursen: hashtabeller och treapar.
