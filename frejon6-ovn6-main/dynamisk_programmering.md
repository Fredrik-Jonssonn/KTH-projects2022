### Förklara varför rekursionen fungerar?

>p(0) = 0,\
>p(n) = max<sub>1 &le; i &le; n</sub>(h(i) + p(n-i)) om n > 0.

Vid anropet p(n) kommer inkomsten för alla möjliga kollektioner som kan skapas med n meter garn att beräknas, sedan returnerar p(n) den maximala av 
dessa. Detta gör den explicit genom att man helt enkelt adderar priset för en halsduk av längd i med den maximala 
inkomsten (rekursivt anrop) av resterande garn och jämför för vilket i detta maximeras. 

### Implementera en rekursiv funktion som beräknar p(n). Glöm inte dokumentation och testkod.
Se [dynprog_no_caching.py](dynprog_no_caching.py)
### Beräkna p(5) när h[1] = 2, h[2] = 5, h [3] = 6, h[4] = 9, h[n] = 0 när n > 4. Simulera beräkningarna för hand och rita ett träd över alla funktionsanrop. Det går bra med ett foto på ett handritat träd.
p(5) = 12. Anropet p(5) kommer göra 5 stycken rekursiva anrop: p(5-i), i &in;[1, 5] (i är heltal) och utföra beräkningarna
h[i]+p(5-i), anropet p(4) kommer göra 4 stycken rekursiva anrop: p(4-i), i &in;[1, 4] och utföra beräkningarna
h[i]+p(4-i), varje anrop p(3) kommer göra 3 stycken rekursiva anrop: p(3-i), i &in;[1, 3] och utföra beräkningarna
h[i]+p(3-i) osv. Detta ger följande träd av rekursiva anrop.

![anropsträd](anropsträd.jpg)
### Förklara varför tidskomplexiteten för denna funktion är exponentiell.
För varje rekursivt funktionsanrop (och ursprungsanropet) gör algoritmen p(n) endast en begränsad mängd konstant tid operationer om vi bortser från eventuella
rekursiva anrop, vi kan därför 
låta antalet funktionsanrop vara vår elementära operation i beräkningen av tidskomplexiteten. 
Låt T(n) = "totala antalet funktionsanrop som görs vid anropet p(n) (p(n) inkluderat)". p(n) gör de rekursiva anropen
p(n-i), i = heltal &in;[1, n]. Vilket alltså ger:
T(n) = 1 + T(n-1) + T(n-2) + ... T(0). Detta är i sig en rekursiv funktion och med vetskapen att p(0) är basfallet
vilket ger att T(0) = 1 kan den lösas. Lösning ger T(n) = 2<sup>n</sup>. Alltså är funktionens tidskomplexitet O(2<sup>n</sup>),
dvs. exponentiell. 

En mer intuitiv förklaring för att funktionen har exponentiell tidskomplexitet kan fås genom att betrakta 
funktionsanropen som träd likt ovan. Då inses att trädet med rot p(n) består av alla subträd med rot p(n-i), i = heltal &in;[1, n] + roten p(n) själv.
Detta medför en fördubbling av antalet funktionsanrop för varje heltal som n ökar, dvs T(n) = 2<sup>n</sup>.
### Förbättra tidskomplexiteten genom att skriva en version av programmet som cachar delresultat.
Se [dynprog_cachingVG.py](dynprog_cachingVG.py)
### Räkna ut en tabell över p(n) för n= 0, 1, 2, 3, 4, 5 (med samma h som ovan). Gör beräkningen för hand.

I beräkningarna nedan så sparar jag värdena p(n) så fort de beräknas i tabellen så att de direkt kan användas som de kommer upp.

<i>

p(0) = 0 = basfall

p(1) = h[1] + p(0) = 2 + 0 = 2

p(2) = max(h[1] + p(1), h[2] + p(0)) = max(4, 5) = 5

p(3) = max(h[1] + p(2), h[2] + p(1), h[3] + p(0)) = max(7, 7, 6) = 7

p(4) = max(h[1] + p(3), h[2] + p(2), h[3] + p(1), h[4] + p(0)) = max(9, 10, 8, 9) = 10

p(3) = max(h[1] + p(4), h[2] + p(3), h[3] + p(2), h[4] + p(1), h[5] + p(0)) = max(12, 12, 11, 11, 0) = 12

</i>

| n | p(n) |
|---|------|
| 0 | 0    |
| 1 | 2    |
| 2 | 5    |
| 3 | 7    |
| 4 | 10   |
| 5 | 12   |
### Visa att tidskomplexiteten för den uppdaterade koden är <i>O(n<sup>2</sup>)</i>.
Låt n i texten nedan vara argumentet n för ursprungsanropet. Observera dock att n i kodstyckena enbart är ett funktionsargument
som kan anta olika värden för olika rekursiva anrop. 

Först har vi följande for loop som bidrar med tidskomplexiteten O(n).

    23    if len(memo) == 0:
    24        memo = [None for _ in range(n + 1)]
Loopen körs totalt en gång endast i ursprungsanropet max_value_collection(n, h) och bidrar därför med en linjär tidskomplexitet.

Sedan har vi 

    25  if memo[n] is not None:
    26    return memo[n]

Denna if sats är en konstant tid jämförelse som är sann om max_value_collection(n-i, h, memo) (p(n-i)) redan är beräknad och sparad i listan memo. Vi kan därför
betrakta alla funktionsanrop max_value_collection(n-i, h, memo) förutom det första som konstant tid operationer. i kan här vara
alla heltal &in;[0,n].


Resten av koden i max_value_collection(n, h, memo) körs en gång för varje heltal i&in;[0, n] i de första anropen av max_value_collection(n-i, h, memo),
och motsvarar den första beräkningen av max_value_collection(n-i, h) och sparandet av resultatet i listan memo: 
    
    27  curr_max_value_collection = ScarfCollection()
    28  curr_max_value_collection.scarfs = [0 for _ in range(n + 1)]
    29  temp_scarf = None
    30  for i in range(1, n + 1):
    31      temp_value = h[i] + max_value_collection(n - i, h, memo).value
    32      if temp_value > curr_max_value_collection.value:
    33          curr_max_value_collection.value = temp_value
    34          temp_scarf = i
    35  if temp_scarf is not None:
    36      for i in range(n + 1 - temp_scarf):
    37          curr_max_value_collection.scarfs[i] = memo[n - temp_scarf].scarfs[i]
    38      curr_max_value_collection.scarfs[temp_scarf] += 1
    39  memo[n] = curr_max_value_collection
    40  return curr_max_value_collection

Här kan vi ta summationen på rad 31 som elementär operation. Låt antalet elementära operationer som utförs totalt över alla
de första anropen max_value_collection(n-i, h, memo) (som härstammar från ursprungsanropet max_value_collection(n, h)) vara T(n). Som
sagt betraktar vi funktionsanropen i denna rad som konstant tid operationer eftersom fallen där de inte är det redan
tas hänsyn till. Vi får

T(n) = n + &sum;<sub>1</sub><sup>n</sup>(n-i) = n(n+1)/2 = (n^2+n)/2

&rarr; Tidskomplexiteten som denna del av koden bidrar med är O(n^2)

Alltså är hela funktionens tidskomplexitet O(n^2).

### Uppdatera koden i G-uppgiften så att den inte bara beräknar den maximala inkomsten, utan också ger en lista över halsdukar (garnåtgång och antal som uppnår detta). Om det finns flera möjliga lösningar så räcker det om du anger en.

Se [dynprog_cachingVG.py](dynprog_cachingVG.py). Den sökta listan är max_value_collection(n, h).scarfs och kollektionens värde
(pris/inkomsten man kan tjäna på kollektionen) som är maximal för n meter garn är max_value_collection(n, h).value