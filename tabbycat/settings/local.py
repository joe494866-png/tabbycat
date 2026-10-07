# Placeholder for render.
import os
import sys
from split_settings.tools import include

# 获取当前 settings 目录以及项目 root 路径
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__)) # tabbycat/settings
TABBYCAT_DIR = os.path.dirname(SETTINGS_DIR)               # tabbycat
APPS_DIR = os.path.join(TABBYCAT_DIR, 'apps')               # tabbycat/apps

# 确保 apps 目录和 tabbycat 根目录都在 sys.path 最前面
for path in [APPS_DIR, TABBYCAT_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

# 加载基础设置和 Render 专属设置
include(
    'core.py',
    'render.py',
)

# 覆盖静态文件存储后端，忽略缺失文件哈希映射引起的崩溃
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# 兼容旧版 Django 的静态文件设置
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
