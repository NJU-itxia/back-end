# -*- coding: utf-8 -*-
import json
from pprint import pprint

from eve import Eve
app = Eve()


def post_get_callback(resource, request, payload):
    pprint(json.loads(payload.data))

def post_post_callback(resource, request, payload):
    pprint(json.loads(payload.data))
    pprint(json.loads(request.data))

app.on_post_GET += post_get_callback
app.on_post_POST += post_post_callback

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
