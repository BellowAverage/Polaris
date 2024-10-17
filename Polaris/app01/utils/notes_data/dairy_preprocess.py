import pandas as pd
from database_operations import polaris_db


# data = pd.read_csv(r'Polaris\app01\utils\diary_info_20w_to_1000.csv')
# data = data.dropna()
# data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# data.to_csv("preprocessed_diary_info_19.6w_to_17.6w.csv", index=False, encoding='utf-8-sig')


# data = pd.read_csv(r'Polaris\app01\utils\preprocessed_diary_info_19.6w_to_17.6w.csv')
# data["User"].drop_duplicates().to_csv(r'Polaris\app01\utils\user_list.csv', index=False, encoding='utf-8-sig')

data = pd.read_csv(r'Polaris\app01\utils\preprocessed_diary_info_19.6w_to_17.6w.csv')
data['uid'] = data['User'].apply(lambda x: polaris_db(f"SELECT uid FROM users WHERE user_name='{x}';")[0][0])
data.to_csv("preprocessed_diary_info.csv", index=False, encoding='utf-8-sig')