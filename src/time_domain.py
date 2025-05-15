"""
时域信号处理模块
处理和分析震动信号的时域特性
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import scipy.signal as signal

def load_signal(file_path, column_name=None):
    """
    从文件加载时域信号
    
    参数:
    file_path (str): 数据文件路径
    column_name (str, optional): 如果数据是表格形式，指定信号所在列名
    
    返回:
    tuple: (时间数组, 信号数组)
    """
    file_path = Path(file_path)
    if file_path.suffix == '.csv':
        df = pd.read_csv(file_path)
        if column_name and column_name in df.columns:
            y = df[column_name].values
        else:
            # 假设第一列是时间，第二列是信号
            if len(df.columns) >= 2:
                t = df.iloc[:, 0].values
                y = df.iloc[:, 1].values
                return t, y
            else:
                y = df.iloc[:, 0].values
        
        # 如果没有时间列，生成时间序列
        t = np.arange(len(y))
        return t, y
    
    elif file_path.suffix in ['.npy', '.npz']:
        data = np.load(file_path)
        if isinstance(data, np.ndarray):
            if data.ndim == 1:
                t = np.arange(len(data))
                return t, data
            elif data.ndim == 2 and data.shape[1] == 2:
                return data[:, 0], data[:, 1]
        elif isinstance(data, dict) and 'time' in data and 'signal' in data:
            return data['time'], data['signal']
    
    # 其他格式可自行扩展
    raise ValueError(f"不支持的文件格式: {file_path.suffix}")

def generate_synthetic_signal(signal_type='sine', duration=1.0, sampling_rate=1000, **kwargs):
    """
    生成合成的振动信号用于测试
    
    参数:
    signal_type (str): 信号类型，可以是'sine', 'chirp', 'impulse', 'noise'等
    duration (float): 信号持续时间（秒）
    sampling_rate (int): 采样率（Hz）
    **kwargs: 具体信号类型的其他参数
    
    返回:
    tuple: (时间数组, 信号数组)
    """
    t = np.linspace(0, duration, int(duration * sampling_rate))
    
    if signal_type == 'sine':
        freq = kwargs.get('frequency', 10)
        amplitude = kwargs.get('amplitude', 1.0)
        phase = kwargs.get('phase', 0.0)
        y = amplitude * np.sin(2 * np.pi * freq * t + phase)
    
    elif signal_type == 'chirp':
        f0 = kwargs.get('f0', 5)  # 起始频率
        f1 = kwargs.get('f1', 50)  # 结束频率
        amplitude = kwargs.get('amplitude', 1.0)
        y = amplitude * signal.chirp(t, f0, duration, f1)
    
    elif signal_type == 'impulse':
        loc = kwargs.get('location', duration/2)
        width = kwargs.get('width', 0.01)
        amplitude = kwargs.get('amplitude', 1.0)
        # 高斯脉冲
        y = amplitude * np.exp(-0.5 * ((t - loc) / width) ** 2)
    
    elif signal_type == 'noise':
        noise_type = kwargs.get('noise_type', 'white')
        amplitude = kwargs.get('amplitude', 1.0)
        if noise_type == 'white':
            y = amplitude * np.random.randn(len(t))
        else:
            # 可以扩展其他类型的噪声
            y = amplitude * np.random.randn(len(t))
    
    elif signal_type == 'composite':
        # 复合信号，例如正弦+噪声
        freq = kwargs.get('frequency', 10)
        signal_amp = kwargs.get('signal_amplitude', 1.0)
        noise_amp = kwargs.get('noise_amplitude', 0.2)
        
        signal_component = signal_amp * np.sin(2 * np.pi * freq * t)
        noise_component = noise_amp * np.random.randn(len(t))
        y = signal_component + noise_component
    
    else:
        raise ValueError(f"不支持的信号类型: {signal_type}")
    
    return t, y

def calculate_time_features(signal):
    """计算时域特征"""
    mean = np.mean(signal)
    std = np.std(signal)
    rms = np.sqrt(np.mean(np.square(signal)))
    peak = np.max(np.abs(signal))
    crest_factor = peak / rms if rms > 0 else 0
    kurtosis = np.sum((signal - mean) ** 4) / (len(signal) * std ** 4) if std > 0 else 0
    
    return {
        'mean': mean,
        'std': std,
        'rms': rms,
        'peak': peak,
        'crest_factor': crest_factor,
        'kurtosis': kurtosis
    }

def plot_time_signal(t, y, title='时域信号', figsize=(10, 6), save_path=None):
    """绘制时域信号"""
    plt.figure(figsize=figsize)
    plt.plot(t, y)
    plt.title(title)
    plt.xlabel('时间 (s)')
    plt.ylabel('幅值')
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path)
        print(f"图像已保存至 {save_path}")
    
    plt.show()
