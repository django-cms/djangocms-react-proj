def get_css_and_js_link_from_vite_assets(type):
    """
    We read the vite diretory bath of the build from the manifest
    file and then use that to find our static assets to load the
    react application
    """
    css_links = []
    js_links = []
    main_js_links = []
    asset_manifest = open("static/js/" + type + "/build/manifest.json").read()
    asset_manifest_dict = json.loads(asset_manifest)
    for key, value in asset_manifest_dict.items():
        if key == "index.html":
            """
            {'index.css': {'file': 'static/css/main.272c5c26.css', 'src': 'index.css'},
            'index.html': {'css': ['static/css/main.272c5c26.css'],
            'file': 'static/js/main.0e6a838c.js', 'isEntry': True, 'src': 'index.html'}}
            """
            js_file = value.get("file")
            full_js_link = "js/" + type + "/build/" + js_file
            js_links = [full_js_link]
            main_js_links = [full_js_link]
            css_file = "js/" + type + "/build/" + "static/css/main.css";
            css_links = [css_file]
    return css_links, js_links, main_js_links
