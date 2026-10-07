# Placeholder for render.
import os
import sys
from split_settings.tools import include

# 1. 将 apps 目录强制加入 Python 路径，确保 actionlog 等模块可以被全局 import
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, 'apps')
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)

# 2. 按顺序导入基础配置与 Render 配置
include(
    'core.py',
    'render.py',
)
