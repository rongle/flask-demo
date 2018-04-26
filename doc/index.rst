.. mzly documentation master file, created by
   sphinx-quickstart on Wed Nov 18 14:34:15 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

要盈利API文档-商户
================

商户接口
##########

.. autoflask:: api:create_app('default')
    :blueprints: app
    :undoc-endpoints: api.unionpaycallback, api.cmpay_callback, api.cmpay_notify, api.alipaynotify, api.wxpay_notify
    :undoc-static:


管理后台接口
#############

.. autoflask:: api:create_app('default')
    :blueprints: admin
    :undoc-static:

