## Fredrik Jonsson, grudat22 uppgift 2.4

#### Ge ett exempel på en positiv funktion <i>f(n)</i> sådan att <i>f(n)</i> varken är <i>O</i>(<i>n</i>) eller &Omega;(<i>n</i>).

#### Lösning
Ett exempel på en positiv funktion som varken är <i>O(n)</i> eller <i>&Omega;(n)</i> är 
<i>f(n) = 1 + n<sup>2</sup>sin<sup>2</sup>(n)</i>. Då <i>n</i> går mot &infin; kommer <i>sin<sup>2</sup>(n)</i> faktorn hela tiden 
oscillera mellan 0 och 1 med perioden &pi;. För n så att <i>sin<sup>2</sup>(n)=1 och n ---> &infin; </i> gäller
att <i>f(n)=1+n<sup>2</sup> > Kn </i>för alla positiva konstanter K.
Alltså är <i>f(n) &ne; O(n) </i>. För n så att <i>sin<sup>2</sup>(n)=0 och n ---> &infin; </i>
gäller att <i>f(n)=1 <  Kn </i>
för alla positiva konstanter K. Alltså är <i>f(n) &ne; &Omega;(n)</i>.