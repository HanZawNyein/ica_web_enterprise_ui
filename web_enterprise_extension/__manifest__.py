{
    "name":"Web Enterprise Extension",
    "license":"LGPL-3",
    "depends":["web_enterprise"],
    "assets":{
        'web.assets_backend': [
            'web_enterprise_extension/static/src/webclient/home_menu/home_menu.xml',
            'web_enterprise_extension/static/src/webclient/home_menu/home_menu.js',
            ('remove','web_enterprise/static/src/webclient/settings_form_view/res_config_edition.xml'),
        ]
    }
}