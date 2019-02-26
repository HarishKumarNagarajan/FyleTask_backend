from django.shortcuts import render
from django.views.generic.base import TemplateView
import psycopg2
#import pprint
import json

def HomeView(request):
    query = request.GET.get('ifsc')
    query2 = request.GET.get('city')
    query3 = request.GET.get('bank')
    conn_string = "host='ec2-54-227-246-152.compute-1.amazonaws.com' dbname='d218lc4kiovrou' user='hwfzpbcmccsxqi' password='5d216f28599d664da4a569279aa3eba58901cbd7a02629f9f7d82058a5431581'"
    # print the connection string we will use to connect
    print("Connecting to database\n ->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # execute our Query
    if query != None:
        cursor.execute("SELECT * from branches where ifsc='{}'".format(query))
        records = cursor.fetchall()
        jsonout = json.dumps([dict(ix) for ix in records])
        return render(request, 'index.html', {'disp': jsonout})

    else:
        cursor.execute("select * from bank_branches where city='{}' AND bank_name='{}'".format(query2,query3))


    # retrieve the records from the database
        records = cursor.fetchall()

    #last = json.loads(records)
    #pprint(last)
    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    #pprint.pprint(records)
    #pprint.pprint("hello")
        jsonout = json.dumps([dict(ix) for ix in records])
        return render(request, 'index.html', {'disp': jsonout})
