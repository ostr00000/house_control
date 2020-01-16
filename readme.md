
# Cel projektu
Projekt ma dostarczyć narzędzie do obsługi urządzeń w domu za pomocą 
wypowiadanych poleceń. Celem jest przetworzenie tekstu na odpowiadającą mu
akcję.


# Opis dzialania
Komenda do przetworzenia jest analizowana w następujący sposób:
- wykrywane są możliwe rodzaje poleceń - przypisywana jest odpowiednia waga
- wykrywane są możliwe miejsca, do którego odwołuje się polecenie - przypisywana jest odpowiednia waga
- wykrywane są możliwe urządzenia, przydzielana jest ocena bazująca na następujących właściwościach (od najbardziej istotnych):
    - czy urządzenie zwróciło wartość twierdzącą dla odpowiedniej komendy (domyślnie tak)
    - liczba pokrywających się słów z opisu urządzenia i komendy, ale bez słów opisujących miejsce
    - uwzględnia czy lokalizacja jest na liście możliwych miejsc
    - uwzględnia czy urządzenie jest w tym samym pomieszczeniu co wypowiadający polecenie   
    - poziom zagłębienia w lokalizacji - bardziej 
- wybierany jest rodzaj akcji z największą wagą
    - gdy jest kilka takich urządzeń, pierwszeństwo mają akcje, które są możliwe do wykonania na możliwych urządzeniach
    - gdy nie znaleziono żadnej akcji, wyszukiwane jest urządzenie, gdy urządzenie ma zdefiniowaną domyślną akcje jest ona wybierana
- wybierane jest urządzenie z największą wagą
    - gdy jest kilka takich urządzeń, pierwszeństwo mają urządzenia agregujące
    - gdy nie znaleziono żadnego urządzenia, a możliwa lokalizacja jest tylko jedna:
        - gdy jest jedno urządzenie, jest ono wybierane
        - filtrowane są urządzenia mające możliwą akcje, jeśli jest tylko jedno takie, jest ono wybierane    
    
## Opis lokalizacji
## Opis urzadzen
## Opis akcji

# Przygotowanie

### Git repository
Wymagany jest plik zawierający pogrupowane słowa.
```shell script
git submodule init
git submodule update
```

### Python environment
Requirement python>=3.8
```shell script
python -m venv house_control_env
source ./house_control_env/bin/activate
pip install -r requirements.txt
```

### Class relations
![diagram](docs/class_relations_diagram.png)