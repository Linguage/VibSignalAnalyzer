#!/bin/bash
# 震动信号分析系统 - 环境安装脚本
# 此脚本用于自动化安装项目所需的依赖

# 设置颜色变量，用于美化输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 显示欢迎信息
echo -e "${GREEN}=== 震动信号分析系统 - 环境安装程序 ===${NC}"
echo "此脚本将为您设置项目所需的Python环境和依赖包"
echo ""

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}错误: 未检测到Python3。请先安装Python3后再运行此脚本。${NC}"
    exit 1
fi

# 显示检测到的Python版本
PYTHON_VERSION=$(python3 --version)
echo -e "检测到 ${GREEN}${PYTHON_VERSION}${NC}"

# 项目根目录路径
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo -e "项目根目录: ${GREEN}${PROJECT_ROOT}${NC}"

# 创建虚拟环境（如果尚未存在）
ENV_PATH="${PROJECT_ROOT}/env/vibration_analysis"

if [ ! -d "$ENV_PATH" ]; then
    echo "正在创建Python虚拟环境..."
    python3 -m venv "${ENV_PATH}" || { echo -e "${YELLOW}创建虚拟环境失败${NC}"; exit 1; }
    echo -e "${GREEN}虚拟环境创建成功！${NC}"
else
    echo -e "${GREEN}检测到已有虚拟环境，将复用现有环境${NC}"
fi

# 激活虚拟环境
echo "正在激活虚拟环境..."
source "${ENV_PATH}/bin/activate" || { echo -e "${YELLOW}激活虚拟环境失败${NC}"; exit 1; }

# 更新pip
echo "正在更新pip..."
pip install --upgrade pip

# 安装依赖
echo "正在安装项目依赖..."
pip install -r "${PROJECT_ROOT}/requirements.txt" || { echo -e "${YELLOW}依赖安装失败${NC}"; exit 1; }

# 创建必要的文件夹（如果不存在）
echo "正在创建项目文件夹结构..."
mkdir -p "${PROJECT_ROOT}/data/raw"
mkdir -p "${PROJECT_ROOT}/data/processed"
mkdir -p "${PROJECT_ROOT}/results/figures"
mkdir -p "${PROJECT_ROOT}/results/reports"

# 安装成功信息
echo -e "${GREEN}=== 安装完成! ===${NC}"
echo "您可以通过以下命令激活环境："
echo -e "${YELLOW}source ${ENV_PATH}/bin/activate${NC}"
echo ""
echo "推荐的下一步操作："
echo "1. 运行示例程序: python ${PROJECT_ROOT}/examples/generate_synthetic_signals.py"
echo "2. 查看Jupyter笔记本: jupyter notebook ${PROJECT_ROOT}/notebooks/"
echo ""
echo -e "${GREEN}祝您使用愉快！${NC}"
