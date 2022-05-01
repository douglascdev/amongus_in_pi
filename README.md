# Among Us in π

```
   ________
__|  ______|
|    |_____|
|__   __   | 
  |__|  |__|
```

An algorithm that scans the digits of pi for the amongus above in binary form:

```
0, 1, 1, 1,
1, 1, 0, 0,
1, 1, 1, 1,
0, 1, 0, 1,
```

## But.. why?

I don't know, why not?

After seeing [this video](https://www.youtube.com/watch?v=dET2l8l3upU) by Matt Parker I wanted to implement my own algorithm to search for...amonguses? Amongi? Well, let's see how it goes.

## How?

From what I understand Matt's way of doing it was to use pi calculated to a certain precision, ignore the integer part of pi, treat the decimals as an integer and convert the number to binary. This approach leads to very different binary representations of the number depending on the precision used to calculate pi:
```
3.1415        =>  1415       =>  10110000111
3.1415927     =>  1415927    =>  101011001101011110111
3.141592654   =>  141592654  =>  1000011100001000100001001110
```

So my approach was to convert each decimal digit of pi according to the following rule:
```
If digit <= 4, turn it into a 0
If digit >= 5, turn it into a 1
```

This should lead to more consistent results:
```
3.1415        =>  1415       =>  0001
3.1415927     =>  1415927    =>  0001101
3.141592654   =>  141592654  =>  000110110
```

Current results for pi with 500.000 digits of precision was:

```

       ________
    __|  ______|
    |    |_____|
    |__   __   | 
      |__|  |__|
    
Something sus about digits => 37422 to 37438
Something sus about digits => 142369 to 142385
Something sus about digits => 154794 to 154810
Something sus about digits => 178012 to 178028
Something sus about digits => 348179 to 348195
Something sus about digits => 467472 to 467488

```