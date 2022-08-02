from flask import Flask, request, jsonify

#Create a flask object
app=Flask(__name__)

#create root
@app.route('/XYZ',methods=['GET','POST'])
def test():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify(str(result))
@app.route('/abc/sanowar/',methods=['POST'])
def test1():
    if (request.method=='POST'):
        a=request.json['num3']
        b=request.json['num4']
        result=a+b
        return jsonify(str(result))

@app.route('/abc/sanowar/hossain',methods=['POST'])
def test2():
    if (request.method=='POST'):
        a=request.json['num5']
        b=request.json['num6']
        result=a+b
        return jsonify(str(result))

@app.route('/abc/sanowar/xyz',methods=['POST'])
def test3():
    if (request.method=='POST'):
        a=request.json['sanowar']
        b=request.json['hossain']
        result=a+b
        return jsonify(str(result))

if (__name__)==("__main__"):
    app.run()

