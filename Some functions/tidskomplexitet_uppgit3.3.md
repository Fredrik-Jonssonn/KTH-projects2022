Tidskomplexiteten för sign_partition-funktionen i uppgift3.3VG.py är <i>O(n)</i>, där 
n är antalet element i vektorn v. Funktionen består av en while loop
som itererar n gånger. Detta då loopen terminerar då variabeln low är lika med variabeln
high, differensen (high - low) är initialt = n och den minskar med 1 för varje iteration tills (high-low)=0 och loopen
terminerar. Alla operationer (tilldelningar och jämförelser) i en enskild iteration har konstant tidskomplexitet <i>O(1)</i>, alltså har 
hela funktionen tidskomplexitet <i>O(n)</i>.

Algoritmen är in-place då det enda extra minnet som används är för de två variablerna low och high som vardera pekar
på en int. Det extra minnet är alltså <i>O(1)</i>.