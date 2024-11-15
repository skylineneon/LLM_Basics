import time

class Order:
    def __init__(self, order_id, price, quantity, side, timestamp):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.side = side  # 'buy' or 'sell'
        self.timestamp = timestamp  # 订单提交的时间戳

class MatchingEngine:
    def __init__(self):
        self.buy_orders = []  # 按价格从高到低，时间戳从早到晚排序
        self.sell_orders = []  # 按价格从低到高，时间戳从早到晚排序

    def insert_order(self, order):
        if order.side == 'buy':
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda x: (-x.price, x.timestamp))
        elif order.side == 'sell':
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda x: (x.price, x.timestamp))

        self.match_orders()

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            best_buy_order = self.buy_orders[0]
            best_sell_order = self.sell_orders[0]

            if best_buy_order.price >= best_sell_order.price:
                # 执行交易
                trade_quantity = min(best_buy_order.quantity, best_sell_order.quantity)
                print(f"Trade executed: {trade_quantity} at {best_sell_order.price} (Order IDs: {best_buy_order.order_id}, {best_sell_order.order_id})")

                # 更新订单数量
                best_buy_order.quantity -= trade_quantity
                best_sell_order.quantity -= trade_quantity

                # 如果订单完全成交，则从列表中移除
                if best_buy_order.quantity == 0:
                    self.buy_orders.pop(0)
                if best_sell_order.quantity == 0:
                    self.sell_orders.pop(0)
            else:
                break

# 示例
engine = MatchingEngine()
engine.insert_order(Order(1, 100, 10, 'buy', time.time()))
time.sleep(1)  # 模拟等待一秒钟
engine.insert_order(Order(2, 100, 10, 'buy', time.time()))  # 两个买单价格相同，第二个订单时间晚
engine.insert_order(Order(3, 95, 10, 'sell', time.time()))
engine.insert_order(Order(4, 100, 10, 'sell', time.time()))
