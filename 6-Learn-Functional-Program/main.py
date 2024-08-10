def word_count_aggregator():
    count = 0

    def sum_values(document):
        nonlocal count
        words = document.split()
        count += len(words)
        return count

    return sum_values