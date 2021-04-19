import configparser
import redis
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
r = redis.Redis(host=(config['REDIS']['HOST']), password=(config['REDIS']['PASSWORD']), port=(config['REDIS']['REDISPORT']))
db_keys = r.keys(pattern="*")

weight = r.get("@magicalxzc").decode("UTF-8")
print(weight)
for single in db_keys:
    chat_id = r.get(single).decode("UTF-8")
    print(single.decode("UTF-8"), ": ", chat_id)