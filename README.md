# polygon
[![Build Status](https://travis-ci.org/pl461516/polygon.svg?branch=master)](https://travis-ci.org/pl461516/polygon)

##Projekt na zaliczenie modułu "Środowiska i narzędzia wytwarzania oprogramowania"
Autor: Patryk Ligenza, gr 1


### Jak używać programu:

W linii komend należy wpisać na przykład:
```sh
$ python polygon.py x1 y1 x2 y2 x3 y3
```
Powyższe wywołanie zwróci pole trójkąta o wierzchołkach: (x1, y1), (x2, y2) oraz (x3, y3)

### Przykładowe wyniki:

```sh
$ python polygon.py 3 5 5 7 2 5
1.0
```
```sh
$ python polygon.py 2 4 3 7 14 34 6 10 7 15
19.0
```
```sh
$ python polygon.py 2 4 14 34 6 10 7 15 3 7
19.0
```
```sh
$ python polygon.py 3 4 5 11 12 8 9 5 5 6
30.0
```
```sh
$ python polygon.py -2 14 -3.4 7.1 6.0 -10
44.400000000000006
```

###Dodatkowe informacje:
 - Algorytm nie działa w przypadku, gdy jeden z punktów jest mocno oddalony od reszty.
 - Nie jest wymagane podawanie punktów w określonym porządku, ponieważ program
   potrafi samodzielnie je posortować.



