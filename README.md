
## [--- Day 1: Trebuchet?! ---](http://adventofcode.com/2023/day/1)

Here we are again! Let's get some stars!
Small gotcha today that *re.findall* does not do overlapping matches, 
but that can be solved with positive lookahead.
## [--- Day 2: Cube Conundrum ---](http://adventofcode.com/2023/day/2)
Just some 10 minute weekend holiday coding at the Ardennes! 
Nothing fancy.. part 2 was given the way I solved part 1.

## [--- Day 3: Gear Ratios ---](http://adventofcode.com/2023/day/3)
No time today, so solved it on day 4 as straight forward as
I could. Duplicate code and everything! But not worth the effort
to make a nicer implementation. Save the time for harder problems.

## [--- Day 4: Scratchcards ---](http://adventofcode.com/2023/day/4)
Nice puzzle in which you really need to pay attention to details
when reading the description. After grasping the idea, the programming
was not so hard and integrating part 2 with part 1 worked like a 
charm. After some advent of codes in which defaultdict was really
a default in my solutions, here I could revisit it once more.
GPT4 can solve days 2 and 4, without a problem or extra input, 
it's getting crazy. Maybe it already pulls some fresh solutions from
the AoC reddit megathread or github repo's, than it is less magic, 
who knows, but I fear it comes up with its own magic ;-)

## [--- Day 5: If You Give A Seed A Fertilizer ---](http://adventofcode.com/2023/day/5)
If it is brute-forceable: go for it :') For part two reversing from
destination (location) to source (seed) made it doable. It was faster
with calculating the answer than me coding a better way with ranges,
so, this is it and I'm fine with it. 10 stars!

## [--- Day 6: Wait For It ---](http://adventofcode.com/2023/day/6)
A breather today. Easy solution which worked for part 2, after noticing
it was symmetric it became a fast solution.

## [--- Day 7: Camel Cards ---](http://adventofcode.com/2023/day/7)
Good old poker game simulation! Fun one, decided just to go with
an OO style simulation, which worked fine and fast. No real weird
challenges along the way. Not very pythonic or compact code, but
I wanted to keep it readable and understandable.

## [--- Day 8: Haunted Wasteland ---](http://adventofcode.com/2023/day/8)
Classic solution for all AoC-veterans. Cycle check and use LCM. 
Apparantly the python math library has a lcm function since 3.9
which supports an arbitrary amount of arguments. Perfect for today!
No need for numpy or own math skills.

## [--- Day 9: Mirage Maintenance ---](http://adventofcode.com/2023/day/9)
A fine short weekend puzzle today. Part 2 was almost the same as 
part 1, no real increased difficulty. Probably could do it very easily
in reversed way, if you solve part 1 clean.

## [--- Day 10: Pipe Maze ---](http://adventofcode.com/2023/day/10)
Went a bit crazy, cause I had a stupid bug in my first approach that I 
couldn't figure out. I tried to expand the grid, so I could floodfill 
it easily. Took a different turn later tried some possibilties to
create polygons and check if points are inside or not.. so matplotlib 
does the heavy lifting today. But I actually enjoyed this one to think 
about!

## [--- Day 11: Cosmic Expansion ---](http://adventofcode.com/2023/day/11)
For part 1 I expanded the grid as a quick solution, but already guessed that 
would not work for p2. Had the sample input working fast, but made an error 
which took some time to figure out, went back to p1 and solved that again
ith my "new" approach and got my bug fixed. Code got even shorter this way.
Should probably use numpy or pandas for these kind of operations. but I like
basic python.

## [--- Day 12: Hot Springs ---](http://adventofcode.com/2023/day/12)
Solved part 1 with a cool regex with the corresponding combinations, worked
like a charm! Then part 2 came along and we needed a faster more scalable 
solution, so need to sit down and (re)curse at it and throw in lru_cache in
the mix. Easier said then done, but solved it after the lunch break.

## [--- Day 13: Point of Incidence ---](http://adventofcode.com/2023/day/13)
My first idea worked (look for two similar strings next to each other, 
and from the edge to that point check the symmetry). 
For part 2 I first didn't account for the original reflection (so just 
which came first was the "hit"), took some time to debug that.. maybe had 
to think a little better. But once I got that it worked and runs in ~70ms.
Don't like the big nested loops and flow, code is also not very explanatory..
but it is what it is today (edited)

## [--- Day 14: Parabolic Reflector Dish ---](http://adventofcode.com/2023/day/14)
Ugliest solution up till now! Didn't have time to finish it, so made it
up today. Got stuck on part 2 for quite some time, thinking first the
grid needed to be tilted to the north before calculating the score (as in
part 1), so got all wrong score numbers. Took a while.. But after that did
a cycle detection, again with a slow method.. took the scores instead of
a representation of the rocks. It works and probably for the inputs in general,
but could be refactored a lot.. but still need to do Day 15!

## [--- Day 15: Lens Library ---](http://adventofcode.com/2023/day/15)
Fun day, not very difficult, but the explanation of part 2 was big, had to
read carefully! Just fiddled a bit with comprehensions to make it short, 
but still some "classic" bigger flows going one. Kinda start to like the
"else"-clause in a for-loop, instead of a "found" boolean or something.

## [--- Day 16: The Floor Will Be Lava ---](http://adventofcode.com/2023/day/16)
Nice mellow weekend day. Quick coding, slow runtime solution (4s or something), 
spend more time puzzling today with "Darda" racetracks for/with my kids.
But I like the style of these puzzles, I won't ask for more challenging ones,
because that will result in a big hard puzzle tomorrow I guess ;-)

## [--- Day 17: Clumsy Crucible ---](http://adventofcode.com/2023/day/17)
Tough day! Knew what to do, sort of, but got clumsy with the states in Dijkstra.
So resulted in Dijksdrama, but could refactor a bit to get p1 and p2 in one
solution which is kinda robust, also for different starting points. And is 
slowwww. Hardest day to debug for me this year (till now, wait for the monday
monster ;-))

## [--- Day 18: Lavaduct Lagoon ---](http://adventofcode.com/2023/day/18)
For part 1 decided to do floodfill from the outside without bugs, cause that 
didn't work on day 10. Because I did some reading after day 10 about this 
problem already (like many of you I guess), decided to go for understanding 
that theory (shoelace + pick's) and just implemented it. Not too excited about 
this one, because I don't see the real difference with day 10 (except everyone 
has different bugs on different days..). 

## [--- Day 19: Aplenty ---](http://adventofcode.com/2023/day/19)
Part 1 parsing was most of the fun. Part 2 just figuring out how this is
a graph and it can be searched for the ends and adjust the ranges accordingly.
That took me some time and along the way thought of some different approaches.
Seems similar as day 5, but now I really do a search with adjusted ranges instead
of starting at the end and backtracking it.

## [--- Day 20: Pulse Propagation ---](http://adventofcode.com/2023/day/20)
A lot of reading to do! Didn't take too much time, just follow the rules of
the examples and it works. On the flipside; part 2 didn't even have a testcase,
so it was looking for a clue in the input. That could be found by noting that
the "con" sending to "rx" was dependent of 4 flips. So check when all flips are
on by cycledetection and lcm and done!

## [--- Day 21: Step Counter ---](http://adventofcode.com/2023/day/21)
When reading the first part, I first didn't know why it was so elaborately 
explained, just bfs/dfs, right? Almost.. but a small change, which took
some adjustment. The second part was really difficult to extrapolate, 
especially when just looking at the example. When later examining the input,
the challenge changed. There were "corridors" from the starting point to the end
of the grids in all directions. Also there was a wide "diamond" corridor.
In this sparse grid and with these specifications, it became a bit clearer.
Drawing the biiiiig diamond and shuffling with some length numbers it worked
out. The idea from the input was not that hard, but get the details right took
my quite some time. Without a sample input which was similar, it made it even
more difficult to test, but with some smaller testcases, I got there finally.

## [--- Day 22: Sand Slabs ---](http://adventofcode.com/2023/day/22)
Family fever weekend. Still need to do the second part, started with it, but really
need to rest! Catched up: nice puzzle. I am using a recursive approach for p2, which works
great with the data I could gather in P1 (which I didn't have yet, but could easily extend)

## [--- Day 23: A Long Walk ---](http://adventofcode.com/2023/day/23)
Family fever weekend, but managed to finish it with a very boring bfs method which
is really slow. Took some time to figure out how to simplify the grid to a graph.

## [--- Day 24: Never Tell Me The Odds ---](http://adventofcode.com/2023/day/24)
Ah, there it is, the Z3/Sympy/whatever math library you have: throw it at
this problem! I have been there: stuck for hours and hours with these problems,
math way above my head. Not this year! Used Sympy for p2 to change it up. One
puzzle left. Difficult puzzles with diffculties with family fever these last
days, made this definitely one of the harder years for me and not so enjoyable
as earlier years. Also because of a lot of repetition and maybe "have seen it all"-
feeling. I was not as engaged as before. We'll see what next year brings.

## [--- Day 25: Snowverload ---](http://adventofcode.com/2023/day/25)
Just for once handed it over to NetworkX. It's a maxflow/mincut problem, and networkX
(or iGraph!) can handle this for you, so why not! Off to bed, unfortunately, with
pneumonia for me, so need some rest!
