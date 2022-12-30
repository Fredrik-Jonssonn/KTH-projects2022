### Beräkna den asymptotiska värstafallstiden för samtliga publika metoder i din implementation. Uttryck tiden som en funktion av antalet element n i listan.

Låt den sökta värstafallstiden för samtiliga metoder betecknas W(n). 
#### konstruktorn: __init_ _(self)
Metoden utför en konstant mängd operationer, vi skapar en tom lista och därför är listans storlek alltid n = 0.
Alltså är W(n) = C, där C är någon konstant.
#### add_first(self, element)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### add_last(self, element)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### get_first(self)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### get_last(self)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### get(self, index)
Låt oss välja tilldelningen på rad 67 som den elementära operationen.
        
    66: for i in range(0, index):     
    67:     temp = temp._next
Denna operation utförs 0<=index<=n-1 (index är ett heltal) gånger. Alltså är W(n) = n-1 i fallet
då vi söker elementet längst bak i listan,
dvs index = n-1.  
#### remove_first(self)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### clear(self)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### size(self)
Metoden utför en konstant mängd operationer oavsett storleken n på den befintliga listan.
Alltså är W(n) = C, där C är någon konstant.
#### string(self)
Metoden består av en for loop som itererar n gånger.

    for i in range(0, self._size):
        str_repr += str(self.get(i)) + ", "
För varje iteration anropas metoden get(self,index) med indata index = i = 0,1,2,3...,n-1 ökandes 
för varje iteration. Återigen väljer vi tilldelningen på rad 67 i metoden get(self, index) som den elementära
operationen. 

    68: for i in range(0, index):     
    69:     temp = temp._next

 Som ovan beskrivet i delen om get(self,index)
utförs den elementära operationen "index" gånger för varje anrop av get(self,index), därför utförs den totalt 1+2+3+...n-1 gånger.
Alltså är W(n) = 1+2+3+...+n-1=(n(n-1))/2=(n^2)/2-n/2