# Specyfikacja problemu badawczego

## Konsultacje 15.10.2022

- Decydujemy się na grę w wojnę ze względu na relatywnie małe skomplikowanie reguł względem innych gier karcianych. Jeżeli wystarczy czasu, można próbować przystosować rozwiązanie do innych gier.
- Wnioski z badań powinny zawierać informację o:
  - tym, czy udało się stworzyć system, który daje graczowi rzeczywistą przewagę,
  - złożoności pamięciowej algorytmu,
  - złożoności czasowej algorytmu,
  - warunkach rozkładu kart, w którym korzystanie z systemu jest zasadne.
- Literatury szukać głównie na własną rękę, jednakże prowadzący postara się dodatkowo polecić jakieś prace.
- Rozważyć różne strategie zbierania kart przez przeciwnika i czy ma to jakiekolwiek znaczenie dla algorytmu:
  - Przeciwnik zawsze najpierw podnosi kartę mocniejszą.
  - Przeciwnik zawsze najpierw podnosi kartę słabszą.
  - Przeciwnik zawsze najpierw podnosi swoją kartę.
  - Przeciwnik zawsze najpierw podnosi nieswoją kartę.
  - Przeciwnik losowo wybiera którą kartę podniesie jako pierwszą.
- Porównać działanie algorytmu z różnymi innymi strategiami (np. wymienionymi w poprzednim punkcie).
- Przy tworzeniu rozwiązania możemy pominąć aspekt poznawania rozkładu kart i założyć, że algorytm od razu ma pełną wiedzę o stanie gry. Ewentualnie później zbadać wpływ dodania _tury poznawczej_ na działanie algorytmu.
- Przeanalizować działanie algorytmu przy różnych rozłożeniach kart:
  - "Sztucznie" sprawiedliwe rozłożenie kart.
  - Losowe rozłożenie kart.
  - Niekorzystne dla algorytmu rozłożenie kart.
  - Korzystne dla algorytmu rozłożenie kart.
- Jeszcze nie wiadomo w jakim czasopiśmie będziemy potencjalnie publikować tworzony artykuł.
- Przy tworzeniu testów oprogramowania nie musimy się skupiać na jak największym pokryciu aplikacji. Powinniśmy testować te fragmenty, których testowanie uznamy za zasadne.
- Warstwa prezentacyjna ma niski priorytet i skupimy się na niej, jeżeli zostanie czas.
