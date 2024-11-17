from typing import List


def count_min_numbers_of_platforms(weights: List[int], limit: int) -> int:
    """Считает минимальное количество платформ, для перевозки роботов."""
    sorted_weights = sorted(weights)
    lightest = 0
    heaviest = len(sorted_weights) - 1
    platforms = 0

    while lightest <= heaviest:
        if sorted_weights[lightest] + sorted_weights[heaviest] <= limit:
            lightest += 1
        heaviest -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":

    weights = list(map(int, input().split()))
    limit = int(input())

    result = count_min_numbers_of_platforms(weights, limit)
    print(result)

