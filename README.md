# QLANG（Qi Language）

## 语法

var *var_name*;  # declare a variable

var *var_name* = *value*;  # define a variable

func *func_name*(*var a, var b~=Decimal, var c=3*) -> *ReturnType* { pass; }  # This is a typical example of defining a funtion. Arguments can be nothing but the braces cannot be omitted. But if a function does not return a value, you can omit the arrow.

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

