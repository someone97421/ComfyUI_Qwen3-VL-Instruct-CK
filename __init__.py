from .nodes import Qwen3_VQA
# 引入我们的新本地节点文件
from .nodes_local import Qwen3_VQA_Local
from .util_nodes import ImageLoader, VideoLoader, VideoLoaderPath
from .path_nodes import MultiplePathsInput

WEB_DIRECTORY = "./web"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Qwen3_VQA": Qwen3_VQA,
    "Qwen3_VQA_Local": Qwen3_VQA_Local,  # 新增：注册本地版节点类
    "ImageLoader": ImageLoader,
    "VideoLoader": VideoLoader,
    "VideoLoaderPath": VideoLoaderPath,
    "MultiplePathsInput": MultiplePathsInput,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Qwen3_VQA": "Qwen3 VQA",
    "Qwen3_VQA_Local": "👻Qwen3 VQA (Local)-CK👻",  # 新增：设置显示名称
    "ImageLoader": "Load Image Advanced",
    "VideoLoader": "Load Video Advanced",
    "VideoLoaderPath": "Load Video Advanced (Path)",
    "MultiplePathsInput": "Multiple Paths Input",
}