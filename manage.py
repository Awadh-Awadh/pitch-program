from app import db, create_app
from flask_migrate import Migrate
from app.models import User
from flask_migrate import Migrate


app = create_app('production')

#create a migration instance
migrate = Migrate(app,db)

# creating a shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User = User)