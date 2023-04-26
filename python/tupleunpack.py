list = [('apple',200), ('banana',50), ('orange',100), ('kiwi',50)]
# cost = 0

def max_cost(list):
    cost = 0
    # max_cost_fruit = ''

    for fruit,rate in list:
        if rate>150:
            cost = rate + cost
            # max_cost_fruit = fruit
        else:
            pass

    return(fruit ,rate)

result = max_cost(list)
# fruit, rate= max_cost(list)
print(result)


