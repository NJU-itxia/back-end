import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.hmset('name',{'if':'ok','if2':'f'})
print r.hgetall('name')

r.hmset('name',{'of':'ff'})
print r.hgetall('name')
