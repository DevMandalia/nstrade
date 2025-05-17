"""
Template for creating a new trading strategy.
Copy this file and modify it to implement your strategy.
"""

from src.core.strategy import Strategy
import pandas as pd

class TemplateStrategy(Strategy):
    def __init__(self, initial_capital=10000):
        super().__init__(
            initial_capital=initial_capital,
            author_name="Devaang Mandalia",  # Replace with your name
            strategy_name="20-DM",  # Replace with your strategy name
            description="Testing 20-day momentum"  # Replace with your strategy description
        )
        
        # Add any strategy-specific initialization here
        # For example:
        # self.lookback_period = 20
        # self.threshold = 0.02

    # def process_bar(self, bar):
    #     """
    #     Process each bar of data.
    #     This is where you implement your strategy logic.
        
    #     Args:
    #         bar: Dictionary containing 'time', 'close', and 'volume' data
    #     """
    #     self.current_bar = bar
        
    #     #Add your strategy logic here
       
    #     if self.current_bar['close'] > self.current_bar['close'].shift(-20):
    #         self.last_signal = 'buy'
    #     elif self.current_bar['close'] < self.current_bar['close'].shift(-20):
    #         self.last_signal = 'sell'
    #     else:
    #         self.last_signal = 'hold'

    def get_signal(self):
        """
        Return the current trading signal.
        Must return one of: 'buy', 'sell', 'hold'
        """
        # Add your signal generation logic here
        return 'hold'

    def get_signals(self, df: pd.DataFrame) -> pd.Series:
        """
        Vectorized version of signal generation.
        Override this if you want to implement a more efficient vectorized version.
        """
        #Add your strategy logic here
        df = df.tail(4000)

        twenty_days_back = df['close'].shift(480)
        current = df['close']
        signals = pd.Series('hold', index=df.index)
        signals[current > twenty_days_back] = 'buy'
        signals[current < twenty_days_back] = 'sell'
        signals = signals.shift(1).fillna('hold')
        return signals
       
        # if self.current_bar['close'] > self.current_bar['close'].shift(-20):
        #     self.last_signal = 'buy'
        # elif self.current_bar['close'] < self.current_bar['close'].shift(-20):
        #     self.last_signal = 'sell'
        # else:
        #     self.last_signal = 'hold'


        # return super().get_signals(df) 