# -*- coding: utf-8 -*-
from __future__ import print_function
import termios
import fcntl
import sys
import os

from morseconverter.error import UnknowLetter
from morseconverter.alphabet_mapping import mapping
from morseconverter import pyver
from morseconverter import sys_input


class Morse:
    def __init__(self, alphabet='latin'):
        self.alphabet = alphabet

    def convert(self, real_time=False, text=False):
        """
        Default action is real_time is False
        If real_time is True, calling real_time_converter function.
        If real_time is False, calling text_converter function.

        @param real_time: Default is False. Only morseconverter console script
                          use True.
        @param text: string
        """
        if real_time:
            self.real_time_converter()

        if text is not False:
            morse = self.text_converter(str(text))
            return morse

    def real_time_converter(self):
        """
        Real time printing letter to morse alphabet converter.
        termios details: http://man7.org/linux/man-pages/man3/termios.3.html
        fcntl details: http://man7.org/linux/man-pages/man2/fcntl.2.html
        """
        fd = sys.stdin.fileno()
        old_term = termios.tcgetattr(fd)
        new_attr = termios.tcgetattr(fd)
        old_term[3] = ~termios.ICANON & ~termios.IEXTEN
        new_attr[3] = new_attr[3] & ~termios.ICANON & ~termios.ECHO

        old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, old_flags | os.O_NONBLOCK)

        try:
            while True:
                try:
                    k_input = sys_input.read(1)
                    # if Back Space
                    if '\x7f' == k_input:
                        print('\nBack Space not supported. Starting with new line.')
                        continue
                    # if Ctrl-C
                    if '\x03' == k_input:
                        print('\nBye!')
                        # turning off output flushing
                        os._exit(0)
                    if '\r' == k_input:
                        print('\r')
                    if len(k_input) != 0:
                        k_input = k_input.lower()
                        if ' ' == k_input:
                            morse_map = ' '
                        # if press enter
                        elif '\r' == k_input:
                            morse_map = '\n'
                        else:
                            morse_map = self.alphabet_map(self.alphabet, k_input)
                        if pyver:
                            print(morse_map, end='', flush=True)
                        else:
                            print(morse_map, end='')
                except IOError:
                    pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)
            fcntl.fcntl(fd, fcntl.F_SETFL, old_flags)

    def text_converter(self, text):
        """
        Convert text to morse alphabet. 
        It can be letter, word or sentences

        @param return: str
        """
        text_to_morse = ''
        for letter in text:
            letter = letter.lower()
            if ' ' == letter:
                text_to_morse += ' '
            else:
                morse_map = self.alphabet_map(self.alphabet, letter)
                text_to_morse += morse_map
        
        return text_to_morse

    def alphabet_map(self, alphabet, letter):
        if pyver is False:
            letter = letter.encode('utf-8')
        try:
            return mapping[alphabet][letter]
        except KeyError as e:
            raise UnknowLetter('Unknown Alphabet or Word: %s' % e)
            
