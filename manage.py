#!/usr/bin/env python
import os
import sys
import psycopg2
import pprint

if __name__ == "__main__":
    conn_string = "host='ec2-54-227-246-152.compute-1.amazonaws.com' dbname='d218lc4kiovrou' user='hwfzpbcmccsxqi' password='5d216f28599d664da4a569279aa3eba58901cbd7a02629f9f7d82058a5431581'"
    # print the connection string we will use to connect
    print("Connecting to database\n ->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("select * from bank_branches where city='MUMBAI' AND bank_name='ABHYUDAYA COOPERATIVE BANK LIMITED'")

    # retrieve the records from the database
    records = cursor.fetchall()
    #pprint.pprint(records)

    #index = open("templates/index.html").read().format(disp=records)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ftask.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)