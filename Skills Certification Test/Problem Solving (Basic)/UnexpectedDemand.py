def filledOrders(order, k):
    total = 0
    for count, value in enumerate(sorted(order)):
        if total + value <= k:
            total += value  # total stays <= k
        else:
            return count  # provides the count
    else:
        return len(order)  # was able to place all orders


if __name__ == '__main__':

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)
    print(result)
