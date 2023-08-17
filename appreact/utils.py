import sys
import os

# Add the path to the 'proj' directory to sys.path
proj_path = os.path.join(os.path.dirname(__file__), 'XTBApi')
sys.path.append(proj_path)

from XTBApi.api import Client

from datetime import datetime


class Trad:
    def __init__(self) -> None:
        # FIRST INIT THE self.CLIENT
        self.client = Client()
        # THEN LOGIN
        self.client.login("15046335", "BAssetmca18", mode='demo')
        # CHECK IF MARKET IS OPEN FOR EURUSD
        market_is_open = self.client.check_if_market_open("EURUSD")
        # BUY ONE VOLUME (FOR EURUSD THAT CORRESPONDS TO 100000 units)

    
    def get_data(self, number=10000): 
        # self.client.open_trade('buy', "EURUSD", 1)
        # SEE IF ACTUAL GAIN IS ABOVE 100 THEN CLOSE THE TRADE
        data = self.client.get_lastn_candle_history(symbol="EURUSD", timeframe_in_seconds=60, number=number)
        
        for x in data:
            x['date'] =  datetime.fromtimestamp(x['timestamp'])
            x['month'] = x['date'].month
            x['day'] = x['date'].day
            x['hour'] = x['date'].hour
            x['minute'] = x['date'].minute
        return data

    def trad(self):
        
        while True:
            trades = self.client.update_trades() # GET CURRENT TRADES
            trade_ids = [trade_id for trade_id in trades.keys()]
            for trade in trade_ids:
                actual_profit = self.client.get_trade_profit(trade) # CHECK PROFIT
                if actual_profit >= 100:
                    self.client.close_trade(trade) # CLOSE TRADE
            if not trade_ids:
                break #     
        # CLOSE ALL OPEN TRADES
        self.client.close_all_trades()
    
    def logout(self):
        # THEN LOGOUT
        self.client.logout()