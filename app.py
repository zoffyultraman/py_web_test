from flask import Flask
from flask import request
from flask import render_template
import os
import re
import string
app = Flask(__name__)



@app.route('/test',methods=['POST'])
def test():
    ip1=request.form.get('ip1')
#   ip2 = request.form.get('ip2')
#    ip3= request.form.get('ip3')
#    ip4 = request.form.get('ip4')
#    ip_add=ip1+'.'+ip2+'.'+ip3+'.'+ip4
    output = os.popen('ping ' + ip1)
    t=output.read()
    q=(re.search('平均 = ',t))
    s=str(q)
    o=s[24:27]
    y=s[29:32]
    oo=int(o)
    yy=int(y)+3
    print(t)
    return render_template('index.html',t=t[oo:yy])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
