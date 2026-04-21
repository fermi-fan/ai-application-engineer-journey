# <h1 align="center">Python编程从入门到实践</h1>

## Chapter 01 起步

这一章讲不同操作系统有的python编程环境配置

## Chapter 02 变量和简单的数据类型

### 变量
什么是变量？  ---> 变量是存储数据值的容器

变量的命名规则：Python 变量名要由字母、数字、下划线组成，不能以数字开头，不能用关键字；实际编写时最好做到见名知意，并使用小写加下划线的命名方式。


### 字符串
字符串是一系列字符，在python中所有用引号引起的都是字符串，其中的引号可以是单引号也可以是双引号。

```py
# 将字符串的首字母大写
name = "he qian"
print(name.title())

# 将所有字符大写
print(name.upper())

# 将所有字符小写
print(name.lower())
```
以上方法不会改变原来字符串的内容。

### 在字符串中使用变量

```py
first_name = "qian"
last_name = "he"
full_name = f"{first_name} {last_name}"
print(full_name)
```

### 使用制表符或换行符来添加空白
目的是组织输出，让用户阅读起来更容易

```py
print("Languages:\n\tPython\n\tC\n\tJavascript")
```

### 删除空白

```py
favorite_language = ' python c '
# 删除右边空白
print(favorite_language.rstrip())
# 删除左边空白
print(favorite_language.lstrip())
# 删除两端空白
print(favorite_language.strip())
```

