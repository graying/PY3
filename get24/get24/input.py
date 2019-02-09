from flask import (Blueprint, render_template, request
                   )

from . import cal_24

# from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('input', __name__, url_prefix='/input')


@bp.route('/', methods=("GET", "POST"))
def input():
    return render_template("/index.html")


@bp.route('/calc', methods=("GET", "POST"))
def calc():
    if request.method == "POST":
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        n3 = int(request.form['n3'])
        n4 = int(request.form['n4'])
    result = cal_24.cal24(n1, n2, n3, n4)
    nums = [n1, n2, n3, n4]
    if len(result) > 0:
        for res in result:
            print(res)
    else:
        result = ["no result"]
    return render_template("/calc.html", result=result, nums=nums)
