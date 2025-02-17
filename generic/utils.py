import json
import os

import json
from typing import List, Tuple
from pathlib import Path

def get_css_and_js_link_from_vite_assets(project_type: str, uses_client: bool = False) -> Tuple[List[str], List[str], List[str]]:
    """
    Retrieve CSS and JS links from Vite asset manifest.

    Args:
        project_type (str): The type/name of the project build.
        uses_client (bool): Whether to use the client build path.

    Returns:
        Tuple containing:
        - CSS links
        - JS links
        - Main JS links (entry points)
    """
    # Construct the path to the manifest file
    if uses_client:
        manifest_path = Path(f"backend/static/js/{project_type}/build/client/.vite/manifest.json")
        # Construct full paths for assets
        base_path = f"js/{project_type}/build/client/"
        print(manifest_path, base_path)
    else:
        manifest_path = Path(f"backend/static/js/{project_type}/build/.vite/manifest.json")
        base_path = f"js/{project_type}/build/"

    # try/:
    # Read and parse the manifest file
    with manifest_path.open('r', encoding="utf-8") as manifest_file:
        asset_manifest_dict = json.load(manifest_file)
        print(manifest_path, base_path)
        print(asset_manifest_dict)
    # except (FileNotFoundError, json.JSONDecodeError) as e:
    #     print(f"Error reading manifest file: {e}")
    #     return [], [], []

    css_links = []
    js_links = []
    main_js_links = []

    # Iterate through all entries in the manifest
    for key, entry in asset_manifest_dict.items():
        # Skip entries that don't have a 'file' property
        if 'file' not in entry:
            continue

        # Add CSS assets
        if 'assets' in entry:
            for asset in entry['assets']:
                if asset.endswith('.css'):
                    css_links.append(base_path + asset)

        # Add JS files
        file_path = entry['file']
        if file_path.endswith('.js'):
            js_links.append(base_path + file_path)
            # If it's an entry point, add to main_js_links
            if entry.get('isEntry', False):
                main_js_links.append(base_path + file_path)

    return css_links, js_links, main_js_links

