# coding:utf-8
from app import create_app, db
from app.model import Form, Server, Client
from flask_script import Manager, Shell, Command
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, Server=Server, Client=Client, Form=Form)
    
@manager.command    
def testdb():
    Client.generate_fake(10) #构造虚拟用户
    Server.generate_fake(10)
    Form.generate_fake(10) #构造虚拟订单
#    client_1 = Client(phone_number='15850551103', password='123456', email='221410232@qq.com');
#    client_2 = Client(phone_number='15850123187', password='234786', email='2364726346@qq.com');
#    client_3 = Client(phone_number='15850123905', password='234786', email='2err4726346@qq.com');

#    form_1 = Form(campus='gulou', machine_model='dell', OS='win8', description='jkjslafjsl');
#    form_2 = Form(campus='gulou', machine_model='dell', OS='win8', description='jksjfklsa');
#    form_3 = Form(campus='gulou', machine_model='mac', OS='win8', description='jksdfsdgfsfklsa');

#    client_1.post_forms = [form_1, form_2];
#    client_3.post_forms = [form_1];

#    db.session.add_all([client_1, client_2, client_3]);
#    db.session.commit();

#    client = Client.query.filter_by(phone_number=15850123187).first();
#    client.post_forms = [form_3];
#    db.session.add(client);
#    db.session.commit();

#    client = Client.query.filter_by(phone_number=15850123187).first()
#    db.session.delete(client)
#    db.session.commit()

#    form = Form.query.filter_by(id=2).first()
#    form.post_client = client
#    db.session.add(form)
#    db.session.commit()
    
                   
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    manager.run()
