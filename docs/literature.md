# Analiza literatury i wnioski

### [On Finiteness in the Card Game of War](https://www.tandfonline.com/doi/pdf/10.4169/amer.math.monthly.119.04.318?needAccess=true&) (krótki artykuł)

- To czy gra będzie skończona czy nie, zależy od tego jak dobierane przez zwycięzcę.
- Jeżeli karty zbierane są zawsze w taki sam sposób (np. zawsze dobieramy najpierw swoją a później przeciwnika) to mogą się zdarzyć nieskończone gry z cyklem.
- Jeżeli kolejność zbierania kart jest w jakimś stopniu losowa, gra zawsze jest grą skończoną. Jest to wniosek na podstawie analizy [Łańcuchów Markowa](https://pl.wikipedia.org/wiki/%C5%81a%C5%84cuch_Markowa)
- Zmiana kolejności wkładanych kart na spód swojej talii ma wpływ zarówno na długość rozgrywki jak i może mieć wpływ na jej wynik.

### [Predictability in the Game of War](https://www.scq.ubc.ca/predictability-in-the-game-of-war/) (krótki artykuł)

- Określenie _wag_ kart:

  | Figura | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | J   | Q   | K   | A   |
  | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Waga   | -6  | -5  | -4  | -3  | -2  | -1  | 0   | 1   | 2   | 3   | 4   | 5   | 6   |

- Waga całej talii, czyli suma wag wszystkich kart, to 0.
- "Sprawiedliwy" podział talii wtedy, gdy waga kart każdego z graczy to 0 (np. gdy jeden z graczy otrzyma wszystkie czerwone, a drugi czarne karty).
- Prawdopodobieństwo zwycięstwa liniowo zależne od wagi kart gracza.
- Prawdopodobieństwo zwycięstwa liniowo zależy od liczby zwyciężonych rund przez gracza w pierwszej iteracji talii.

### [~~Framework for Monte Carlo TreeSearch-related strategies in Competitive Card Based Games~~](https://core.ac.uk/download/pdf/143405876.pdf) (96 stron)

- Bardzo matematyczne podejście do strategii w grach. Raczej w kontekście naszej pracy się nie przyda.

### [Combinatorial Aspects of the Card Game War](https://arxiv.org/pdf/2202.00473.pdf) (22 strony)

- Rozważono 2 rodzaje chowania do talii - najpierw swoja, a potem przeciwnika oraz losowo.
- Podano wzór na prawdopodobieństwo, że gra będzie trwała daną liczbę rund przy odkładaniu najpierw swojej karty.

### [~~All's Fair in Love and WAR: Combinatorics in a card game~~](https://digitalcommons.csbsju.edu/honors_theses/602/)

Nie ma chyba dostępnego pdf'a. Może gdzieś uda się znaleźć, bo też się wydaje pasować do tematu.

> ... For example is it possible that a game may not end? Is it plausible that an entire game be played without a match occurring? Some of these questions were asked and answered by Angela Chappell in her 1998 senior honors thesis. To find her answers, however, she had to establish a set of assumptions for the way the game was to be played. To illustrate, she generated her data using the convention that, if player A and B were playing War, and on the first hand player A's card was greater than player B's card, then A's card would go back to A's hand first before B's card. My project, then, is to change several of Ms. Chappell's assumptions and replay the games. ...

### [Counting Cards: Combinatorics, Group Theory, and and Probability in War](https://digitalcommons.csbsju.edu/cgi/viewcontent.cgi?article=1646&context=honors_theses) (54 strony)

Praca, na której bazuje "All's Fair in Love and WAR: Combinatorics in a card game".

- Opis możliwości powstawania pętli w trakcie gry. Bardzo ciekawe rozważenia w celu unikania przez algorytm zagrań, które mogą doprowadzić do nieskończonej rozgrywki.

### [An analysis of a war-like card game](https://arxiv.org/abs/1001.1017)

- Gra różniąca się od klasycznej gry w wojnę (Raczej z tego względu nie przydatne dla naszej pracy):
  - przy każdej rundzie karta wyższa jest odrzucana,
  - W grze nie ma dwóch kart o takich samych wartościach (nie rozważane są sytuacje remisów/wojen).
- Praca zawiera dodatkowe rozważania na temat wpływu stosunku liczby kart posiadanych przez graczy na prawdopodobieństwo wygranej, co może być dodatkowo ciekawym tematem do rozważenia w naszej pracy.

### [Note on a War-like Card Game](https://www.tandfonline.com/doi/pdf/10.4169/amer.math.monthly.119.09.793?needAccess=true)

> We prove that the probability that one of the players has a winning strategy in the War-like card game “Peer Pressure” approaches zero as the number of cards dealt approaches infinity, even if the cards are dealt in a slightly-biased manner.

- Zwycięska strategia to taka która pozwala na zwycięstwo niezależnie od ruchów przeciwnika.

## Prace dodatkowo zaproponowane przez prowadzącego

### [Computing Game Strategies](https://www.researchgate.net/publication/265829608_Computing_Game_Strategies)

- Konstruowanie strategii w grach decyzyjnych. Bardzo matematyczne, nie ma bezpośrednio nic o grze w wojnę. Można poszukać ciekawych rozwiązań, jak symulować czy jakie są możliwe strategie.

### [~~Designing Card Game Strategies with Genetic Programming and Monte-Carlo Tree Search: A Case Study of Hearthstone~~](https://www.researchgate.net/publication/348262166_Designing_Card_Game_Strategies_with_Genetic_Programming_and_Monte-Carlo_Tree_Search_A_Case_Study_of_Hearthstone)

Nie ma dostępu. Można pokusić się o poproszenie autorów o pracę.

### [A Simple Winning Strategy for the Card Game War](https://scienceblogs.com/pontiff/2008/09/12/a-simple-strategy-for-the-card)

- Pokazuje że wybór strategii ma znaczenie i ma wpływ na % wygranych gier. Ciekawe dane udostępnione w zależności od wybranej strategii. Autor nie powiedział nic o potencjalnym wykorzystaniu strategii przez obu graczy i co się wtedy dzieje.

### [~~How can you introduce strategy into the card game "WAR"?~~](https://www.quora.com/How-can-you-introduce-strategy-into-the-card-game-WAR)

- Nic ciekawego tutaj nie ma - forum na którym ludzie piszą, że wojna to gra w której nie można mówić o strategii bo nie ma decyzji. Do odrzucenia.

## Wnioski z badań literatury

Gra w wojnę nie jest grą mocno przebadaną w literaturze naukowej. Istnieje kilka dzieł, które badają tą grę karcianą, jednakże opierają się na statystyce. Istnieją prace analizujące występowanie strategii wygrywającej czyli takiej która prowadzi do zwycięstwa niezależnie od ruchów przeciwnika, lecz także jest to oparte na statystyce i nie wskazuje w jaki sposób można by dojść do takiej strategii. Jedynie jeden wpis na blogu poruszał temat realnego zwiększenia szansy na wygraną przy grze w wojnę. Wpis ten zawierał sztywny sposób zbierania wygranych kart i na podstawie wyników z eksperymentów udało się uzyskać zwiększenie szans na zwycięstwo o kilkanaście procent. Jednakże nie udało nam się znaleźć pracy, która pokazywałaby w jaki sposób można by zwiększyć szansę na swoją wygraną, posiadając komputer pozwalający na zapamiętanie rozkładu wszystkich kart zarówno w swojej ręce jak i ręce przeciwnika.
