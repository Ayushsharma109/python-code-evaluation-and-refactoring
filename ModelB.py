def get_top_buyers(orders):
    # Find all unique users
    unique_users = []
    for order in orders:
        if order['user_id'] not in unique_users:
            unique_users.append(order['user_id'])
            
    # Calculate total spent for each unique user
    user_spending = []
    for user_id in unique_users:
        total = 0
        for order in orders:
            if order['user_id'] == user_id:
                total += order['price']
        user_spending.append((user_id, total))
        
    # Sort and pick top 3
    for i in range(len(user_spending)):
        for j in range(0, len(user_spending) - i - 1):
            if user_spending[j][1] < user_spending[j + 1][1]:
                user_spending[j], user_spending[j + 1] = user_spending[j + 1], user_spending[j]
                
    return [user[0] for user in user_spending[:3]]
