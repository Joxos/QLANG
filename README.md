# Sakura 樱花语

## 语法

变量声明/定义：

```sakura
<Type> <variable_name>( = <value>)
```

## 运行

**注：需要安装Python3**

```bash
sakura <filename>
```

## 命名规范

1. 变量名：Camel
2. 类型：Pascal
3. 常量：全大写或Pascal
4. 函数：Camel
5. 装饰器：Pascal

## 开发者指南

编译指令：

```bash
python -m nuitka --remove-output --output-dir=build --clang --follow-imports --show-progress --show-scons .\sakura.py
```

