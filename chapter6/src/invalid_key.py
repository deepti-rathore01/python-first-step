"""
@file  :invalid_key.py
@brief :Print 'Invalid key!' when d['os_ver'] on d={'os':'linux'}
"""
try:
    d={'os':'linux'}
    print d['os_ver'] 
except:
    print 'Invalid key!' 
