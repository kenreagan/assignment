from typing import Iterable, Optional, TypeVar


T = TypeVar('T', str, int, float)


sample_transactions = [
        ("B", 100,1104,"VTI",1),
        ("B", 200,36,"ONEQ",3),
        ("B", 50, 1223, "VTI", 5),
        ("S", 150,1240,"VTI",9),
        ("B", 100, 229, "IWRD", 10),
        ("S", 200, 32, "ONEQ", 11),
        ("S", 100, 210, "IWRD",12)
];

class Transaction:
    def __init__(self, transactions: Iterable):
        self.transactions = transactions
        self.action: str = "Bought" if transactions[0] == "B" else "Sold"
        self.units: int = transactions[1]
        self.price: float = transactions[2]
        self.stock: str = transactions[3]
        self.day: int = transactions[4]

    def __repr__(self):
        return f"({self.transactions[0]}, {self.units}, {self.price}, {self.stock}, {self.day})"

    def to_string(self):
        return f"{self.action} {self.units} units of {self.stock} for {self.price} each on day {self.day}"

    def __contains__(self, item: str) -> bool:
        return self.stock == item

def transaction_to_string(action, units, price, stock, day):
    transaction = Transaction((action, units, price, stock, day))
    return transaction.to_string()


def trade_report_list(transactions: Iterable[Iterable[Optional[T]]]):
    return [item.to_string() for item in list(map(create_transaction, transactions))]


def get_trades(stock: str, test_log):
    transactions = list(map(create_transaction, test_log))
    return list(filter(lambda x: x.stock == stock, transactions))


def create_transaction(transaction) -> Transaction:
    return Transaction(transaction)


def stock_test(stock: str, transaction_log: Iterable) -> bool:
    transaction = Transaction(transaction_log)
    return stock in transaction

def trade_report(stock: str, test_log: Iterable[Iterable[Optional[T]]]) -> str:
    transactions = get_trades(stock, test_log)
    for items in transactions:
        print(items.to_string())


def update_money(transaction: Iterable[Optional[T]], value):
    transaction = Transaction(transaction)
    if transaction.action == "Bought":
        loss = transaction.units * price
        value -= loss
    elif transaction.action == "Sold":
        profit = transaction.units * price
        value += profit
    return value

def profit(transaction_log, stock) -> int:
    profit = sum([item.unit * item.price for item in [filter(lambda x: x.action == 'Bought', get_trades(transaction_log, log))]])
    loss = sum(item.unit * item.price for item in [filter(lambda x: x.action == 'Sold', get_trades(transaction_log, log))])
    return profit - loss


def profit_report(reports: Iterable[str], transaction_log):
    for items in reports:
        print(f"{items}: {profit(transaction_log, items)}")

price_database = [
        ("VTI", [1689, 1785, 1772, 1765, 1739, 1725, 1615, 1683, 1655, 1725, 1703, 1726, 1725,
            1742, 1707, 1688, 1697, 1688, 1675]),
        ("ONEQ", [201, 203, 199, 199, 193, 189, 189, 183, 185, 190, 186, 182, 186, 182, 182,
            186, 183, 179, 178]),
        ("IWRD", [207, 211, 213, 221, 221, 222, 221, 218, 226, 234, 229, 229, 228, 222, 218,
            223, 222, 218, 214])
]

def complex_profit_report(transaction_log: str, price) -> str:
    filtered_res = list(filter(lambda x: x[0] == transaction_log, price))
    return f"{transaction_log}: {sum(filtered_res[0][1])}"


if __name__ == '__main__':
    print(complex_profit_report("ONEQ", price_database))
