# -*- coding: utf-8 -*-
from eve import Eve
app = Eve()


def post_get_callback(resource, request, payload):
    print payload.data

def post_post_callback(resource, request, payload):
    print payload.data
    print request.data

app.on_post_GET += post_get_callback
app.on_post_POST += post_post_callback

if __name__ == '__main__':
    app.run(debug=True)
