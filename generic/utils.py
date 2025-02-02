import json
import os

def get_css_and_js_link_from_vite_assets(type):
    """
    We read the vite diretory bath of the build from the manifest
    file and then use that to find our static assets to load the
    react application
    """
    css_links = []
    js_links = []
    main_js_links = []
    asset_manifest = open("backend/static/js/" + type + "/build/.vite/manifest.json").read()
    asset_manifest_dict = json.loads(asset_manifest)
    for key, value in asset_manifest_dict.items():
        if key == "index.html":
            """
            {'index.html': 
            {'file': 'assets/index-BtVi8doP.js', 'name': 'index', 'src': 'index.html', 'isEntry': True, 
            'css': ['assets/index-n_ryQ3BS.css'], 
            'assets': ['assets/react-CHdo91hT.svg']}, 
            'src/assets/react.svg': {'file': 'assets/react-CHdo91hT.svg', 
            'src': 'src/assets/react.svg'
            }
            }
            """
            full_js_link = "js/" + type + "/build/" + value.get("file")
            js_links = [full_js_link]
            main_js_links = [full_js_link]
            css_file = "js/" + type + "/build/" + value.get("css")[0]
            css_links = [css_file]
    print("DEBUG" * 100)
    print(css_links, js_links, main_js_links)
    print("DEBUG" * 100)
    return css_links, js_links, main_js_links
