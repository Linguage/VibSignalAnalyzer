#!/usr/bin/env python3
"""
振动信号分析系统 - 示例程序
此示例展示了如何生成、分析和可视化不同类型的振动信号
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.time_domain import generate_synthetic_signal, calculate_time_features, plot_time_signal
from src.frequency_domain import compute_fft, plot_spectrum, find_dominant_frequencies

def generate_example_signals():
    """生成不同类型的示例信号并进行分析"""
    # 创建输出目录
    results_dir = project_root / 'results'
    figure_dir = results_dir / 'figures'
    figure_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. 生成正弦信号
    print("\n=== 生成正弦信号 ===")
    t, y_sine = generate_synthetic_signal(
        signal_type='sine',
        duration=1.0,
        sampling_rate=1000,
        frequency=10,
        amplitude=1.0
    )
    
    # 保存时域图
    plot_time_signal(
        t, y_sine,
        title='正弦信号 (10Hz)',
        save_path=str(figure_dir / 'sine_time.png')
    )
    
    # 计算并显示频谱
    freq, amp = compute_fft(y_sine, fs=1000)
    plot_spectrum(
        freq, amp,
        title='正弦信号频谱',
        save_path=str(figure_dir / 'sine_freq.png')
    )
    
    # 计算时域特征
    features = calculate_time_features(y_sine)
    print("时域特征:")
    for name, value in features.items():
        print(f"{name}: {value:.4f}")
    
    # 2. 生成复合信号（正弦+噪声）
    print("\n=== 生成复合信号 ===")
    t, y_composite = generate_synthetic_signal(
        signal_type='composite',
        duration=1.0,
        sampling_rate=1000,
        frequency=10,
        signal_amplitude=1.0,
        noise_amplitude=0.2
    )
    
    # 保存时域图
    plot_time_signal(
        t, y_composite,
        title='复合信号 (正弦+噪声)',
        save_path=str(figure_dir / 'composite_time.png')
    )
    
    # 计算并显示频谱
    freq, amp = compute_fft(y_composite, fs=1000)
    plot_spectrum(
        freq, amp,
        title='复合信号频谱',
        save_path=str(figure_dir / 'composite_freq.png')
    )
    
    # 查找主要频率分量
    dominant_freqs = find_dominant_frequencies(freq, amp, n_peaks=3)
    print("\n主要频率分量:")
    print(dominant_freqs)
    
    # 3. 生成啁啾信号
    print("\n=== 生成啁啾信号 ===")
    t, y_chirp = generate_synthetic_signal(
        signal_type='chirp',
        duration=1.0,
        sampling_rate=1000,
        f0=5,  # 起始频率
        f1=50,  # 结束频率
        amplitude=1.0
    )
    
    # 保存时域图
    plot_time_signal(
        t, y_chirp,
        title='啁啾信号 (5-50Hz)',
        save_path=str(figure_dir / 'chirp_time.png')
    )
    
    # 计算并显示频谱
    freq, amp = compute_fft(y_chirp, fs=1000)
    plot_spectrum(
        freq, amp,
        title='啁啾信号频谱',
        save_path=str(figure_dir / 'chirp_freq.png')
    )
    
    # 4. 保存示例数据
    print("\n=== 保存示例数据 ===")
    data_dir = project_root / 'data' / 'raw'
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存为CSV格式
    import pandas as pd
    for signal_name, signal_data in [
        ('sine', y_sine),
        ('composite', y_composite),
        ('chirp', y_chirp)
    ]:
        df = pd.DataFrame({
            'time': t,
            'amplitude': signal_data
        })
        df.to_csv(data_dir / f'{signal_name}_signal.csv', index=False)
        print(f"已保存 {signal_name}_signal.csv")

if __name__ == '__main__':
    generate_example_signals()
