from matplotlib import pyplot as plt


def draw(title, series_number, values_a_star, values_ldfs):
    test = [x+1 for x in range(series_number)]
    plt.figure()
    plt.title(title)
    plt.plot(test, values_a_star, 'o-r')
    plt.plot(test, values_ldfs, 'd-b')
    plt.show()

def print_table(series_number, values_a_star, values_ldfs, average_a_star, average_ldfs):
    print("{:<8} {:<10} {:<10}".format('TestCase', 'BFS', 'AStar'))
    for i in range(series_number):
        print("{:<8} {:<10} {:<10}".format(i+1, values_ldfs[i], values_a_star[i]))
    print("{:<8} {:<10} {:<10}".format("Avg", average_ldfs, average_a_star))
    print()
