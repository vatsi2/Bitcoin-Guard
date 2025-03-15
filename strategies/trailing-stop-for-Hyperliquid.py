def update_trailing_stop(order_id, current_price):
    stop_price = get_stop_price(order_id)
    if current_price > stop_price * 1.02:  # Update the stop when the price rises by 2%
        update_order(order_id, new_stop=current_price * 0.98)
