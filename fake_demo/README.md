#### 结果

![image](https://user-images.githubusercontent.com/58416451/112970732-17bcf400-9181-11eb-9bcf-1b86eadd115e.png)

#### 打包

```
pip install -r requirments.txt
pyinstaller -F -w .\main.py


```

#### 问题

```
PS C:\Users\faces\Desktop\fake_demo\dist> .\main.exe
Traceback (most recent call last):
  File "auto.py", line 17, in <module>
  File "site-packages\gooey-1.0.3-py3.7.egg\gooey\python_bindings\gooey_decorator.py", line 87, in inner2
  File "auto.py", line 12, in main
  File "site-packages\gooey-1.0.3-py3.7.egg\gooey\python_bindings\gooey_parser.py", line 114, in parse_args
  File "site-packages\gooey-1.0.3-py3.7.egg\gooey\python_bindings\gooey_decorator.py", line 82, in run_gooey
  File "site-packages\gooey-1.0.3-py3.7.egg\gooey\gui\application.py", line 21, in run
  File "site-packages\gooey-1.0.3-py3.7.egg\gooey\gui\application.py", line 28, in build_app
  File "site-packages\gooey-1.0.3-py3.7.egg\gooey\gui\lang\i18n.py", line 24, in load
  File "json\__init__.py", line 293, in load
UnicodeDecodeError: 'gbk' codec can't decode byte 0xa7 in position 20: illegal multibyte sequence
```

#### 解决方案

从报错信息中可以看到是因为load代码的时候使用encoding='cp936'去加载文件导致的错误，那么简单粗暴的方法是编辑`site-packages\gooey-1.0.3-py3.7.egg\gooey\gui\lang\i18n.py`这个文件

找到
```python
    with io.open(os.path.join(language_dir, json_file), 'r', encoding=encoding) as f:
      _DICTIONARY = json.load(f)
```
修改为
```python
    with io.open(os.path.join(language_dir, json_file), 'r', encoding='utf-8') as f:
      _DICTIONARY = json.load(f)
```

