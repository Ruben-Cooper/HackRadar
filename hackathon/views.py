from logging import PlaceHolder
from flask import Blueprint, request, render_template
from .forms import RegisterForm


bp = Blueprint('main', __name__)



@bp.route('/')
def index():
    print(request.headers)
    print(request.args.get('name'))
    return render_template('base.html')
    
@bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')\

@bp.route('/create_event')
def create_event():
    return render_template('create_event.html')