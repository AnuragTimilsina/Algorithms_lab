def brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items):
    # Initial conditions:
    if no_of_items ==0 or bag_size==0:
        return 0
    
    # If item_weight is higher than bag capacity then it is not included
    if(item_weight[no_of_items-1] > bag_size):
        return brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items)
    
    # Return either Nth item being included or not
    else:
        return max(item_profit[no_of_items-1] + brute_force_knap_sack(bag_size-item_weight[no_of_items-1], item_weight, item_profit, no_of_items-1),
                   brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items-1))


if __name__ == "__main__":
    item_profit = [60, 100, 20]
    item_weight = [10, 20, 30]
    bag_size = 50
    no_of_items = len(item_profit)
    print(brute_force_knap_sack(bag_size, item_weight, item_profit, no_of_items))


    
    