from flask import Flask, request
import redis
redis_net_id = redis.Redis()
redis_app_id = redis.Redis(db=1)
app = Flask(__name__)


@app.route('/<net_id>/<app_id>',methods = ['GET', 'DELETE'])
def get_net(net_id, app_id):
   if request.method == 'GET':
      return 'net id = ' +  redis_net_id.get(net_id).decode("utf-8") + ' , app_id  = ' + redis_app_id.get(app_id).decode("utf-8")

   if request.method == 'DELETE':
      redis_net_id.delete(net_id)
      redis_app_id.delete(app_id)
      return 'deleted ' + net_id + ':' + app_id
   
  
if __name__ == '__main__':
   app.run()