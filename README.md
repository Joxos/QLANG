# QLANG（Qi Language）

## 命名规范

1. 变量名：Camel
2. 类型：Pascal
3. 常量：全大写
4. 函数：Camel

## 开发者指南

编译指令：

```bash
python -m nuitka --remove-output --output-dir=build --clang --follow-imports --show-progress --show-scons .\sakura.py
```

编译ANTLR：

```bash
java -jar ./antlr-4.9.2-complete.jar -Dlanguage=Python3 -no-listener -visitor ./QLANG.g4
```

