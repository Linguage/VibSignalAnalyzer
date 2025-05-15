# 震动信号分析系统 - 阶段一使用说明

## 当前进度

截止 2025年5月15日，项目已完成第一阶段的主要功能实现，包括：

1. 基础环境搭建
2. 合成信号生成模块
3. 时域分析功能
4. 频域分析功能
5. 示例程序和交互式分析 notebook

## 环境配置

### 自动配置方式

1. 打开终端，进入项目根目录。
2. 执行安装脚本：

   ```bash
   ./scripts/setup_env.sh
   ```

### 手动配置方式

如果自动配置脚本无法正常运行，可以按以下步骤手动配置：

1. 创建虚拟环境：

   ```bash
   python3 -m venv env/vibration_analysis
   ```

2. 激活虚拟环境：

   ```bash
   source env/vibration_analysis/bin/activate
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

## VS Code 配置

项目已包含 VS Code 配置文件（在 `.vscode` 文件夹中），支持：

- 自动使用项目的 Python 虚拟环境
- 代码智能提示和自动补全
- 集成调试环境
- Jupyter Notebook 支持

使用 VS Code 打开项目文件夹后，环境会自动配置完成。如需重新加载配置，可以：

1. 关闭并重新打开 VS Code。
2. 或使用命令面板（⌘+⇧+P）执行 "Developer: Reload Window"。

## 项目结构

```
项目根目录/
├── src/                    # 源代码
│   ├── time_domain.py      # 时域分析模块
│   └── frequency_domain.py # 频域分析模块
├── examples/               # 示例程序
├── notebooks/              # Jupyter notebooks
├── data/                   # 数据目录
│   ├── raw/                # 原始数据
│   └── processed/          # 处理后的数据
└── results/                # 结果输出
    ├── figures/            # 图表输出
    └── reports/            # 报告输出
```

## 使用说明

### 1. 运行示例程序

可以通过以下两种方式运行示例程序：

#### 方式一：使用 VS Code

1. 在 VS Code 中打开 `examples/generate_synthetic_signals.py`。
2. 点击右上角的运行按钮，或使用快捷键 F5。
3. 在运行配置中选择 "Python: 示例程序"。

#### 方式二：使用命令行

1. 激活虚拟环境（如果尚未激活）：

   ```bash
   source env/vibration_analysis/bin/activate
   ```

2. 运行示例程序：

   ```bash
   python examples/generate_synthetic_signals.py
   ```

### 2. 使用交互式分析笔记本

1. 在 VS Code 中直接打开 `notebooks/signal_analysis_demo.ipynb`。
2. 或通过命令行启动 Jupyter Notebook：

   ```bash
   jupyter notebook notebooks/signal_analysis_demo.ipynb
   ```

### 3. 生成的结果

示例程序运行后会生成：

1. 示例信号数据（保存在 `data/raw/` 目录）：
    - `sine_signal.csv`：纯正弦信号
    - `composite_signal.csv`：复合信号（正弦+噪声）
    - `chirp_signal.csv`：啁啾信号
2. 可视化结果（保存在 `results/figures/` 目录）：
    - 时域波形图
    - 频谱图
    - 其他分析结果图

## 已实现的功能

### 时域分析功能

- 信号加载与保存
- 合成信号生成（正弦、啁啾、脉冲、噪声等）
- 时域特征计算（均值、标准差、峰值等）
- 时域波形可视化

### 频域分析功能

- FFT 频谱分析
- 功率谱密度计算
- 主要频率分量识别
- 频谱可视化

## 下一步计划

1. 实现小波变换相关功能
2. 添加希尔伯特-黄变换模块
3. 开发结果对比与评估模块

## 注意事项

1. 运行程序前请确保虚拟环境已正确激活。
2. 示例数据和图表会自动保存到对应目录。
3. 如遇到导入模块错误，检查是否正确设置了 PYTHONPATH。

## 常见问题解决

1. 如果遇到模块导入错误，确保：
    - 已激活虚拟环境
    - 在项目根目录下运行程序
    - VS Code 使用了正确的 Python 解释器
2. 如果图表无法显示：
    - 检查 matplotlib 是否正确安装
    - 在 Jupyter Notebook 中添加 `%matplotlib inline`
3. 如果数据保存失败：
    - 检查目标目录是否存在
    - 确保有写入权限

## 获取帮助

如需技术支持或报告问题，请：

1. 查看源代码中的详细注释
2. 参考示例程序和 Notebook
3. 检查项目文档

---

最后更新时间：2025年5月15日
