import os
from nonebot import require

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store
__KERNEL_VERSION__:str = "V0.1.5.6-Public-Dev"
# 获取当前工作目录  
current_directory:str = str(store.get_plugin_data_dir())
_confdir = store.get_plugin_config_dir()
_datadir = store.get_plugin_data_dir()
config_dir = _confdir/"config"
if not config_dir.exists():
    config_dir.mkdir()
group_memory = _datadir/"group"
if not group_memory.exists():
    group_memory.mkdir()
private_memory = _datadir/"private"
if not private_memory.exists():
    private_memory.mkdir()
main_config = config_dir/"config.json"
custom_models_dir = config_dir/"models"