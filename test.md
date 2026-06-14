# Python 学习指南

## 第一章：基础语法

Python 是一种高级编程语言，由 Guido van Rossum 于 1991 年发布。Python 的设计哲学强调代码的可读性和简洁性。

### 1.1 变量与数据类型

Python 支持多种数据类型：
- 整数（int）：如 42
- 浮点数（float）：如 3.14
- 字符串（str）：如 "hello"
- 布尔值（bool）：True 或 False
- 列表（list）：如 [1, 2, 3]
- 字典（dict）：如 {"name": "Alice", "age": 25}

### 1.2 控制流

Python 使用 if/elif/else 进行条件判断，使用 for 和 while 进行循环。

```python
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

## 第二章：函数与模块

函数是组织代码的基本单位。Python 中使用 def 关键字定义函数。

### 2.1 函数定义

```python
def greet(name, greeting="Hello"):
    """向某人打招呼"""
    return f"{greeting}, {name}!"
```

### 2.2 模块导入

Python 通过 import 语句导入模块，支持多种导入方式。

## 第三章：面向对象编程

Python 是一门面向对象的语言，支持类和继承。

### 3.1 类的定义

类是对象的蓝图，定义了对象的属性和方法。

### 3.2 继承

继承允许子类复用父类的代码，是面向对象编程的核心概念之一。

## 第四章：异常处理

异常处理使程序能够优雅地处理错误情况，而不是直接崩溃。

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零")
finally:
    print("执行完毕")
```

## 总结

Python 是一门强大且易学的编程语言，适合从初学者到专业开发者的各类人群。掌握上述基础知识后，你可以进一步学习 Web 开发、数据分析、机器学习等方向。
