## Fredrik Jonsson, grudat22 uppgift 2.2
### Prefixsumma
Indata är en heltalsvektor <i>A</i> med <i>n</i>&nbsp;element. Vi vill beräkna en vektor <i>B</i>, där <i>B</i>[i]&nbsp;=<i>A</i>[0]&nbsp;+&nbsp;<i>A</i>[1]&nbsp;+&nbsp;...&nbsp;+&nbsp;<i>A</i>[i]. Här är en enkel algoritm som löser problemet.

<pre><code><b>for</b> i = 0 <b>to</b> n-1
    Add the numbers A[0] thru A[i].
    Store the result in B[i].
</code></pre>

- Beräkna tidskomplexiteten för denna algoritm och uttryck den på
  formen&nbsp;<i>O</i>(<i>f(n)</i>), där funktionen&nbsp;<i>f(n)</i>
  är så liten och enkel som möjligt.

- Visa att tidskomplexiteten också är &Omega;(<i>f(n)</i>).

- Hitta på en algoritm med bättre asymptotisk tidskomplexitet.
  Beskriv algoritmen i pseudokod och ange dess
  tidskomplexitet med Θ-notation.

#### Lösning
Låt oss välja additionen inuti for-loopen som den elementära operationen. 
För varje iteration av for-loopen utförs <i>i</i> st additioner. Detta ger en tidskomplexitet
<i>T(n)=1+2+3 + ... + (n-1) = n(n-1)/2  = n<sup>2</sup>/2 - n/2 </i>. Det gäller att <i>T(n) &le; n<sup>2</sup>
</i> då n ---> &infin; alltså är <i>T(n) = O(n<sup>2</sup>)</i>. Det gäller även att <i>T(n) &ge; n<sup>2</sup>/4</i>
då n ---> &infin; alltså är <i>T(n) = &Omega;(n<sup>2</sup>)</i> och därmed är <i>T(n) = &Theta;(n<sup>2</sup>)</i>.

Följande algoritm har en bättre asymptotisk tidskomplexitet:

<pre><code><b>for</b> i = 0 <b>to</b> n-1
    <b>if </b>i = 0:
      Store the value of A[i] in B[i]
    <b>else</b>
      Add B[i-1] and A[i]
      Store the result in B[i]
</code></pre>
Låt oss återigen välja additionen inuti for-loopen som den elementära operationen. 
För varje iteration av for-loopen utförs nu istället endast <i>1</i> addition (0 för i=0). Detta ger totalt n-1 additioner
och alltså en tidskomplexitet
<i>T(n) = n-1</i>. Det gäller att <i>T(n) &le; n
</i> då n ---> &infin; alltså är <i>T(n) = O(n)</i>. Det gäller även att <i>T(n) &ge; n/2</i>
då n ---> &infin; alltså är <i>T(n) = &Omega;(n)</i> och därmed är <i>T(n) = &Theta;(n)</i>.