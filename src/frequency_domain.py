"""
频域信号处理模块
实现各种频域变换和分析方法
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd
from pathlib import Path

def compute_fft(y, fs=1.0, window='hann'):
    """
    计算信号的快速傅里叶变换
    
    参数:
    y (array): 输入信号
    fs (float): 采样频率
    window (str): 窗函数类型
    
    返回:
    tuple: (频率数组, 幅值谱)
    """
    n = len(y)
    
    # 应用窗函数
    if window != 'rect':
        win = signal.get_window(window, n)
        y = y * win
    
    # 执行FFT
    yf = np.fft.rfft(y)
    
    # 计算频率轴
    freq = np.fft.rfftfreq(n, d=1/fs)
    
    # 计算单边振幅谱
    amp = 2.0 / n * np.abs(yf)
    
    return freq, amp

def compute_power_spectrum(y, fs=1.0, window='hann', nperseg=256, noverlap=None):
    """
    计算信号的功率谱密度
    
    参数:
    y (array): 输入信号
    fs (float): 采样频率
    window (str): 窗函数类型
    nperseg (int): 每段的长度
    noverlap (int): 重叠的点数
    
    返回:
    tuple: (频率数组, 功率谱密度)
    """
    freq, psd = signal.welch(y, fs, window, nperseg, noverlap)
    return freq, psd

def plot_spectrum(freq, amp, title='频谱图', figsize=(10, 6), scale='linear', save_path=None):
    """
    绘制频谱图
    
    参数:
    freq (array): 频率数组
    amp (array): 幅值数组
    title (str): 图表标题
    figsize (tuple): 图形尺寸
    scale (str): 刻度类型, 'linear', 'log', 或 'dB'
    save_path (str): 保存图像的路径
    """
    plt.figure(figsize=figsize)
    
    if scale == 'log':
        plt.loglog(freq, amp)
        plt.ylabel('幅值 (对数刻度)')
    elif scale == 'dB':
        # 转换为分贝
        with np.errstate(divide='ignore'):
            amp_db = 20 * np.log10(np.abs(amp))
        plt.semilogx(freq, amp_db)
        plt.ylabel('幅值 (dB)')
    else:  # linear
        plt.plot(freq, amp)
        plt.ylabel('幅值')
    
    plt.title(title)
    plt.xlabel('频率 (Hz)')
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path)
        print(f"图像已保存至 {save_path}")
    
    plt.show()

def frequency_band_energy(freq, psd, bands):
    """
    计算指定频带的能量
    
    参数:
    freq (array): 频率数组
    psd (array): 功率谱密度
    bands (list): 频带列表，每个元素为 (低频, 高频) 的元组
    
    返回:
    dict: 每个频带的能量
    """
    band_energy = {}
    
    for i, (low, high) in enumerate(bands):
        # 查找频带的索引范围
        idx = (freq >= low) & (freq <= high)
        if np.any(idx):
            # 计算带内能量
            energy = np.trapz(psd[idx], freq[idx])
            band_energy[f'band_{i+1}_{low}-{high}_Hz'] = energy
    
    return band_energy

def find_dominant_frequencies(freq, amp, n_peaks=5, min_height=None, min_distance=1):
    """
    查找主要频率分量
    
    参数:
    freq (array): 频率数组
    amp (array): 幅值数组
    n_peaks (int): 返回的峰值数量
    min_height (float): 最小峰值高度
    min_distance (float): 峰值之间的最小距离（单位：Hz）
    
    返回:
    pandas.DataFrame: 主要频率分量及其幅值
    """
    # 转换为索引上的最小距离
    if min_distance:
        if len(freq) > 1:
            freq_step = freq[1] - freq[0]
            min_distance = int(min_distance / freq_step) if freq_step > 0 else 1
        else:
            min_distance = 1
    
    # 查找峰值
    peak_indices = signal.find_peaks(amp, height=min_height, distance=min_distance)[0]
    
    # 按幅值排序
    peak_indices = peak_indices[np.argsort(-amp[peak_indices])]
    
    # 取前N个峰值
    if n_peaks and len(peak_indices) > n_peaks:
        peak_indices = peak_indices[:n_peaks]
    
    # 创建结果数据帧
    results = pd.DataFrame({
        'frequency': freq[peak_indices],
        'amplitude': amp[peak_indices]
    }).sort_values('amplitude', ascending=False)
    
    return results
