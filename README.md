# Blum-Blum-Shub

Implemented for Cryptography course

Vide demo https://streamable.com/aqxnxl

### Explicatie pentru corectare
Am ales sa implemetentez Blum blumb shub.

Ideea principala e ca foloseste formula X(n+1) = X(n)^2 (mod M)

Se pleaca de la un X(0), numit si seed, generat random prin `random.randint(1, 1e10)`

Apoi se ia cel mai putin significant bit(adica cel mai din dreapta bit dupa ce convertesti nr in baza 2) si se concateneaza la ceilalti biti obtinuti.

M = p*q, unde p si q trebuie sa fie numere prime unde p si q sunt congruente cu 3(mod 4).
Logica este la functia `def next_prime(num)`.

Am folosit `tkinter` pt GUI unde este un input(functioneaza doar daca se introduce corect un int, nu un string oarecare).

Rezultatul este un sir de caractere care este scris in fisierul `output`.



