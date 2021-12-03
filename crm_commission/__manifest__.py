{
    'name': 'commission Generation',
    'version': '14.0.1.0',
    'depends': ['report_xlsx'],
    'data': ['security/ir.model.access.csv',
             'views/crm_commission.xml',
             'data/sequence.xml',
             'wizard/commission_wizard.xml',
             'report/report.xml',
             'report/commission_pdf.xml'],
    'depends': ['base', 'crm'],
    "external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    'auto_install': False,
    'installable': True,
    'license': 'LGPL-3',
}