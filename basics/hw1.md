1. Define a function, that takes string as argument `arg` and prints `"Hello, %arg%!"`
2. Define a function `sum()` and a function `multiply()` that sums and multiplies (respectively) all the numbers in a list of numbers. For example, `sum([1, 2, 3, 4])` should return 10, and `multiply([1, 2, 3, 4])` should return 24.
3. Define a function `reverse()` that computes the reversal of a string. For example, `reverse("I am testing")` should return the string "gnitset ma I".
4. Define a function `isPalindrome()` that recognizes palindromes (i.e. words that look the same written backwards). For example, `isPalindrome("radar")` should return True.
5. Define a procedure `histogram()` that takes a list of integers and prints a histogram to the screen. For example, `histogram([4, 9, 7])` should print the following:

```
****
*********
******
```

(usage some kind of sleep for better visualization)

6. Define a function `caesarCipher` that takes string and `key(number)`, whuch returns encrypted string
7. define a function `diagonalReverse()` that takes matrix and returns diagonal-reversed one:

```
1 2 3         1 4 7
4 5 6 returns 2 5 8
7 8 9         3 6 9
```

8. Write a function `game()` number-guessing game, that takes 2 int parameters defining the range. Using some kind of `random` function to generate random int from the range. While user input isn't equal that number, print "Try again!". If user guess the number, congratulate him and exit.

9. Define a function, which takes a string with N opening brackets `("[") and N closing brackets ("]")`, in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:

```
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
```

10. Write a function `charFreq()` that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like `charFreq("abbabcbdbabdbdbabababcbcbab")`.

11. Write a function `decToBin()` that taces decimal integer and outputs its binary representation.

12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as an order of matrix, randomly generates index (x, y) and checks user input (2 integers).

hard task: Visualize the game.
