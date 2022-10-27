由于angr对于z3等库有重写所以官方文档建议安装在虚拟环境中。

虚拟环境建立：

``` powershell
pip install virtualenv
pip install virtualenvwrapper-win
```

安装完成后使用workon命令查看当前存在的虚拟环境：

![image-20221027111441294](C:\Users\xyyy\AppData\Roaming\Typora\typora-user-images\image-20221027111441294.png)

新建虚拟环境

```powershell
mkvirtualenv 'env_name'
```

默认虚拟环境创建在用户目录下，需要自定义环境变量：

![image-20221027111727292](C:\Users\xyyy\AppData\Roaming\Typora\typora-user-images\image-20221027111727292.png)

进入虚拟环境，安装angr：

```powershell
workon angr
pip install angr
```

这里有一个非常有意思的问题：在powershell中使用workon命令无法进入虚拟环境，需要使用cmd，找到相关问题的答案：

[Powershell无法使用workon打开虚拟环境 - LiMings - 博客园 (cnblogs.com)](https://www.cnblogs.com/LiMings/articles/15164359.html)

![image-20221027111944835](C:\Users\xyyy\AppData\Roaming\Typora\typora-user-images\image-20221027111944835.png)

进入虚拟环境后如上图显示，输入

```python
import sys
sys.path
```

可以看到相关的库并不会使用原生python的那些库即代表当前在虚拟环境

