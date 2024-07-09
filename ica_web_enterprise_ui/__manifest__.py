# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Enterprise',
    'category': 'Hidden',
    'version': '1.0',
    'description': """
Odoo Enterprise Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
        """,
    'depends': ['web', 'base_setup'],
    'auto_install': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'ica_web_enterprise_ui/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'ica_web_enterprise_ui/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'ica_web_enterprise_ui/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'ica_web_enterprise_ui/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'ica_web_enterprise_ui/static/src/webclient/home_menu/home_menu_background.scss', # used by login page
            'ica_web_enterprise_ui/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'ica_web_enterprise_ui/static/src/webclient/**/*.scss',
            'ica_web_enterprise_ui/static/src/views/**/*.scss',

            'ica_web_enterprise_ui/static/src/core/**/*',
            'ica_web_enterprise_ui/static/src/webclient/**/*.js',
            'ica_web_enterprise_ui/static/src/webclient/**/*.xml',
            'ica_web_enterprise_ui/static/src/views/**/*.js',
            'ica_web_enterprise_ui/static/src/views/**/*.xml',

            # Don't include dark mode files in light mode
            ('remove', 'ica_web_enterprise_ui/static/src/**/*.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'ica_web_enterprise_ui/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'ica_web_enterprise_ui/static/src/scss/primary_variables.scss', 'ica_web_enterprise_ui/static/src/scss/primary_variables.dark.scss'),
            ('before', 'ica_web_enterprise_ui/static/src/**/*.variables.scss', 'ica_web_enterprise_ui/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'ica_web_enterprise_ui/static/src/scss/secondary_variables.scss', 'ica_web_enterprise_ui/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'ica_web_enterprise_ui/static/src/scss/bootstrap_overridden.scss', 'ica_web_enterprise_ui/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'ica_web_enterprise_ui/static/src/scss/bs_functions_overridden.dark.scss'),
            # assets_backend
            'ica_web_enterprise_ui/static/src/**/*.dark.scss',
        ],
        'web.tests_assets': [
            'ica_web_enterprise_ui/static/tests/*.js',
        ],
        'web.qunit_suite_tests': [
            'ica_web_enterprise_ui/static/tests/views/**/*.js',
            'ica_web_enterprise_ui/static/tests/webclient/**/*.js',
            ('remove', 'ica_web_enterprise_ui/static/tests/webclient/action_manager_mobile_tests.js'),
        ],
        'web.qunit_mobile_suite_tests': [
            'ica_web_enterprise_ui/static/tests/views/disable_patch.js',
            'ica_web_enterprise_ui/static/tests/mobile/**/*.js',
            'ica_web_enterprise_ui/static/tests/webclient/action_manager_mobile_tests.js',
        ],
    },
    'license': 'OEEL-1',
}
