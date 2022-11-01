from flask import Blueprint, request, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    print(request.headers)
    print(request.args.get('name'))
    return render_template('base.html')
    
@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/create_event')
def create_event():
    return render_template('create_event.html')