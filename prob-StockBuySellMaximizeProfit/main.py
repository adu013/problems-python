# Calculate the max profit from the array of stock prices \
# when you are allowed to make transaction only once
array = [40, 55, 30, 75, 300, 310, 325, 315, 250, 20, 280, 275, 400]

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_method_1(array):
    """
    method: brute force
    """
    buy_price = 0
    sell_price = 0
    max_profit = 0
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[j] - array [i] > max_profit:
                buy_price = array[i]
                sell_price = array[j]
                max_profit = sell_price - buy_price
    return buy_price, sell_price, max_profit


def buy_and_sell_method_2(array):
    """
    """
    max_profit_ = 0
    min_price = array[0]

    for price in array:
        min_price = min(min_price, price)
        local_profit = price - min_price
        max_profit_ = max(max_profit_, local_profit)
    return max_profit_


# Validating
# buy, sell, max = buy_and_sell_method_1(array)
# print("Buy @ " + str(buy) + " & Sell @ " + str(sell))
# print("Max profit: " + str(max))

profit = buy_and_sell_method_2(array)
print(str(profit))
