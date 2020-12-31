# MultiplicativePersistence
Algoritmo que busca números com uma persistência multiplicativa de N etapas.

A persistência consiste em multiplicar todos os numeros de um digite, encontrando assim um novo número. Faz-se o mesmo com o novo número gerado e assim sucessivamente, até que a sequência chegue ao valor 0. O algoritmo busca valores que passem por N etapas.

Exemplo de persistência multiplicativa:


1. 277777788888899 → 2x7x7x7x7x7x7x8x8x8x8x8x8x9x9 = 4996238671872
2. 4996238671872 → 4x9x9x6x2x3x8x6x7x1x8x7x2 = 438939648
3. 438939648 → 4x3x8x9x3x9x6x4x8 = 4478976
4. 4478976 → 4x4x7x8x9x7x6 = 338688
5. 338688 → 3x3x8x6x8x8 = 27648
6. 27648 → 2x7x6x4x8 = 2688
7. 2688 → 2x6x8x8 = 768
8. 768 → 7x6x8 = 336
9. 336 → 3x3x6 = 54
10. 54 → 5x4 = 20
11. 20 → 2x0 = 0
