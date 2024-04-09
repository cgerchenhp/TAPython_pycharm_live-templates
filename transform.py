import xml.etree.ElementTree as ET
import json
import re

def convert_variable_syntax(value):
    """
    将PyCharm变量格式($VARIABLE$)转换为VS Code格式(${VARIABLE})
    """
    return re.sub(r'\$(\w+)\$', r'${\1}', value)


def convert_xml_to_json(xml_file, json_file):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    snippets = {}

    # 遍历每个模板
    for template in root.findall('template'):
        name = template.get('name')
        value = template.get('value')
        description = template.get('description')

        # 转换变量格式并将模板内容转换为VS Code需要的字符串数组格式
        body = convert_variable_syntax(value).split('\n')

        # 构建VS Code片段格式
        snippet = {
            'prefix': name,
            'body': body,
            'description': description
        }

        snippets[name] = snippet

    # 写入JSON文件
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(snippets, f, indent=4, ensure_ascii=False)

# 调用函数进行转换
convert_xml_to_json('./templates/TAPython.xml', './templates/json.json')