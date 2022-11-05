### Wpływ ilości danych na dokładność wyniku

Eksperyment polegający na zbadaniu jaki wpływ ma ilość wykonanych prób na dokładność otrzymanych wyników.
W grze w Wojnę, gdy mamy dwóch graczy i gracze zbierają karty losowo, ilość wygranych każdego z graczy powinna być równa około 50%.
Dlatego właśnie przeprowadziliśmy eksperyment w którym gracze otrzymują karty losowo i każdy z graczy po wygranej wkłada karty do swojej talii w losowej kolejności. Próby były powtarzane 20 razy.
Na osi pionowej widzimy jaką część wszystkich gier wygrał gracz numer 1, a na osi poziomej liczbę rozegranych gier.

![alt text](results_accuracy.png "Title")

Możemy zauważyć, że wyraźne zmniejszenie rozstrzału wyników przestajemy obserwować powyżej 50 tysięcy gier.

### Strategia - moja karta na górze

Zbadaliśmy jaki skutek przynosi stosowanie strategii wkładania do talii swojej karty ponad kartą przeciwnika.
Do tego eksperymentu gracze otrzymywali idealnie zbalansowane talie (każda z figur występowała po 2 razy u każdego z graczy).

![alt text](own_first.png "Title")

Dla 50 000 gier i 20 prób, liczba wygranych partii wynosiła średnio 66.0272%

### Strategia - moja karta na dole

Zbadaliśmy jaki skutek przynosi stosowanie strategii wkładania do talii swojej karty na spód.
Do tego eksperymentu gracze otrzymywali idealnie zbalansowane talie (każda z figur występowała po 2 razy u każdego z graczy).

Dla 50 000 gier i 20 prób, liczba wygranych partii wynosiła średnio 56.155%
