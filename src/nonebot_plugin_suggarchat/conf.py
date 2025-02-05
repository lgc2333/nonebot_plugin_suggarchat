import os
from nonebot.adapters.onebot.v11 import Bot
import nonebot_plugin_localstore as store
__KERNEL_VERSION__:str = "V1.9.3-Public"
# 获取当前工作目录  
current_directory:str = os.getcwd()  
config_dir = store.get_plugin_config_dir()
if not config_dir.exists():
    config_dir.mkdir()
group_memory = store.get_plugin_data_dir()/"group"
if not group_memory.exists():
    group_memory.mkdir()
private_memory = store.get_plugin_data_dir()/"private"
if not private_memory.exists():
    private_memory.mkdir()
main_config = config_dir/"config.json"
group_prompt = config_dir/"prompt_group.txt"
private_prompt = config_dir/"prompt_private.txt"
custom_models_dir = config_dir/"models"
def init(bot:Bot):
    global config_dir
    config_dir = config_dir/bot.self_id