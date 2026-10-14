
from typing import List


def ways_to_make_change(total: int) -> int:
    cache = {}
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    return ways_to_make_change_helper(total, coins, cache)


def ways_to_make_change_helper(
    total: int, coins: List[int], cache: dict
) -> int:
    if total == 0:
        return 1

    if len(coins) == 0:
        return 0

    key = (total, tuple(coins))

    if key in cache:
        return cache[key]

    ways = 0

    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1

        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin

            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(
                    total - total_from_coins,
                    coins[coin_index + 1:],
                    cache,
                )

            count_of_coin += 1

    cache[key] = ways
    return ways
