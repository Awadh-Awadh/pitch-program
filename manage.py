from app import db, create_app


app = create_app('development')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)