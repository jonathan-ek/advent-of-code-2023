from utils import open_input


def main():
    inp = open_input("06").split("\n")
    times = [int(x) for x in inp[0].split(" ")[1:] if x != ""]
    distances = [int(x) for x in inp[1].split(" ")[1:] if x != ""]
    wins = [0 for _ in times]
    product = 1
    for i in range(len(times)):
        for x in range(times[i]):
            if x * (times[i] - x) > distances[i]:
                wins[i] += 1
        product *= wins[i]
    print(wins)
    print(product)



if __name__ == '__main__':
    main()
