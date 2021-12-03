import time

from parser import parse


def main():
    start = time.time()
    data = parse()
    end = time.time()

    print(f'Found total of {data["stats"]["total_sentences"]} sentences.'
          f' With total of {data["stats"]["total_chars"]} character in the file.')
    print(f'Total execution time: {end - start}')


if __name__ == '__main__':
    main()
