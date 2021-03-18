{
    'name': 'Sale Order Email',
    'version': '1.1',
    'summary': 'Create this module for testing purpose',
    'category': 'Sale order',
    'depends': ['sale'],

    # 'data': [],
    'data': ['views/sale_order_email_view.xml', 'views/mail_template.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,

}