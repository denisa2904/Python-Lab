def compose(notes, moves, start):
    song = [notes[start]]
    for i in range(len(moves)):
        if start + moves[i] < 0:
            song.append(notes[start + moves[i] + len(notes)])
        else:
            song.append(notes[(start + moves[i]) % len(notes)])
        start = (start + moves[i]) % len(notes)
    return song


def main():
    notes = input("Enter the notes: ").split()
    moves = [int(x) for x in input("Enter the moves: ").split()]
    start = int(input("Enter the start position: "))
    print(compose(notes, moves, start))


if __name__ == '__main__':
    main()
