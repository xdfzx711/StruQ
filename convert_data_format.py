#!/usr/bin/env python3
"""
将 unicode_alpaca.json 转换为目标数据格式
目标格式：只包含 instruction 和 input 字段的 JSON 列表
"""

import json

def convert_data_format(input_file, output_file):
    """
    转换数据格式
    
    Args:
        input_file: 源数据文件路径
        output_file: 目标数据文件路径
    """
    # 读取源数据
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 转换格式
    converted_data = []
    for item in data:
        converted_item = {
            "instruction": item.get("instruction", ""),
            "input": item.get("input", "")
        }
        converted_data.append(converted_item)
    
    # 保存转换后的数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, ensure_ascii=False, indent=2)
    
    print(f"转换完成！")
    print(f"源文件: {input_file}")
    print(f"目标文件: {output_file}")
    print(f"转换了 {len(converted_data)} 条记录")

if __name__ == "__main__":
    # 设置文件路径
    input_file = "unicode_alpaca.json"
    output_file = "test_data.json"  # 可以改为其他名称
    
    convert_data_format(input_file, output_file)
