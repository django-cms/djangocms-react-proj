import json
import os

import json
from typing import List, Tuple
from pathlib import Path

def get_css_and_js_link_from_vite_assets(project_type: str) -> Tuple[List[str], List[str], List[str]]:
    """
    Retrieve CSS and JS links from Vite asset manifest.

    Args:
        project_type (str): The type/name of the project build.

    Returns:
        Tuple containing:
        - CSS links
        - JS links
        - Main JS links
    """
    # Construct the path to the manifest file
    manifest_path = Path(f"backend/static/js/{project_type}/build/.vite/manifest.json")

    try:
        # Read and parse the manifest file
        with manifest_path.open('r') as manifest_file:
            asset_manifest_dict = json.load(manifest_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading manifest file: {e}")
        return [], [], []

    # Extract entry point (index.html) information
    entry_point = asset_manifest_dict.get('index.html', {})

    # Construct full paths for assets
    base_path = f"js/{project_type}/build/"

    css_links = [base_path + entry_point.get('css', [''])[0]] if entry_point.get('css') else []
    js_links = [base_path + entry_point.get('file', '')] if entry_point.get('file') else []
    main_js_links = js_links.copy()

    return css_links, js_links, main_js_links

