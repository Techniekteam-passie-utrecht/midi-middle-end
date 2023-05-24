"""LCD:
sysex (hex) F0 00 20 32 dd 4C nn cc c1 .. c14 F7
    dd: device id (X-Touch: 0x14, X-Touch-Ext: 0x15)
    nn: LCD number 0..7
    cc: bits 0-2: backlight color (black, red, green, yellow, blue, magenta, cyan, white)
    cc: bit 4: invert upper half of LCD
    cc: bit 5: invert lower half of LCD
    c1..c14: ascii characters (1..7: upper half, 8..14: lower half)
so for:
    'hello
     world'
F0 00 20 32 dd 4C nn cc a1 a2 a3 a4 a5 a6 a7 b1 b2 b3 b4 b5 b6 b7 F7
F0 00 20 32 14 4C 00 20 00 48 65 6c 6c 6f 00 00 57 6f 72 6c 64 00 F7
                        _  H  e  l  l  o  _  _  W  o  r  l  d  _
"""

"""Segment Displays:
sysex (hex) F0 00 20 32 dd 37 s1 .. s12 d1 d2 F7
    dd: device id (X-Touch: 0x14, X-Touch-Ext: 0x15)
    s1..s12: segment data (bit 0: segment a, .. bit 6: segment g)
    d1: dots for displays 1..7 (bit 0: display 1, .. bit 6: display 7)
    d2: dots for displays 8..12 (bit 0: display 8, .. bit 4: display 12)

    0bABCDEFG0
     AA
    F  B
    F  B
     GG
    E  C
    E  C
     DD

so for 012345678901 with alternating dots on the displays:
F0 00 20 32 dd 37 s1 .. s12 d1 d2 F7
F0 00 20 32 14 47 7E 0C B6 9E CC DA FA 0E FE DE 7E 0C AA A8 F7
                  0  1  2  3  4  5  6  7  8  9  0  1  .  .
"""
# print(hex(0b01111110))
# print(hex(0b00001100))
# print(hex(0b10110110))
# print(hex(0b10011110))
# print(hex(0b11001100))
# print(hex(0b11011010))
# print(hex(0b11111010))
# print(hex(0b00001110))
# print(hex(0b11111110))
# print(hex(0b11011110))
# print(hex(0b10101000))

import rtmidi


def main():
    midi_in  = rtmidi.MidiIn()
    midi_out = rtmidi.MidiOut()

    print("MIDI input ports:")
    ports_in = midi_in.get_ports()
    for i, name in enumerate(ports_in):
        print(f"{i + 1}. {name}")

    print("MIDI output ports:")
    ports_out = midi_out.get_ports()
    for i, name in enumerate(ports_out):
        print(f"{i + 1}. {name}")


if __name__ == '__main__':
    main()