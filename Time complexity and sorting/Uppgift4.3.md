<pre><code><b>Algorithm</b> repeat_sort(v)
    """Sort the elements of the vector v in ascending order,
    v stores integers"""
    freq_hash &larr; empty hash table
    <b>for</b> i &larr; 0 <b>to</b> length(v)
        <b>if</b> v[i] <b>in</b> freq_hash:
            freq_hash[v[i]] += 1
        <b>else</b>
            freq_hash[v[i]] &larr; 1
    v_sorted &larr; []
    <b>for</b> i <b>in</b> sorted(freq_hash.keys): # where the sorted() sorting algorithm is expected <i>O(k logk)</i>
        v_sorted += freq_hash[i]*[i]
    v &larr; v_sorted
</code></pre>
Låt n vara antalet element i vektorn v och k vara det totala antalet olika tal i v. Algoritmen ovan har den
förväntade tidskomplexiteten <i>O(n+klog(k))</i> och den är linjär i n om <i> n > k log(k)</i>.

***Motivering för tidskomplexiteten:***\
Algoritmen består av tre stycken delar som är intressanta att undersöka ur ett tidskomplexitetsperspektiv.

Först skapas en hashtabell (freq_hash) med
k element i den första for-loopen. For-loopen itererar n gånger över v:s element och operationerna i en enskild iteration
(ändra/lägga till nyckel-värdepar, sökning) har förväntad tidskomplexitet <i>O(1)</i>. Detta ger en total
förväntad tidskomplexitet <i>O(n)</i> för for-loopen. 

Sedan sorteras freq_hash's nycklar med en valfri förväntad <i>O(k log(k))</i> sorteringsalgoritm som t.ex
quicksort eller pythons inbyggda sorted() (timsort). Eftersom freq_hash har k element bidrar denna sortering alltså
med en förväntad tidskomplexitet <i>O(k log(k))</i>.

Slutligen iterer algoritmen k gånger över sorted(freq_hash.keys) (dvs. freq_hash's nycklar i sorterad ordning) i en for-loop. I varje
enskild iteration läggs frekvensen av ett tal i v stycken element av talet till i slutet av en ny vektor v_sorted. Operationen
att lägga till ett element i slutet av en vektor har amorterad tidskomplexitet <i>O(1)</i> och totalt läggs n element till.
Detta ger en total tidskomplexitet <i>O(n)</i> för for-loopen.

Totalt har algoritmen alltså den förväntade tidskomplexiteten <i>O(n+k log(k))</i>