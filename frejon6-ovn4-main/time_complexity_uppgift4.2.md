Algoritmen counting_sort(v) i uppgift4.2.py har värstafallstidskomplexitet <i>O(n + k)</i>, där n är antalet element
i v och k är det största av dessa element. Algoritmen blir linjär i n om <i>n > k </i>.

***Motivering för tidskomplexiteten:***\
Algoritmen består av ett anrop till max() metoden som har värstafallstidskomplexiteten <i>O(n)</i> och sedan 6 stycken
for loopar alla med antingen <i>O(n)</i> eller <i>O(k)</i> värstafallstidskomplexitet.

Totalt ger detta att algoritmen värstafallstidskomplexiteten <i>O(n + k)</i>.