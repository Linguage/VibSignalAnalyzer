# VibSignalAnalyzer (振动、信号分析系统)

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 项目简介

VibSignalAnalyzer 是一个全面的振动、信号分析工具包，用于实现振动、信号的时域、频域和时频域分析。本项目支持多种信号变换方法的对比分析，包括傅立叶变换、小波变换和希尔伯特-黄变换等。

### 主要特性

- 🌊 支持多种信号生成和采集
  - 合成信号生成（正弦、啁啾、脉冲等）
  - 实际振动、信号采集与处理

- 📊 丰富的分析功能
  - 时域分析（统计特征、波形分析）
  - 频域分析（FFT、功率谱）
  - 时频分析（小波变换）
  - 非线性分析（希尔伯特-黄变换）

- 📈 可视化与结果对比
  - 多种可视化方式
  - 算法性能对比
  - 结果导出功能

## 快速开始

### 环境要求

- Python 3.12 或更高版本
- 相关依赖包（见 requirements.txt）

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/VibSignalAnalyzer.git
cd VibSignalAnalyzer
```

2. 运行安装脚本：
```bash
./scripts/setup_env.sh
```

### 使用示例

1. 生成并分析合成信号：
```bash
python examples/generate_synthetic_signals.py
```

2. 使用交互式notebook进行分析：
```bash
jupyter notebook notebooks/signal_analysis_demo.ipynb
```

## 项目结构

```
VibSignalAnalyzer/
├── src/                    # 源代码
│   ├── time_domain.py      # 时域分析模块
│   └── frequency_domain.py # 频域分析模块
├── examples/               # 示例程序
├── notebooks/             # Jupyter notebooks
├── data/                  # 数据目录
├── results/               # 结果输出
└── docs/                  # 文档
```

## 文档

详细的使用说明和API文档请参考 [docs/phase1_guide.md](docs/phase1_guide.md)。

## 开发计划

- [x] 基础框架搭建
- [x] 时域分析模块
- [x] 频域分析模块
- [ ] 小波变换模块
- [ ] 希尔伯特-黄变换模块
- [ ] 性能评估模块

## 贡献指南

欢迎提交 Issue 和 Pull Request。在提交代码前，请确保：

1. 代码风格符合项目规范
2. 添加了适当的测试用例
3. 更新了相关文档

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 参考资料

- 《信号处理原理与应用》
- 《小波分析及其应用》
- Huang et al., "The empirical mode decomposition and the Hilbert spectrum for nonlinear and non-stationary time series analysis"

## 联系方式

- 项目维护者：[Your Name]
- 电子邮件：[your.email@example.com]

---

最后更新时间：2025年5月15日
