# FlipFlop

## -= Puzzle 7: Hyper Grids =-

You've gotten quite far in your journey through C-land, and now you find yourself at your final destination: the map makers' guild.

You arrive at the map makers' guild in C-land. The guild is filled with maps of all shapes and sizes, and you're eager to explore them all.

You meet the guild master, who hands you a few maps of empty grids (your puzzle input). "We need you to find the shortest path to the farthest corner of each grid," they explain.

"After that, you need to determine the number of distinct shortest paths to the farthest corner"

Your input consists of a series of sizes, like this:

    2 2
    3 3
    2 3

The first number in each line represents the number of rows, and the second number represents the number of columns in the grid.

Mapping these 3 grids out would make them look something like this:

          ..       ...       ..
    2 2 = .. 3 3 = ... 2 3 = ..
                   ...       ..

We can then mark the start and end positions like this:

          S.       S..       S.
    2 2 = .E 3 3 = ... 2 3 = ..
                   ..E       .E

One of the shortest paths to the farthest corner of each grid is then:

          -+       --+       -+
    2 2 = .| 3 3 = ..| 2 3 = .|
                   ..|       .|

The shortest path for the first grid is **3** steps long, the shortest path for the second grid is **5** steps long, and the shortest path for the third grid is **4** steps long.

Now, the guild master wants you to determine **how many shortest paths exist for each grid**.

For example, the first grid has **2** shortest paths, the second grid has **6** shortest paths, and the third grid has **3** shortest paths.

Here are all the shortest paths:

          -+     |.
    2 2 = .| and +-


          --+   -+.   |..   |..   |..     -+.
    3 3 = ..| , .++ , +-+ , ++. , |.. and .|.
          ..|   ..|   ..|   .+-   +--     .+-

          -+   |      |.
    2 3 = .| , ++ and |.
          .+   .|     +-

Your answer is the sum of the number of shortest paths for each grid. For all the examples that answer is **11**.

_What is the sum of the number of shortest paths for each grid?_

Your answer was: `221`

## -= Part 2: Stepping into the Third Dimension =-

The guild master is impressed by your work, but they have more challenges for you.

"You've mastered the 2D grids, but can you handle the 3D grids?" they ask.

The same grid maps are now in 3D, with the third dimension being equal to the first dimension.
A grid X × Y becomes a box of size X × Y × X.

The 3 grids from the previous example become boxes of size `2 × 2 × 2`, `3 × 3 × 3`, and `2 × 3 × 2`.
As shown, the last number is equal to the first number.

Like before, you can take steps in each dimension, x, y, and z respectively.
Your goal again is to find the amount of shortest paths from 1 corner to the farthest corner from that corner.

The amount of shortest paths for the first box is **6**, for the second box is **90** and for the third box is **12**.

The sum of the number of shortest paths for each grid is **108**.

_What is the sum of the number of shortest paths for each 3D grid?_

Your answer was: `4079922`

## -= Part 3: Infinite Dimensions! =-

The guild master is now very impressed by your work, and they have one final challenge for you.

"You've mastered the 3D grids, but can you handle infinite dimensions?" they ask.

The numbers you have now mean something different. The first number is the number of dimensions, and the second number is the length of each dimension.

For example, the grid `2 2` would mean a 2D grid of size `2 × 2`, and the grid `3 3` would mean a 3D grid of size `3 × 3 × 3`.

The slightly more complex grid `2 3` would mean a 2D grid of size `3 × 3`.

For these 3 simpler examples, the amount of shortest paths for each grid is **2**, **90**, and **6** respectively.

Here is another example:

`4 3` would mean a 4D grid of size `3 × 3 × 3 × 3`.

The amount of shortest paths for this grid is **2520**.

You may move in any dimension, in any direction, just like before — only now, there are more dimensions to consider.

Watch out! The number of distinct shortest paths can grow very large, make sure to use a data type that can handle large numbers.

_Your final challenge!_

_What is the sum of the number of shortest paths for each grid?_

Your answer was: `455219065224`

You've completed all the parts for this puzzle! This earns you 3 Pointers \*\*\*!
