## Påstående
P(n) = Funktionsanropet factorial(n) returnerar n!, där n är ett icke-negativt heltal.

## Induktionsbevis
#### Basfall
P(0) är sant då funktionen returnerar 1 om n=0.

#### Induktionssteg
Vi gör induktionsantagandet att "P(i) är sant för alla <i>i < k </i>". Om <i>k &ge; 1</i> returnerar funktionsanropet
factorial(k): k * factorial(k-1), men enligt induktionsantagandet gäller att factorial(k-1)=(k-1)! . Alltså returnerar 
funktionsanropet factorial(k): k*(k-1)!=k! . Alltså är P(k) sant givet induktionsantagandet.

Per induktion är därmed P(n) sant för alla icke negativa heltal n.

V.S.V