from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv('./assets/ks-projects-201801.csv')
df = pd.DataFrame(csv_data).head(10000)

del df['ID']
df['usd_pledged'] = df['usd pledged']
del df['usd pledged']

df['name'] = df['name'].fillna('unknown')
df['category'] = df['category'].fillna('unknown')
df['main_category'] = df['main_category'].fillna('unknown')
df['currency'] = df['currency'].fillna('unknown')
df['goal'] = df['goal'].fillna(0.0)
df['pledged'] = df['pledged'].fillna(0.0)
df['state'] = df['state'].fillna('unknown')
df['backers'] = df['backers'].fillna(0.0)
df['country'] = df['country'].fillna('unknown')
df['usd_pledged'] = df['usd_pledged'].fillna(0.0)
df['usd_pledged_real'] = df['usd_pledged_real'].fillna(0.0)
df['usd_goal_real'] = df['usd_goal_real'].fillna(0.0)

db_protocol = 'postgresql'
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')


engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))


df.to_sql('project_data_project', engine, if_exists='append', index=False)
