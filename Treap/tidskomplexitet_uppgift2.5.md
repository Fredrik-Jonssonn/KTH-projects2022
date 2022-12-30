### Ange tidskomplexiteten i värstafall för samtliga operationer i uppgift2.5.py

Låt den sökta värstafallstiden för samtiliga metoder betecknas W(n), där n är antalet element i Treap-strukturen.

#### konstruktorn: __init_ _(self)
Metoden utför en konstant mängd operationer, vi skapar en tom Treap och därför är dess storlek alltid n = 0.
Alltså är W(n) = C = <i>O(1)</i>, där C är någon konstant.
#### insert(self, string)
Treap strukturen är ett balanserat binärt sökträd vilket medför en värstafallstidskomplexitet
<i>W(n)=O(log n)</i> för tillägg av element<sup>1,2</sup>.
#### _ _len_ _(self)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga lista.
Alltså är W(n) = C = <i>O(1)</i>, där C är någon konstant.
#### __ repr __
Sorteringen av listan i bokstavsordning är det som bidrar med störst tidskomplexitet för metoden, detta görs med 
den inbyggda sort() metoden för listor i Python. Sort() har  värstafallstidskomplexitet <i>O(n log n)</i> <sup>3</sup>,
vilket medför att
__ repr __ även har värstafallstidskomplexiteten <i>W(n)=O(n log n)</i>  <sup>3</sup>.

Resten av __ repr __ metoden bygger på att rekursivt besöka varje element i Treap-strukturen och lägga till 
varje element i en lista (element_list) med append() metoden för listor. Append() har amorterad konstant tidskomplexitet<sup>4</sup>
och metoden anropas en gång per rekursivt anrop av _repr_helper och _repr_helper anropas n gånger. Alltså skapas listan
med linjär tidskomplexitet. Listan skapas ordnad enligt Treap-strukturen där elementen är ordnade enligt storlek på
strängelementens Unicode värden<sup>5</sup>, vilket nästan är bokstavsordning. Skillnaden är att alla versaler
ordnas före alla gemener, vilket ej stämmer överrens med bokstavsordning där man inte skiljer på versal och gemen. Detta
gör att vi behöver sortera om listan innan vi returnerar listans strängrepresentation som strängrepresentationen för
Treap-strukturen. Denna metod skulle alltså kunna ha linjär värstafallstidskomplexitet om man accepterade att strängen var ordnad enligt
Treap-strukturen eller om man ändrade ordningen i Treap-strukturen så att den ej skiljer på versal och gemen. 


### Källor:
1. https://yourbasic.org/algorithms/binary-search-tree/
2. https://yourbasic.org/algorithms/treap/
3. https://en.wikipedia.org/wiki/Timsort
4. https://yourbasic.org/algorithms/time-complexity-arrays/
5. https://www.geeksforgeeks.org/string-comparison-in-python/