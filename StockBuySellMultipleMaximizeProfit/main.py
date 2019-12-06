# Calculate the max profit from the array of stock prices \
# when you are allowed to make transaction multiple times
array = [40, 55, 30, 75, 300, 310, 325, 315, 250, 20, 280, 275, 400]

class Date(object):
    def __init__(self):
        self.buy = 0
        self.sell = 0

def buy_and_sell_multiple(array):
    i = 0
    transaction = 0
    date_list = []
    max_profit = 0

    while i < len(array) - 1:
        # Finding local minima
        while i < len(array) - 1 and array[i+1] <= array[i]:
            i += 1

        date = Date()
        date.buy = i

        i += 1
        # Finding local maxima
        while i < len(array) and array[i-1] >= array[i]:
            i += 1

        date.sell = i
        date_list.append(date)
        transaction += 1

    for i in range(transaction):
        local_profit = array[date_list[i].sell] - array[date_list[i].buy]
        max_profit += local_profit
    return max_profit



# Validation
p = buy_and_sell_multiple(array)
print("Total profit: " + str(p))
