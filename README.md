# eve api

## source
>`GET  /clients`  
> 得到所有的客户的`phone_number`(只显示此信息),据此进一步访问.


>`GET  /clients/<phone_number>`  
>得到用户的详细信息.
>>如果是`HTTP/1.0 404 NOT FOUND` 找不到用户   
>>
>>进入到新建表单页面,将信息打包成json,然后`POST  /clients/<phone_number>`
>  
>用户只能查看信息和新建信息.   


>`GET /orders`
>得到所有订单的详细信息，处理者`handled_by`和用户`applicant`只显示`_id`(在mongodb中的键值)


>`POST /orders`  
>存储表单，用前面的json来存储.

>`GET /servers`  
>`HTTP/1.0 401 UNAUTHORIZED` 需要验证
>
>`GET /servers username:password`  
>>如果是`admin`, 拥有GET,PATCH,DELETE,PUT所有item的权利  
>>如果是`itxia`, 则只能在自己的路由下即`/servers/<username>`,行使GET,PATCH,DELETE,PUT自己的item  
（路由最深的端点所对应的资源为item）

```json
"schemes": [
    "http"
  ],
  "parameters": {
    "client__id": {
      "in": "path",
      "name": "clientId",
      "required": true,
      "description": "",
      "type": "string",
      "format": "objectid"
    },
    "order__id": {
      "in": "path",
      "name": "orderId",
      "required": true,
      "description": "",
      "type": "string",
      "format": "objectid"
    },
    "server__id": {
      "in": "path",
      "name": "serverId",
      "required": true,
      "description": "",
      "type": "string",
      "format": "objectid"
    }
  },
  "produces": [
    "application/xml",
    "application/json"
  ],
  "tags": [
    {
      "name": "client"
    },
    {
      "name": "order"
    },
    {
      "name": "server"
    }
  ],
  "host": "127.0.0.1:5000",
  "definitions": {
    "client": {
      "required": [
        "phone_number",
        "name",
        "campus"
      ],
      "type": "object",
      "properties": {
        "phone_number": {
          "type": "string"
        },
        "_id": {
          "$ref": "#/definitions/client__id"
        },
        "name": {
          "minLength": 1,
          "type": "string",
          "maxLength": 15
        },
        "campus": {
          "enum": [
            "gulou",
            "xianlin"
          ],
          "type": "string"
        },
        "lilybbs_id": {
          "type": "string"
        }
      }
    },
    "order": {
      "required": [
        "description",
        "requested_by",
        "machine_model",
        "OS"
      ],
      "type": "object",
      "properties": {
        "status": {
          "default": "waiting",
          "enum": [
            "waiting",
            "working",
            "done"
          ],
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "handled_by": {
          "$ref": "#/definitions/server__id"
        },
        "comments": {
          "items": {
            "type": "object",
            "properties": {
              "username": {
                "type": "string"
              },
              "content": {
                "type": "string"
              },
              "created_at": {
                "default": "Thu, 27 Oct 2016 15:41:30 GMT",
                "type": "string",
                "format": "date-time"
              }
            }
          },
          "type": "array"
        },
        "requested_by": {
          "$ref": "#/definitions/client__id"
        },
        "machine_model": {
          "type": "string"
        },
        "_id": {
          "type": "string",
          "format": "objectid"
        },
        "OS": {
          "type": "string"
        }
      }
    },
    "server": {
      "required": [
        "username",
        "password",
        "campus",
        "role",
        "email"
      ],
      "type": "object",
      "properties": {
        "username": {
          "type": "string"
        },
        "_id": {
          "$ref": "#/definitions/server__id"
        },
        "campus": {
          "enum": [
            "gulou",
            "xianlin"
          ],
          "type": "string"
        },
        "role": {
          "enum": [
            "itxia",
            "admin"
          ],
          "type": "string"
        },
        "password": {
          "type": "string"
        },
        "email": {
          "type": "string"
        }
      }
    },
    "client__id": {
      "type": "string",
      "format": "objectid"
    },
    "server__id": {
      "type": "string",
      "format": "objectid"
    }
  },
  "consumes": [
    "application/json"
  ]
}
```
