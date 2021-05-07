# fretboard_generator

fretboard_generator generates fretboard diagrams for fretted string instruments. Let's run it in interactive mode, and call `pfb()` (i.e. "print fretboard") see what it can do:

```
$ python3 -i fretboard_generator.py
>>>
>>> pfb()

tuning:  E A D G B E   chord/scale:  E G# B 

 0  0 . . . O 0
 1  . . . O . .
 2  . O 0 . . .
 3  . . . . . .
 4  O . . O . O
 5  . . . . 0 .
 6  . . O . . .
 7  O 0 . . . O
 8  . . . . . .
 9  . . O 0 O .
10  . . . . . .
11  . O . . . .
12  0 . . . O 0
```

By default, fretboard diagram are returned for an E major chord in standard guitar tuning, showing where every E, G# and B can be found on the instrument's neck. Many chords, scales and instrument tunings are included as variables at the end of the file. Let's see where we can find the notes of a D minor chord on a ukelele:

```
>>> pfb(chord = d_m, tuning = ukelele)

tuning:  G C E A   chord/scale:  D F A 

 0  . . . O
 1  . . O .
 2  O 0 . .
 3  . . . .
 4  . . . .
 5  . O O 0
 6  . . . .
 7  0 . . .
 8  . . . O
 9  . O . .
10  O . 0 .
11  . . . .
12  . . . O
```

There are a handful of settings that can be changed in order to change the visual representation of the fretboard. Note in the output above that the root of the chord has been labelled, that is, that all instances of the note D are indicated with `0`s, while instances of other notes are labelled with `O`s. In order to display all the notes of the using `O`s, we can set `display_roots` to `False`. Notice the column of numbers on the left, indicating the fret number - this can be turned off by setting `number_frets` to `False`. There's also a header, indicating the notes of the instrument's open strings and the notes of the chord/scale. Let's turn this off by setting `print_header` to `False`.

```
>>> pfb(chord = d_m, tuning = ukelele, display_roots = False, number_frets = False, print_header = False)

 . . . O
 . . O .
 O O . .
 . . . .
 . . . .
 . O O O
 . . . .
 O . . .
 . . . O
 . O . .
 O . O .
 . . . .
 . . . O
```

Finally, notice how we get quite a tall diagram, including up to the twelfth fret. We can look at a smaller part of the fretboard by including only certain frets to be displayed by passing a list of fret numbers into the `fb` parameter. Let's set `fb` to `(0, 1, 2, 3)` to display only the ukelele's first three frets, and then set it to `(5, 6, 7)` to show the notes available if there was a capo on our ukelele at the fifth fret.

```
>>> pfb(chord = d_m, tuning = ukelele, fb = (0, 1, 2, 3))

tuning:  G C E A   chord/scale:  D F A 

 0  . . . O
 1  . . O .
 2  O 0 . .
 3  . . . .


>>> pfb(chord = d_m, tuning = ukelele, fb = (5, 6, 7))

tuning:  G C E A   chord/scale:  D F A 

 5  . O O 0
 6  . . . .
 7  0 . . .
```

## Generating fretboard diagrams to a file

Sometimes it's useful to be able to generate a bunch of fretboard diagrams for a specific tuning. fretboard_generator provides a function to write fretboard diagrams for chords to a file using `pfb_to_file()`. `pfb_to_file()` includes all the same parameters as `pfb()`, with one important distinction: rather than accepting a single chord as its input, it takes a list of chords. Let's use the built-in `maj_and_minor` variable to generate fretboard diagrams for all major and minor chords on a ukelele, and send the output to `uke_output.txt`.

```
>>> pfb_to_file(filename = 'uke_output.txt', chords_list = maj_and_min, tuning = ukelele)
>>>
```

## Beyond 12-tone equal temperament

Finally, if we want to explore some uncharted territory, we can use fretboard_generator.py to generate fretboards for different tuning systems. We can model a quarter-tone guitar (the entire octave is divided into 24 quarter tones) by setting `univ` to `24`. Say we want to learn how to play a C-neutral (notes C, E-half-flat and G) chord on a quarter-tone guitar tuned to standard tuning (EADGBE). In this case, we have to specify all the notes by the number of quarter-tones above C they are: our C-neutral chord will be notated `(0, 7, 14)`, and standard tuning will become `(8, 18, 4, 14, 22, 8)`. Once we leave 12-tone equal temperament, all bets are off for note names, so let's set `use_common_names` to `False` in order to display note names using numbers rather than letters.

```
>>> c_neutral = (0, 7, 14)
>>> standard_24 = (8, 18, 4, 14, 22, 8)
>>> pfb(chord = c_neutral, tuning = standard_24, univ = 24, use_common_names = False)

tuning:  8 18 4 14 22 8   chord/scale:  0 7 14 

 0  . . . O . .
 1  . . . . . .
 2  . . . . 0 .
 3  . . O . . .
 4  . . . . . .
 5  . . . . . .
 6  O 0 . . . O
 7  . . . . . .
 8  . . . . . .
 9  . . . . O .
10  . . O 0 . .
11  . . . . . .
12  . . . . . .
```

## Odds and ends

If you want your fretboards with more or less open space, you can change the `open_character`, `stopped_character` and `root_character` variables at the top of the file before running the program, or by setting the `o_ch`, `s_ch` and `r_ch` parameters when calling a function.

```
>>> pfb(o_ch = " . ", s_ch = " o ", r_ch = " R ")

tuning:  E A D G B E   chord/scale:  E G# B 

 0  R  .  .  .  o  R 
 1  .  .  .  o  .  . 
 2  .  o  R  .  .  . 
 3  .  .  .  .  .  . 
 4  o  .  .  o  .  o 
 5  .  .  .  .  R  . 
 6  .  .  o  .  .  . 
 7  o  R  .  .  .  o 
 8  .  .  .  .  .  . 
 9  .  .  o  R  o  . 
10  .  .  .  .  .  . 
11  .  o  .  .  .  . 
12  R  .  .  .  o  R 
```

`fretboard()` is mostly a helper function for `pfb()` and `pfb_to_file()`, but it returns a string of 1s and 0s separated by commas if you call it directly - potentially useful for piping into other functions.

```
>>> fretboard()
'100011,000100,011000,000000,100101,000010,001000,110001,000000,001110,000000,010000,100011'
```