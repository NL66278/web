# -*- coding: utf-8 -*-
# © 2013-2015 OpenERP SA (http://odoo.com).
# © 2016 Therp BV (http://therp.nl).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Attachment Size Limit',
    'category': 'Hidden',
    'version': '8.0.2.0.0',
    'license': 'AGPL-3',
    'author': 'OpenERP SA,Therp BV,Odoo Community Association (OCA)',
    'summary': 'Limits on # file, size on uploads, Block users for uploading',
    'description': """
Define a size limit for the attachments
=========================================
In company configuration you can control these three things:

* Maximum files allowed to upload per record.
* Maximum size of file that can be uploaded.
* Block User.
""",
    'depends': [
        'web',
        'document',
    ],
    'js': [
        'static/src/js/attachment_size_limit.js',
    ],
    'data': [
        'views/res_company_view.xml',
        'web/resources.xml',
    ],
    'installable': True,
}
