
def ft_filter(function_to_apply, list_of_inputs):
    """
    Return an iterator yielding those items of iterablefor which function(item)
    is true. If function is None, return the items that are true.
    """
    if function_to_apply is None:
        return (item for item in list_of_inputs if item)
    return (item for item in list_of_inputs if function_to_apply(item))


def main():
    """
    Main function to test the ft_filter function.
    """

    res1 = ft_filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4])
    res2 = filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4])

    for x in res1:
        print(x)
    for x in res2:
        print(x)


if __name__ == "__main__":
    main()
