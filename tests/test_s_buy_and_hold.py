def init(context):
    context.s1 = "000001.XSHE"


def before_trading(context):
    pass


def handle_bar(context, bar_dict):
    order_shares(context.s1, 1000)


def after_trading(context):
    pass

__config__ = {
    "base": {
        "strategy_type": "stock",
        "start_date": "2015-01-09",
        "end_date": "2016-01-12",
        "frequency": "1d",
        "matching_type": "current_bar",
        "stock_starting_cash": 1000000,
        "benchmark": "000300.XSHG",
    },
    "extra": {
        "log_level": "error",
    },
    "mod": {
        "sys_progress": {
            "enabled": True,
            "priority": 400,
        },
        "sys_analyser": {
            "plot": False
        },
    },
}