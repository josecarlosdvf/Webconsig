# -*- encoding: utf-8 -*-
"""
Webconsig CRM System - Charts Routes
"""

from apps.charts import blueprint
from flask import render_template

@blueprint.route('/charts')
def charts():
    # Sample data for charts - replace with your CRM data
    sample_data = [
        {'name': 'Sample 1', 'value': 100},
        {'name': 'Sample 2', 'value': 200},
        {'name': 'Sample 3', 'value': 150}
    ]
    return render_template('charts/index.html', segment='charts', products=sample_data)