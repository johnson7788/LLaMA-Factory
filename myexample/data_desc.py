#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2024/1/26 11:26
# @File  : data_desc.py
# @Author: 
# @Desc  : 生成数据集描述
import os
import json

def generate_file():
    file = "../data/dataset_info.json"
    with open(file, "r") as f:
        data = json.load(f)
    save_file = "dataset_desc.json"
    new_data = {}
    for name, value in data.items():
        new_data[name] = {}
        new_data[name]["desc"] = ""
        new_data[name]["url"] = ""
        new_data[name]["paper"] = ""
        new_data[name]["format"] = ""
        new_data[name]["language"] = ""
        new_data[name]["multiturn"] = True
        new_data[name]["length"] = 1000
        new_data[name]["formodel"] = "Pretrain"
    with open(save_file, "w") as f:
        json.dump(new_data, f, indent=4)
    print(f"数据集描述已生成到 {save_file}")

def data_length(name):
    """
    打印数据集的长度
    """
    file = f"../data/{name}"
    assert os.path.exists(file), f"文件 {file} 不存在"
    with open(file, "r") as f:
        data = json.load(f)
    print(f"数据集 {name} 的长度为 {len(data)}")

def modify_data():
    save_file = "dataset_desc.json"
    with open(save_file, "r") as f:
        data = json.load(f)
    new_data = {}
    for name,one in data.items():
        desc = one["desc"]
        if desc == "":
            one["format"] = "alpaca"
            one["language"] = "英文"
            one["multiturn"] = False
            one["formodel"] = "Pretrain,SFT"
        new_data[name] = one
    with open(save_file, "w") as f:
     json.dump(new_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # generate_file()
    data_length("c4_demo.json")
    # modify_data()
