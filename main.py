import pandas as pd
from datetime import datetime
import json
import os
from output_strategies.console_output import ConsoleOutput
from output_strategies.kafka_output import KafkaOutput
from output_strategies.redis_output import RedisOutput

with open('config.json') as f:
    config = json.load(f)

xlsx_file_path = os.path.join(os.path.dirname(__file__), 'sample_data_crimes.xlsx')

df = pd.read_excel(xlsx_file_path)
data = df[:50].copy()

for col in data.columns:
    data[col] = data[col].apply(lambda x: x.isoformat() if isinstance(x, (pd.Timestamp, datetime)) else x)

data = data.to_dict(orient='records')

strategy_map = {
    "console": ConsoleOutput,
    "kafka": KafkaOutput,
    "redis": RedisOutput
}
strategy_class = strategy_map.get(config["output_strategy"], ConsoleOutput)
selected_strategy = strategy_class()

selected_strategy.write(data)
