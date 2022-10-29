Grupy hipotez:

1. Cykle
   - Świadome unikanie z wyprzedzeniem nieskończonych gier będzie "trudne", ale wprowadzenie losowości do podejmowanych wyborów gwarantuje, że gra się skończy
   - W interesie algorytmu nie musi być dbanie o niedoprowadzenie do nieskończonej gry (w przypadku gorszych kart może chcieć "zakończyć" grę remisem)
   - naiwne unikanie cykli: Jeśli wystąpi taki sam stan gry jak wcześniej to podejmij inną najbliższą decyzję
   - Przy zbliżonym rozkładzie kart istnieje większe prawdopodobieństwo wystąpienia cyklu
2. Różne strategie
   - sprawdzenie wpływu stałych strategii (np. W-M-M-W, W-M-W-M, M-W-W-M) na liczbę wygranych partii
   - stały sposób zbierania kart
   - Istnieje strategia wygrywająca do gry w wojnę
   - Strategia pozwala wygrać przy teoretycznych gorszym rozkładzie kart początkowych
     Istnieje więcej niż jedna strategia zwiększająca szanse na wygraną -> strategie te mogą na siebie wpływać i modyfikować swoje osiągi
3. Naiwny algorytm
   - Sprawdzenie, czy znając rozkład swoich i przeciwnika kart, można zwiększyć swoją szansę na wygraną poprzez stosowanie metody zachłannej
   - Wykorzystanie naiwnego algorytmu wybierania w danym momencie najlepszego ułożenia kart za "zauważalną" przewagę nad losowym dobieraniem
   - Strategia wygrywająca bezpośrednio zależy od tego jak gra przeciwnik
4. Drzewo
   - Stworzenie drzewa gry i sprawdzenie możliwości zredukowania go
   - Zagwarantowanie wygranej jest niemożliwe
   - Sprawdzenie czy da się stworzyć program, który będzie wygrywał w wojnę zawsze, gdy podział kart będzie sprawiedliwy
   - osiągnięcie znacznej przewagi będzie trudne (pamięciochłonne)
5. Różne
   - Strategia wygrywająca może działać tylko, gdy jeden z graczy jej nie stosuje
   - Gdy obaj gracze stosują tę samą strategię w większości gier wygra ten z lepszym rozkładem początkowym
   - Przy grze, w której uczestniczy więcej graczy strategie mogą dać inny efekt, lub mogą w ogóle nie działać
