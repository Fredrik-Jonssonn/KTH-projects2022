### Terminologi:
Graf: Graf med självloopar, men ej med multipla kanter (Tillåter man multipla kanter kan man ha oändligt många kanter).

Enkel graf: Graf utan själv-loopar eller multipla kanter.

Träd: Sammanhängande enkel graf utan cykler.
### Frågor
OBS! Jag tar frågan om enkla grafer först, tillskillnad från uppgiftsformulering:

***Hur många kanter kan det som mest finnas i en enkel graf med n stcken hörn?***

Det maximala antalet kanter fås om alla hörn är direkt sammankopplade med en kant, det vill säga att avståndet mellan 
alla kanter är 1. Detta antal motsvarar antalet sätt det går att välja ut två hörn från en mängd med n st hörn, alltså
antalet kombinationer <i><sub>n</sub>C<sub>2</sub>=n(n-1)/2</i>. Eftersom om vi väljer ut två hörn kommer det alltid
finnas en unik kant mellan dem. 

Svar : <i>n(n-1)/2</i>

***Hur många kanter kan det som mest finnas i en graf med n stcken hörn?***

Detta är nästan exakt samma situation som ovan med de enkla graferna med den enda skillnaden att vi nu tillåter själv-loopar.
Det maximala antalet kanter fås om varje hörn har en själv-loop och alla hörn är direkt sammankopplade med en kant, det vill säga att avståndet mellan 
alla kanter är 1. Alltså blir det maximala antalet kanter <i><sub>n</sub>C<sub>2</sub>+n=n(n+1)/2</i> enligt samma resonemang som ovan tillsammans med att vi nu
också har n st själv-loopar.

Svar : <i>n(n+1)/2</i>

***Hur många kanter kan det som mest finnas i ett träd med n stycken hörn?***

Ett träd med n stycken hörn har alltid n-1 stycken kanter. Detta kan visas med induktion: 

Låt P(n)="Ett träd med n stycken hörn har n-1 stycken kanter.", n är ett positivt heltal. 

Basfall:

P(1) =  "Ett träd med 1 hörn har 0 stycken kanter." är trivialt sant då ett träd är en enkel graf som ej tillåter
själv-loopar och det finns endast ett hörn så inga kanter finns i trädet.

Induktionssteg:

Låt k vara ett heltal > 1. Vi gör induktionsantagandet att "P(k-1) är sant". För att skapa ett träd med k stycken hörn måste vi lägga till ett hörn
till ett träd med k-1 stycken hörn, detta k:te hörn måste vara ett löv (gradtal 1), det vill säga att det k:te hörnet
får endast vara sammankopplad med resten av trädet med en kant. Detta eftersom vi annars skapar en cykel. Alltså gäller att antalet
kanter i trädet med k stycken hörn är antalet kanter i trädet med k-1 stycken hörn + 1. Enligt induktionsantagandet 
har trädet med k-1 stycken hörn k-2 stycken kanter, vilket ger att trädet med k stycken hörn har k-1 stycken kanter. 
Detta innebär att P(k) är sant.

Alltså gäller P(n) per induktion.

Det maximala antalet kanter blir därför just n-1. 

Svar: n-1 