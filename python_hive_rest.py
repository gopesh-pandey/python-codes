from pyhive import hive
from flask import Flask, jsonify
from flask import Flask, request
from flask_restful import Resource, Api

#=======================================================================================================================
#Establish connection with hive using Pyhive
#=======================================================================================================================

app = Flask(__name__)
db = hive.Connection(host="hn0-elc-sp.wchiduhu4wpurn1b4rq1rq1vtc.cx.internal.cloudapp.net",port=10000,database="default")
cursor = db.cursor()

#=======================================================================================================================
#Product Rest Endpoints Definition
#=======================================================================================================================

@app.route('/products', methods = ['GET'])

def products():
    if 'benefit' in request.args:
            getbenefit = request.args['benefit']
            splitbenefit = getbenefit.split(",")
            sql_query = '''select * from dev.products_sample where benefit in ('%s')''' % ("','".join(splitbenefit))
            cursor.execute(sql_query)
            content = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row)) for row in cursor.fetchall()]
            return jsonify({'myCollection': content})

    elif 'id' in request.args:
            getid = request.args['id']
            splitid = getid.split(",")
            sql_query = '''select * from dev.products_sample where product_id  in ('%s')''' % ("','".join(splitid))
            print(sql_query)
            cursor.execute(sql_query)
            content= [dict((cursor.description[i][0], value)
                        for i, value in enumerate(row)) for row in cursor.fetchall()]
            return jsonify({'myCollection' : content})

    elif 'brand' in request.args:
            getbrand = request.args['brand']
            splitbrand = getbrand.split(",")
            sql_query = '''select * from dev.products_sample where brand  in ('%s')''' % ("','".join(splitbrand))
            print(sql_query)
            cursor.execute(sql_query)
            content = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row)) for row in cursor.fetchall()]
            return jsonify({'myCollection': content})

    elif 'form' in request.args:
            getform = request.args['form']
            splitform = getform.split(",")
            sql_query = '''select * from dev.products_sample where product_form  in ('%s')''' % ("','".join(splitform))
            print(sql_query)
            cursor.execute(sql_query) 
            content = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row)) for row in cursor.fetchall()]
            return jsonify({'myCollection': content})

    elif 'subcategory' in request.args:
        getsubcategory= request.args['subcategory']
        splitsubcategory= getsubcategory.split(",")
        sql_query = '''select * from dev.products_sample where solution_type in ('%s')''' % ("','".join(splitsubcategory))
        print(sql_query)
        cursor.execute(sql_query)
        content = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]
        return jsonify({'myCollection': content})
    elif 'franchise' in request.args:
        getfranchise= request.args['franchise']
        splitfranchise = getfranchise.split(",")
        sql_query = '''select * from dev.products_sample where franchise in ('%s')''' % ("','".join(splitfranchise))
        print(sql_query)
        cursor.execute(sql_query)
        content = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        return jsonify({'myCollection': content})
    else:
        cursor.execute("select distinct productname from dev.products_sample")
        content = [dict((cursor.description[i][0], value)
                        for i, value in enumerate(row)) for row in cursor.fetchall()]
        return jsonify({'myCollection' : content})
#=======================================================================================================================
#NPD Rest Endpoints Definition
#=======================================================================================================================

@app.route('/npd', methods = ['GET'])
def npdsales():
    if 'geo' in request.args and 'show' in request.args and 'show_depth' in request.args:
        geo = request.args['geo']
        show = request.args['show']
        show_depth = request.args['show_depth']
        cursor.execute("select * from dev.products_sample where geo='%s'" % geo + " and show='%s'" % show + " and show_depth='%s'" % show_depth)
        content = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
        return jsonify({'myCollection': content})

    elif 'product' in request.args and 'show' in request.args and 'show_depth' in request.args:
       product = request.args['product']
       show = request.args['show']
       show_depth = request.args['show_depth']
       cursor.execute("select * from dev.products_sample where product='%s'" % product + " and show='%s'" % show + " and show_depth='%s'" % show_depth)
       content = [dict((cursor.description[i][0], value)
          for i, value in enumerate(row)) for row in cursor.fetchall()]
       return jsonify({'myCollection': content})

    elif 'month' in request.args and 'show' in request.args and 'show_depth' in request.args:
       month = request.args['month']
       show = request.args['show']
       show_depth = request.args['show_depth']
       cursor.execute("select * from dev.products_sample where month='%s'" % month + " and show='%s'" % show + " and show_depth='%s'" % show_depth)
       content = [dict((cursor.description[i][0], value)
          for i, value in enumerate(row)) for row in cursor.fetchall()]
       return jsonify({'myCollection': content})
       
if __name__ == '__main__':
    app.run(debug=True)