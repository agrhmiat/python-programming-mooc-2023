# Write your solution here

def longest_series_of_neighbours(my_list: list) -> int:
    i = 0
    neighbours = 0
    max_neighbours = 0
    neighbour_found = False
    for i in range(len(my_list)-1):
        if abs(my_list[i]-my_list[i+1]) == 1:
            neighbour_found = True
            neighbours += 1
            if neighbours > max_neighbours:
                max_neighbours = neighbours
        else:
            neighbours = 0
    return max_neighbours + 1

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
