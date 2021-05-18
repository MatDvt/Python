def loading_bar(num):
    # create an empty bar(list) to hold just dots
    bar = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    if num == 0:
        return bar
    num = num // 10

    for index in range(num):
        bar[index] = '%'  # substitute the elements of the list with %

    return bar


number = int(input())
bar_result = loading_bar(number)

if bar_result.count('%') == 10:
    print("100% Complete!")
    print(f"[{''.join(bar_result)}]")
else:
    print(f"{number}% [{''.join(bar_result)}]")
    print("Still loading...")
