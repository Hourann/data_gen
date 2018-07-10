# data_gen
根据表达式造数据的命令行小工具

## 命令行选项：
- `--expr`: numpy表达式。已执行`from numpy import *`，对于numpy中的函数直接可以用。变量用`X`表示,`X`是一个numpy array,暂时只支持一维向量。例：`--expr=sum(X)`
- `--range`: 随机生成X的范围。默认为(-10,10)。例：`--range=(-100,200)`
- `--nline`: 指定生成多少组数据。默认为100
- `--nx`: 指定X的长度。默认为15
- `--sep`: 指定分隔符。默认为空格
- `--out`: 指定输出文件，默认为`out.txt`

## 依赖：
- numpy

## 例子：
- `./data_gen.py --range="(-100,200)" --expr="10*15*sum(X*X-10*cos(2*pi*X))"`
- `./data_gen.py --range="(-100,100)" --expr="sum((1-X[:-1])**2+100*(X[1:]-X[:-1]**2)**2)" --out=20.txt --sep=','`
