<pre><code><b>Algorithm</b> bipartite_test(G)
    """Return True if graph G is bipartite.
    Return False if it is not bipartite."""
    <b>while</b> some vertices v are uncolored:
        <b>if</b> _bipartite_test_helper(G, uncolored_v, color1) is False:
            <b>return</b> False
    <b>return</b> True
    
    _bipartite_test_helper(G, v, color)
    """Return True if the connected component of the graph G that 
    the vertex v belongs to is bipartite. Return False if it is not bipartite.""" 
    <b>if</b> v is already colored:
        <b>if</b> v.color != color:
            <b>return</b> False
        <b>return</b> True
    Mark v as colored
    v.color &larr; color
    <b>if</b> color == color1:
        <b>for</b> all neighbours x of v:
            <b>if</b> _bipartite_test_helper(G, x, color2) is False:
                <b>return</b> False
    <b>else</b>:
        <b>for</b> all neighbours x of v:
            <b>if</b> _bipartite_test_helper(G, x, color1) is False:
                <b>return</b> False
    <b>return</b> True


Before running bipartite_test(G) all vertices v in the graph G must be marked as uncolored.
</code></pre>

Det kommer räcka med två uppgifter om och endast om elevgrafen G är bipartit ("två-färgad"), algoritmen bipartite_test(G)
testar just detta. Algoritmen returnerar True om grafen är bipartit vilket innebär att 2 uppgifter räcker och 
och algoritmen returnerar False om den inte är det vilket innebär att 2 uppgifter ej kommer räcka. 
Algoritmen är baserad på en DFS sökning av hela grafen G, där man ger varje hörn en av två färger (uppgifter) på ett sätt
så att hörn som är grannar ej tilldelas samma färg. Om motsägelser uppstår i denna tilldelning terminerar algoritmen
och returnerar False, detta innebär att grafen ej är bipartit. Uppstår inga motsägelser är grafen bipartit och algoritmen returnerar
True.

Algoritmen har värstafallstidskomplexitet &Theta;(|V| + |E|), där |V| är antalet hörn i G och |E| är antalet kanter i G.

**Motivering för tidskomplexiteten:**

Tidskomplexiteten kommer variera beroende på grafen G.
Värstafallet är då algoritmen returnerar True, annars kommer algoritmen terminera och returnera False
så fort en motsägelse i färgtilldelningen uppstår och detta kan ske nästan direkt eller mot slutet av algoritmen.
Vi beräknar därför värstafallstidskomplexiteten i fallet då algoritmen returnerar True.

Algoritmen är i värstafallet en vanlig DFS-sökning med tidskomplexitet &Theta;(|V| + |E|)<sup>1</sup> av hela G. Detta eftersom det görs exakt lika
många anrop av _bipartite_test_helper() som DFS anrop i en vanlig DFS-algoritm (2|E| stycken), och precis som i en vanlig DFS-algoritm
utförs endast en begränsad mängd konstant tid operationer för varje anrop.

### Källor:
1. https://yourbasic.org/algorithms/graph/