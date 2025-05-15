"""
震动信号分析系统 - 主模块
用于分析震动信号的时域、频域和时频域转换
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 项目根目录
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
RESULTS_DIR = ROOT_DIR / "results"

# 确保必要的目录存在
DATA_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

def setup():
    """初始化系统环境"""
    print(f"震动信号分析系统初始化...")
    print(f"数据目录: {DATA_DIR}")
    print(f"结果目录: {RESULTS_DIR}")
    
    # 检查依赖项是否已安装
    try:
        import scipy
        import pywt
        import PyEMD
        print("所有依赖项已正确安装")
        return True
    except ImportError as e:
        print(f"依赖项缺失: {e}")
        print("请执行 'pip install -r requirements.txt' 安装所有依赖")
        return False

if __name__ == "__main__":
    setup()
