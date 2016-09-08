from morseconverter.morse import Morse


def main():
    m = Morse()
    m.convert(real_time=True)

if __name__ == '__main__':
    main()
