"""
ComfyUI-HY-Motion1

Text-to-Motion generation with FBX/GLB export support.
"""

import os
import sys

# Track initialization status
INIT_SUCCESS = False

if not os.environ.get('PYTEST_CURRENT_TEST'):
    print("[ComfyUI-HY-Motion1] Initializing custom node...")

    try:
        from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
        print("[ComfyUI-HY-Motion1] [OK] Node classes imported successfully")
        INIT_SUCCESS = True
    except Exception as e:
        import traceback
        print(f"[ComfyUI-HY-Motion1] [WARNING] Failed to import node classes: {e}")
        print(f"[ComfyUI-HY-Motion1] Traceback:\n{traceback.format_exc()}")
        NODE_CLASS_MAPPINGS = {}
        NODE_DISPLAY_NAME_MAPPINGS = {}

    if INIT_SUCCESS:
        print("[ComfyUI-HY-Motion1] [OK] Loaded successfully!")
    else:
        print("[ComfyUI-HY-Motion1] [ERROR] Failed to load - check errors above")

else:
    print("[ComfyUI-HY-Motion1] Running in pytest mode - skipping initialization")
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
__version__ = "0.3.1"
