# Założenia projektowe

System użyty do przeprowadzenia badań składać będzie z części "backendowej", używanej do przeprowadzania symulacji gry i eksperymentów, oraz ewentualnie części "frontendowej" udostępniającej interfejs w postaci aplikacji przeglądarkowej pozwalającej na uruchamianie symulacji z użyciem GUI.

## Generalne założenia technologiczne

- Projekt zostanie zrealizowany przy użyciu [Visual Studio Code](https://code.visualstudio.com/) (VSC).
- Użyty zostanie system kontroli wersji [git](https://git-scm.com/) oraz serwis [github](https://github.com/).

## Backend

### Założenia technologiczne

- Projekt zostanie zrealizowany przy użyciu języka Python 3.
- Testy jednostkowe tworzone będą przy użyciu frameworka [_pytest_](https://docs.pytest.org/en/7.2.x/).
- Użyty zostanie autoformatter [_autopep8_](https://pypi.org/project/autopep8/) pomagający dbać o spójny styl kodu źródłowego zgodny z wymaganiami _PEP8_.
- Do dbania o zachowanie poprawności typowania użyta zostanie biblioteka [_mypy_](http://mypy-lang.org/).
- Do tworzenia wykresów użyty zostanie biblioteka [_matplotlib_](https://matplotlib.org/).
- Dodatkowo użyta zostanie biblioteka [_isort_](https://pycqa.github.io/isort/) pozwalająca na automatyczne sortowanie deklaracji importowanych modułów.

### Rozszerzenia VSC

Do najważniejszych dla rozwiązania rozszerzeń używanych w projekcie należy zaliczyć:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python),
- [Pylace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).

## Dokumenty

### Notatki

- Wszystkie notatki na bieżąco tworzymy przy użyciu [Markdown](https://www.markdownguide.org/) i przechowujemy w repozytorium projektu.
- Użyte zostanie rozszerzenie VSC [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) zapewniające wsparcie dla języka markdown.
- Użyte zostaną rozszerzenia [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) oraz [Polish - Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-polish) dbające o poprawność ortograficzną tworzonych tekstów.

### Artykuł

Artykuł powstanie przy użyciu lokalnie budowanego projektu [Latex](https://www.latex-project.org/).
