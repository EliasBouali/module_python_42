def ft_count_harvest_recursive() :
    days = input("Days until harvest: ")
    count = 0
    def ft_count(count, days) :
        if count < days :
            count += 1
            print(f"Day {count}")
            ft_count(count, days)

    ft_count(count, int(days))
    print("Harvest time!")
