# FlipFlop

## -= Puzzle 2: Rollercoaster Heights =-

You run into two suspiciously familiar inventors: **Feneas** and **Pherb** (not related to anyone famous). "We've designed the ultimate rollercoaster!" Feneas exclaims, handing you a blueprint. Pherb nods, silently. "We want to advertise it as the **tallest rollercoaster in the world**," Feneas continues. "Can you do that for us?"

_Aren't you two a bit young to be designing rollercoasters?_ you think to yourself. But you decide to help them out anyway.

The blueprint (your puzzle input) consists of a series of movements: **Up (`^`)** and **Down (`v`)**. Each movement corresponds to a change in height. The rollercoaster starts at **ground level (height = 0)**. Each **Up (`^`)** movement increases the height by **1 meter**, and each **Down (`v`)** movement decreases the height by **1 meter**.

**For example:**

Blueprint: `^v^v^v^v^v`
Movements: `up, down, up, down, up, down, up`
This blueprint results in the following heights:
`1, 0, 1, 0, 1, 0, 1, 0, 1, 0`
The highest point the coaster reaches in this example is **1 meter**.

Because the coaster is pretty awesome, **it can even descend below ground level!**

**Another Example:**

Blueprint: `^^^v^^^^vvvvvvv`
Movements: `up, up, up, down, up, up, up, up, down, down, down, down, down, down, down`
This blueprint results in the following heights:
`1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, -1`
The highest point the coaster reaches in this example is **6 meters**.

_What is the highest point the full coaster reaches?_

Your answer was: `145`

## -= Part 2: Aim Higher =-

You look at the numbers... and you realize they are way too small! The height changes are not linear anymore. Instead, each movement adds or subtracts a value that increases cumulatively.

* For consecutive **Up (`^`)** movements, the height increases by the **current movement number**. For example:

  * The 1st up movement increases the height by 1.
  * The 2nd consecutive up movement increases the height by 2.
  * The 3rd consecutive up movement increases the height by 3.
  * And so on.

* For consecutive **Down (`v`)** movements, the height decreases by the **current movement number**. For example:

  * The 1st down movement decreases the height by 1.
  * The 2nd consecutive down movement decreases the height by 2.
  * The 3rd consecutive down movement decreases the height by 3.
  * And so on.

When the direction changes (e.g., from Up to Down or Down to Up), **the count resets**.

**Here's a simple example:**

Blueprint: `^^^^^`
Movements: `up, up, up, up, up`
Height changes:

    1 up -> +1 -> 1
    2 up -> +2 -> 3
    3 up -> +3 -> 6
    4 up -> +4 -> 10
    5 up -> +5 -> 15

The highest point the coaster reaches in this example is **15 meters**.

**Revisiting the previous example:**

Blueprint: `^^^v^^^^vvvvvvv`
Movements: `up, up, up, down, up, up, up, up, down, down, down, down, down, down, down`
Height changes:

    1 up -> +1 -> 1
    2 up -> +2 -> 3
    3 up -> +3 -> 6
    1 down -> -1 -> 5
    1 up -> +1 -> 6
    2 up -> +2 -> 8
    3 up -> +3 -> 11
    4 up -> +4 -> 15
    1 down -> -1 -> 14
    2 down -> -2 -> 12
    3 down -> -3 -> 9
    4 down -> -4 -> 5
    5 down -> -5 -> 0
    6 down -> -6 -> -6
    7 down -> -7 -> -13

The highest point the coaster reaches in this example is also **15 meters**.

_What is the highest point the full coaster reaches with these steep height changes?_

Your answer was: `1971`

## -= Part 3: Aim Even Higher! =-

You look over at the coaster, and then back at the numbers... and you realize they are still _waaaay_ too small!

The height changes actually now follow the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) instead of the linear or stepwise patterns from before. A sequence of **Up (`^`)** or **Down (`v`)** movements now corresponds to the **Fibonacci value of the total number of movements**.

The height change for a consecutive sequence of movements is determined by the Fibonacci number of the total steps in that sequence:

* **n consecutive Up (`^`)** movements add `fib(n)` to the height.
* **n consecutive Down (`v`)** movements subtract `fib(n)` from the height.

When the direction changes (e.g., from Up to Down or Down to Up), **the count resets and the value is added or subtracted based on the Fibonacci sequence**.

**Fibonacci Sequence:**
The Fibonacci sequence is defined as follows:

    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    fib(3) = 2
    fib(4) = 3
    fib(5) = 5
    fib(6) = 8
    fib(7) = 13
    fib(8) = 21
    going on and on...

Each Fibonacci number is the sum of the two preceding numbers.

**Make sure to only add the amount once the sequence of movements ends or changes direction!**

**A simple coaster would be:**
Blueprint: `^^^^^`
Movements: `5 consecutive Up`
Height changes:

    5 consecutive Up -> fib(5) = 5 -> 5

The highest point the coaster reaches in this example is **5 meters**.

**The example from before:**
Blueprint: `^^^v^^^^vvvvvvv`
Movements: `3 consecutive Up, 1 consecutive Down, 4 consecutive Up, 7 consecutive Down` Height changes:

    3 consecutive Up -> (fib(3) = 2) -> 2
    1 consecutive Down -> (fib(1) = 1) -> 1
    4 consecutive Up -> (fib(4) = 3) -> 4
    7 consecutive Down -> (fib(7) = 13) -> -9

The highest point the coaster reaches in this example is **4 meters**.

**Example 3:**
Blueprint: `^^^^^^^^^^^^vvvvvvvvv^`
Movements: `12 consecutive Up, 9 consecutive Down, 1 consecutive Up`
Height changes:

    12 consecutive Up -> fib(12) = 144 -> 144
    9 consecutive Down -> fib(9) = 34 -> 110
    1 consecutive Up -> fib(1) = 1 -> 111

The highest point the coaster reaches in this example is **144 meters**.

_What is the highest point the full coaster reaches with these Fibonacci height changes?_

Your answer was: `49475`

You've completed all the parts for this puzzle! This earns you 3 Pointers \*\*\*!
