Låt n vara antalet hörn i grafen.

***Besök noderna i den här grafen i DFS- och BFS-ordning med start i nod 1. I vilken ordning besöks noderna
i de två fallen? Du kan anta att grannarna till en nod besöks i nummerordning.***

DFS-ordning:
1, 2, 3, 4 , 5, 6

BFS-ordning:
1, 2, 5, 3, 4, 6

***Tidskomplexiteten för DFS blir i vissa fall mycket bättre om man använder närhetslistor istället för en närhetsmatris.
Varför det?***

Närhetslistor är att föredra i fall med glesa grafer, det vill säga när hörnen har lågt gradtal relativt det totala antalet
hörn i grafen. Använder man närhetslistor gör DFS algoritmen för varje anrop till ett omarkerat hörn ett anrop till DFS
för alla hörnets grannar, vilket är hörnets gradtal antal. Använder man istället en närhetsmatris måste DFS algoritmen 
gå igenom en rad av en n x n matris och för varje element i raden göra en jämförelse (kolla om elementet är 0 eller 1) och
i fallen där elementet är 1 göra ett anrop till DFS för det hörnet, är grafen gles medför detta en sämre tidskomplexitet.
Det blir lika många anrop till DFS, men med n stycken extra jämförelser. 

***För vilken typ av grafer blir den asymptotiska tidskomplexiteten för DFS densamma för båda datastrukturerna?***

I fall med väldigt täta grafer, det vill säga när alla hörn i grafen har gradtal ~ n blir den asymptotiska tidskomplexiteten
densamma för dessa datastrukturer. I dessa fall sker ~ n stycken anrop
till DFS för varje hörn i grafen, detta ger att de extra jämförelserna som närhetsmatrisen medför ej är "onödiga" då de
i nästan varje fall kommer leda till ett anrop av DFS. Jämförelserna sker i konstant tid och bidrar ej till tidskomplexiteten
om lika många (som antalet jämförelser) anrop till DFS ändå görs.



