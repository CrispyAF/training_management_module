# -*- coding: utf-8 -*-

{
    'name': "Bista Training Management",

    'summary': """
    Used for managing the training of new employees
        """,

    'description': """
        Used for managing the training of new employees
    """,

    'author': "0d00_dev",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hr_employee_views.xml',
        'views/trainee_views.xml',
        'views/trainer_views.xml',
        'views/designation_views.xml',
        'views/location_views.xml',
        'views/training_subject_views.xml',
        'views/training_topic_views.xml',
        'views/trainee_attendance_views.xml',
        'views/trainee_batch_views.xml',
        'views/training_record_views.xml',
        # 'views/training_record_line_views.xml',
        # 'views/training_stages_views.xml',
        # 'views/training_topic_line_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
