def get_top_buyers(orders):
    # Dictionary to aggregate total spending per user
    user_totals = {}
    for order in orders:
        user_id = order['user_id']
        price = order['price']
        if user_id in user_totals:
            user_totals[user_id] += price
        else:
            user_totals[user_id] = price

    # Sort users based on total spending in descending order
    sorted_users = sorted(user_totals.items(), key=lambda x: x[1], reverse=True)
    
    # Extract top 3 user IDs
    top_3 = [user[0] for user in sorted_users[:3]]
    return top_3
