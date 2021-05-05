"""
Generates fret diagrams for string instruments.

A number of instrument tunings, chords and scales are found at the end
of the file.
"""

universe = 12 #size of pitch-class universe
fretboard_length = 12
open_character = " ."
stopped_character = " O"
root_character = " 0"
new_line_character = "\n"


def fretboard(chord = (4, 8, 11), tuning = (4, 9, 2, 7, 11, 4),
              fb = range(fretboard_length + 1), univ = universe,
              o_ch = "0", s_ch = "1", r_ch = "r", n_ch = ",",
              display_roots = False, number_frets = False):
    """
    Returns a fretboard diagram as a string.
    'chord' is the chord or scale to be labelled - list of integers
    'tuning' is the tuning of the instrument - list of integers
    'fb' is which frets to display - list of integers
    'o_ch' is the character used to indicate an unstopped (open) string
    's_ch' is the character used to indicate a stopped (depressed) string
    'r_ch' is the character used to indicate the root of the chord/scale
    'n_ch' is the character used to indicate a new line
              
    By default, returns an E major chord in standard guitar tuning
    """
    
    # warn user if the open, stopped and root characters are different lengths
    if len(o_ch) != len(s_ch) or len(o_ch) != len(r_ch):
        print("\nwarning! o_ch, s_ch and r_ch are not all the same length.")
    
    output = ""

    # generate fretboard by checking whether each string/fret combination
    # is a member of the given chord
    for fret in fb:
        row_output = ""
        if number_frets:
            row_output = row_output + '%2s ' % str(fret)
        for string in tuning:
            if (string + fret) % univ == chord[0]:
                # if user has requested that chord roots be identified,
                # highlight the first member of the chord
                if display_roots:
                    row_output = row_output + r_ch
                else: row_output = row_output + s_ch
            elif (string + fret) % univ in chord:
                row_output = row_output + s_ch
            else:
                row_output = row_output + o_ch
        output = output + row_output + n_ch

    #remove final line break
    return output[:-1]


def formatted(chord = (4, 8, 11), tuning = (4, 9, 2, 7, 11, 4),
        fb = range(fretboard_length + 1), univ = universe,
        o_ch = open_character, s_ch = stopped_character,
        r_ch = root_character, n_ch = new_line_character,
        display_roots = True, print_header = True, number_frets = True,
        use_common_names = True, sharps = False, flats = False):
    """
    A helper function for pfb() and pfb_to_file().
    Returns fretboard in a nicely formatted manner.
    """
    
    #create header indicating tuning and notes of chord
    output = "\n"
    if print_header:
        #print notes of instrument tuning
        header_output = "tuning:  "
        for string in tuning:
            if use_common_names == True:
                header_output = header_output + note_name(string, flats,
                                                          sharps) + " "
            else:
                header_output = header_output + str(string) + " "
        #print the notes of the chord/scale being displayed
        header_output = header_output + "  chord/scale:  "
        for note in chord:
            if use_common_names == True:
                header_output = header_output + note_name(note, flats,
                                                          sharps) + " "
            else:
                header_output = header_output + str(note) + " "
        output = output + header_output + "\n\n"

    #append fretboard diagram
    output = output + fretboard(chord, tuning, fb, univ,
                                o_ch, s_ch, r_ch, n_ch,
                                display_roots, number_frets) + "\n\n"

    return output
    
    
def pfb(chord = (4, 8, 11), tuning = (4, 9, 2, 7, 11, 4),
        fb = range(fretboard_length + 1), univ = universe,
        o_ch = open_character, s_ch = stopped_character,
        r_ch = root_character, n_ch = new_line_character,
        display_roots = True, print_header = True, number_frets = True,
        use_common_names = True, sharps = False, flats = False):
    """
    pfb, i.e. print fretboard.
    Prints nicely formatted fretboard.
    """
    
    print(formatted(chord, tuning, fb, univ, o_ch, s_ch, r_ch, n_ch,
                    display_roots, print_header, number_frets,
                    use_common_names, sharps, flats))


def pfb_to_file(filename = "pfb_output.txt",
                chords_list = ((0, 4, 7), ), tuning = (4, 9, 2, 7, 11, 4),
                fb = range(fretboard_length + 1), univ = universe,
                o_ch = open_character, s_ch = stopped_character,
                r_ch = root_character, n_ch = new_line_character,
                display_roots = True, print_header = True, number_frets = True,
                use_common_names = True, sharps = False, flats = False):
    """
    For every chord in chords_list, prints nicely formatted fretboard
    to file.
    """
    
    output_string = ''
    
    # generate a fretboard diagram for each 
    for chord in chords_list:
        output_string = (output_string +
                         formatted(chord, tuning, fb, univ,
                                   o_ch, s_ch, r_ch, n_ch,
                                   display_roots, print_header,
                                   number_frets, use_common_names,
                                   sharps, flats)
                         )

    # write all generated files to output_file
    with open(filename, "a") as output_file:
        output_file.write(output_string)


def note_name(pitch, flats = False, sharps = False):
    """
    A helper function for formatted().
    For a note in integer notation, returns the note's common name.
    Works only in 12TET. By default, returns Bb, Eb and F#, C#, G#.
    """
    
    if sharps and flats:
        print("note_name() error: both sharps and flats are True")
        return str(pitch)
    if pitch == 0:
        return "C"
    elif pitch == 1:
        if flats: return "Db"
        else: return "C#"
    elif pitch == 2:
        return "D"
    elif pitch == 3:
        if sharps: return "D#"
        else: return "Eb"
    elif pitch == 4:
        return "E"
    elif pitch == 5:
        return "F"
    elif pitch == 6:
        if flats: return "Gb"
        else: return "F#"
    elif pitch == 7:
        return "G"
    elif pitch == 8:
        if flats: return "Ab"
        else: return "G#"
    elif pitch == 9:
        return "A"
    elif pitch == 10:
        if sharps: return "A#"
        else: return "Bb"
    elif pitch == 11:
        return "B"
    else:
        print("note_name() error: pitch not within 0 - 11")
        return str(pitch)



#various tunings
standard = (4, 9, 2, 7, 11, 4)
drop_d = (2, 9, 2, 7, 11, 4)
double_drop_d = (2, 9, 2, 7, 11, 2)
dadgad = (2, 9, 2, 7, 9, 2)
open_d = (2, 9, 2, 6, 9, 2)
open_e = (4, 11, 4, 8, 11, 4)
open_g = (2, 7, 2, 7, 11, 2)
open_a = (4, 9, 4, 9, 1, 4)
lute = (4, 9, 2, 6, 11, 4)
new_standard = (0, 7, 2, 9, 4, 7)
mandolin = (7, 2, 9, 4)
ukelele = (7, 0, 4, 9)

#various chords
c_M = (0, 4, 7)
c_m = (0, 3, 7)
c_o = (0, 3, 6)
c_M7 = (0, 4, 7, 11)
c_7 = (0, 4, 7, 10)
c_m7 = (0, 3, 7, 10)
c_m7b5 = (0, 3, 6, 10)
c_o7 = (0, 3, 6, 9)
db_M = (1, 5, 8)
db_m = (1, 4, 8)
db_o = (1, 4, 7)
db_M7 = (1, 5, 8, 0)
db_7 = (1, 5, 8, 11)
db_m7 = (1, 4, 8, 11)
db_m7b5 = (1, 4, 7, 11)
db_o7 = (1, 4, 7, 10)
d_M = (2, 6, 9)
d_m = (2, 5, 9)
d_o = (2, 5, 8)
d_M7 = (2, 6, 9, 1)
d_7 = (2, 6, 9, 0)
d_m7 = (2, 5, 9, 0)
d_m7b5 = (2, 5, 8, 0)
d_o7 = (2, 5, 8, 11)
eb_M = (3, 7, 10)
eb_m = (3, 6, 10)
eb_o = (3, 6, 9)
eb_M7 = (3, 7, 10, 2)
eb_7 = (3, 7, 10, 1)
eb_m7 = (3, 6, 10, 1)
eb_m7b5 = (3, 6, 9, 1)
eb_o7 = (3, 6, 9, 0)
e_M = (4, 8, 11)
e_m = (4, 7, 11)
e_o = (4, 7, 10)
e_M7 = (4, 8, 11, 3)
e_7 = (4, 8, 11, 2)
e_m7 = (4, 7, 11, 2)
e_m7b5 = (4, 7, 10, 2)
e_o7 = (4, 7, 10, 1)
f_M = (5, 9, 0)
f_m = (5, 8, 0)
f_o = (5, 8, 11)
f_M7 = (5, 9, 0, 4)
f_7 = (5, 9, 0, 3)
f_m7 = (5, 8, 0, 3)
f_m7b5 = (5, 8, 11, 3)
f_o7 = (5, 8, 11, 2)
gb_M = (6, 10, 1)
gb_m = (6, 9, 1)
gb_o = (6, 9, 0)
gb_M7 = (6, 10, 1, 5)
gb_7 = (6, 10, 1, 4)
gb_m7 = (6, 9, 1, 4)
gb_m7b5 = (6, 9, 0, 4)
gb_o7 = (6, 9, 0, 3)
g_M = (7, 11, 2)
g_m = (7, 10, 2)
g_o = (7, 10, 1)
g_M7 = (7, 11, 2, 6)
g_7 = (7, 11, 2, 5)
g_m7 = (7, 10, 2, 5)
g_m7b5 = (7, 10, 1, 5)
g_o7 = (7, 10, 1, 4)
ab_M = (8, 0, 3)
ab_m = (8, 11, 3)
ab_o = (8, 11, 2)
ab_M7 = (8, 0, 3, 7)
ab_7 = (8, 0, 3, 6)
ab_m7 = (8, 11, 3, 6)
ab_m7b5 = (8, 11, 2, 6)
ab_o7 = (8, 11, 2, 5)
a_M = (9, 1, 4)
a_m = (9, 0, 4)
a_o = (9, 0, 3)
a_M7 = (9, 1, 4, 8)
a_7 = (9, 1, 4, 7)
a_m7 = (9, 0, 4, 7)
a_m7b5 = (9, 0, 3, 7)
a_o7 = (9, 0, 3, 6)
bb_M = (10, 2, 5)
bb_m = (10, 1, 5)
bb_o = (10, 1, 4)
bb_M7 = (10, 2, 5, 9)
bb_7 = (10, 2, 5, 8)
bb_m7 = (10, 1, 5, 8)
bb_m7b5 = (10, 1, 4, 8)
bb_o7 = (10, 1, 4, 7)
b_M = (11, 3, 6)
b_m = (11, 2, 6)
b_o = (11, 2, 5)
b_M7 = (11, 3, 6, 10)
b_7 = (11, 3, 6, 9)
b_m7 = (11, 2, 6, 9)
b_m7b5 = (11, 2, 5, 9)
b_o7 = (11, 2, 5, 8)

#various scales/modes
c_major = (0, 2, 4, 5, 7, 9, 11)
c_dorian = (0, 2, 3, 5, 7, 9, 10)
c_phrygian = (0, 1, 3, 5, 7, 8, 10)
c_lydian = (0, 2, 4, 6, 7, 9, 11)
c_mixolydian = (0, 2, 4, 5, 7, 9, 10)
c_aeolian = (0, 2, 3, 5, 7, 8, 10)
c_locrian = (0, 1, 3, 5, 6, 8, 10)
db_major = (1, 3, 5, 6, 8, 10, 0)
db_dorian = (1, 3, 4, 6, 8, 10, 11)
db_phrygian = (1, 2, 4, 6, 8, 9, 11)
db_lydian = (1, 3, 5, 7, 8, 10, 0)
db_mixolydian = (1, 3, 5, 6, 8, 10, 11)
db_aeolian = (1, 3, 4, 6, 8, 9, 11)
db_locrian = (1, 2, 4, 6, 7, 9, 11)
d_major = (2, 4, 6, 7, 9, 11, 1)
d_dorian = (2, 4, 5, 7, 9, 11, 0)
d_phrygian = (2, 3, 5, 7, 9, 10, 0)
d_lydian = (2, 4, 6, 8, 9, 11, 1)
d_mixolydian = (2, 4, 6, 7, 9, 11, 0)
d_aeolian = (2, 4, 5, 7, 9, 10, 0)
d_locrian = (2, 3, 5, 7, 8, 10, 0)
eb_major = (3, 5, 7, 8, 10, 0, 2)
eb_dorian = (3, 5, 6, 8, 10, 0, 1)
eb_phrygian = (3, 4, 6, 8, 10, 11, 1)
eb_lydian = (3, 5, 7, 9, 10, 0, 2)
eb_mixolydian = (3, 5, 7, 8, 10, 0, 1)
eb_aeolian = (3, 5, 6, 8, 10, 11, 1)
eb_locrian = (3, 4, 6, 8, 9, 11, 1)
e_major = (4, 6, 8, 9, 11, 1, 3)
e_dorian = (4, 6, 7, 9, 11, 1, 2)
e_phrygian = (4, 5, 7, 9, 11, 0, 2)
e_lydian = (4, 6, 8, 10, 11, 1, 3)
e_mixolydian = (4, 6, 8, 9, 11, 1, 2)
e_aeolian = (4, 6, 7, 9, 11, 0, 2)
e_locrian = (4, 5, 7, 9, 10, 0, 2)
f_major = (5, 7, 9, 10, 0, 2, 4)
f_dorian = (5, 7, 8, 10, 0, 2, 3)
f_phrygian = (5, 6, 8, 10, 0, 1, 3)
f_lydian = (5, 7, 9, 11, 0, 2, 4)
f_mixolydian = (5, 7, 9, 10, 0, 2, 3)
f_aeolian = (5, 7, 8, 10, 0, 1, 3)
f_locrian = (5, 6, 8, 10, 11, 1, 3)
gb_major = (6, 8, 10, 11, 1, 3, 5)
gb_dorian = (6, 8, 9, 11, 1, 3, 4)
gb_phrygian = (6, 7, 9, 11, 1, 2, 4)
gb_lydian = (6, 8, 10, 0, 1, 3, 5)
gb_mixolydian = (6, 8, 10, 11, 1, 3, 4)
gb_aeolian = (6, 8, 9, 11, 1, 2, 4)
gb_locrian = (6, 7, 9, 11, 0, 2, 4)
g_major = (7, 9, 11, 0, 2, 4, 6)
g_dorian = (7, 9, 10, 0, 2, 4, 5)
g_phrygian = (7, 8, 10, 0, 2, 3, 5)
g_lydian = (7, 9, 11, 1, 2, 4, 6)
g_mixolydian = (7, 9, 11, 0, 2, 4, 5)
g_aeolian = (7, 9, 10, 0, 2, 3, 5)
g_locrian = (7, 8, 10, 0, 1, 3, 5)
ab_major = (8, 10, 0, 1, 3, 5, 7)
ab_dorian = (8, 10, 11, 1, 3, 5, 6)
ab_phrygian = (8, 9, 11, 1, 3, 4, 6)
ab_lydian = (8, 10, 0, 2, 3, 5, 7)
ab_mixolydian = (8, 10, 0, 1, 3, 5, 6)
ab_aeolian = (8, 10, 11, 1, 3, 4, 6)
ab_locrian = (8, 9, 11, 1, 2, 4, 6)
a_major = (9, 11, 1, 2, 4, 6, 8)
a_dorian = (9, 11, 0, 2, 4, 6, 7)
a_phrygian = (9, 10, 0, 2, 4, 5, 7)
a_lydian = (9, 11, 1, 3, 4, 6, 8)
a_mixolydian = (9, 11, 1, 2, 4, 6, 7)
a_aeolian = (9, 11, 0, 2, 4, 5, 7)
a_locrian = (9, 10, 0, 2, 3, 5, 7)
bb_major = (10, 0, 2, 3, 5, 7, 9)
bb_dorian = (10, 0, 1, 3, 5, 7, 8)
bb_phrygian = (10, 11, 1, 3, 5, 6, 8)
bb_lydian = (10, 0, 2, 4, 5, 7, 9)
bb_mixolydian = (10, 0, 2, 3, 5, 7, 8)
bb_aeolian = (10, 0, 1, 3, 5, 6, 8)
bb_locrian = (10, 11, 1, 3, 4, 6, 8)
b_major = (11, 1, 3, 4, 6, 8, 10)
b_dorian = (11, 1, 2, 4, 6, 8, 9)
b_phrygian = (11, 0, 2, 4, 6, 7, 9)
b_lydian = (11, 1, 3, 5, 6, 8, 10)
b_mixolydian = (11, 1, 3, 4, 6, 8, 9)
b_aeolian = (11, 1, 2, 4, 6, 7, 9)
b_locrian = (11, 0, 2, 4, 5, 7, 9)

# lists of chords
maj_and_minor = (c_M, c_m, db_M, db_m, d_M, d_m, eb_M, eb_m, e_M, e_m,
                 f_M, f_m, gb_M, gb_m, g_M, g_m, ab_M, ab_m, a_M, a_m,
                 bb_M, bb_m, b_M, b_m)

maj_and_minor_diatonic_roots = (c_M, c_m, d_M, d_m, e_M, e_m, f_M, f_m,
                                g_M, g_m, a_M, a_m, b_M, b_m)

