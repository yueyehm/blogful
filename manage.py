from os import environ
from flask.ext.script import Manager

from blog import app
from blog.database import session, Entry

manager = Manager(app)

@manager.command
def run():
    port = int(environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def seed():
    content = """test content"""
    
    for i in range(25):
        entry = Entry(
            title = "Test Entry # {}".format(i),
            content = content
            )
        session.add(entry)
    session.commit()

if __name__ == "__main__":
    manager.run()