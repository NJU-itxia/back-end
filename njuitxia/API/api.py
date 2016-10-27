import bcrypt
from eve import Eve
from eve_swagger import swagger, add_documentation
from eve.auth import BasicAuth


class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        servers = app.data.driver.db['servers']
        server = servers.find_one({'username': username})
        # set 'auth_field' value to the server's username
        if server and 'username' in server:
            if server['role'] == 'admin':
                print 'admin log'
                return server['password'] == password
            else:
                print 'itxia log'
                self.set_request_auth_value(server['username'])
        return server and server['password'] == password

app = Eve(auth=BCryptAuth)
app.register_blueprint(swagger)

app.config['SWAGGER_INFO'] = {
    'title': 'itxia-backend',
    'version': '1.0',
    'description': 'an API description',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'chenhao',
        'url': 'https://github.com/imphoney'
    },
    'license': {
        'name': 'BSD',
        'url': 'https://github.com/nicolaiarocci/eve-swagger/blob/master/LICENSE',
    }
}

app.config['SWAGGER_HOST'] = '127.0.0.1:5000'


if __name__ == '__main__':  
    app.run()
