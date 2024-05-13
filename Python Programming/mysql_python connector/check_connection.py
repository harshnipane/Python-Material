# -*- coding: utf-8 -*-
"""
Created on Mon May  8 14:46:18 2023

@author: cdacstaff
"""

#pip install mysql-connector-python

import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cnx.close()