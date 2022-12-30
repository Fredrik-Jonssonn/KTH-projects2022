## Fredrik Jonsson, grudat22 uppgift 2.1

#### **Ordna funktionerna i följande lista i växande ordning med avseende på tillväxtstakt. Funktionen <i>f(n)</i> ska alltså komma före funktionen <i>g(n)</i>  i listan om <i>f(n)</i>  är <i>O(g(n))</i> .**
<ul>
<li><i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i><sup>1.5</sup>
</li>
<li><i>f<sub>2</sub>(n)</i>&nbsp;=&nbsp;10<sup><i>n</i></sup>
</li>
<li><i>f<sub>3</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;log&nbsp;<i>n</i>
</li>
<li><i>f<sub>4</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;+ 100
</li>
<li><i>f<sub>5</sub>(n)</i>&nbsp;=&nbsp;2<sup><i>n</i></sup>
</li>
</ul>

#### Lösning
Den sökta ordningen är (lägst tillväxtstakt först) 

f<sub>4</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;+ 100 ( <i>&Theta;(n)</i> )

f<sub>3</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;log&nbsp;<i>n</i> ( <i>&Theta;(n log (n))</i> )

f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i><sup>1.5</sup> ( <i>&Theta;(n<sup> 1.5 </sup> </i>) )

f<sub>5</sub>(n)</i>&nbsp;=&nbsp;2<sup><i>n</i></sup> ( <i>&Theta;(2<sup> n </sup> </i>) )

 f<sub>2</sub>(n)</i>&nbsp;=&nbsp;10<sup><i>n</i></sup> ( <i>&Theta;(10<sup> n </sup> </i>) )

Detta eftersom
<i>&Theta;(n)</i> < <i>&Theta;(n log (n))</i> < <i>&Theta;(n<sup> 1.5 </sup> </i>) < <i>&Theta;(2<sup> n </sup> </i>)
 < <i>&Theta;(10<sup> n </sup> </i>) med avseende på tillväxtstakt. 

#### **Vilka av följande påståenden är sanna? Motivera dina svar.**

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>2</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Theta;(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Omega;(<i>n</i>)</li>
</ul>

#### Lösning
För gör vi omskrivningen <i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>n<sup>2</sup>/2 +  n/2</i>.

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>3</sup>)</li> 
</ul>

Vi har att <i>n<sup>2</sup>/2 +  n/2 &le; n<sup>3</sup></i> för <i>n &ge; 1</i> ---> <i>n<sup>2</sup>/2 +  n/2
= </i><i>O</i>(<i>n</i><sup>3</sup>). Påståendet är alltså sant. 

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>2</sup>)</li>
</ul>

Vi har att <i>n<sup>2</sup>/2 +  n/2 &le; n<sup>2</sup></i> för <i>n &ge; 1 ---> n<sup>2</sup>/2 +  n/2
=</i> <i>O</i>(<i>n</i><sup>2</sup>). Påståendet är alltså sant. 

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Theta;(<i>n</i><sup>3</sup>)</li> 
</ul>

Vi har att <i>n<sup>2</sup>/2 +  n/2 =</i> <i>O</i>(<i>n</i><sup>3</sup>) enligt det första påståendet,
men 
<i>n<sup>2</sup>/2 +  n/2 < Kn<sup>3</sup></i> för alla positiva konstanter K då <i>n-->&infin;</i>. Alltså är 
<i>n<sup>2</sup>/2 +  n/2 &ne;  &Omega;</i>(<i>n<sup>3</sup></i>) och
därmed är <i>n<sup>2</sup>/2 +  n/2 &ne;  &Theta;</i>(<i>n<sup>3</sup></i>). Påståendet är alltså falskt.

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Omega;(<i>n</i>)</li>
</ul>

Vi har att <i>n<sup>2</sup>/2 +  n/2 &ge; n/2</i> för <i>n &ge; 0 ---> n<sup>2</sup>/2 +  n/2
=</i> <i>&Omega;</i>(<i>n</i>). Påståendet är alltså sant. 