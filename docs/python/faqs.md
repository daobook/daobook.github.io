# 常见问题

## 解决 Window 平台下对 `tornado` 的支持问题

警告信息：

```{warning}
**\lib\site-packages\zmq\_future.py:591: RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq. Registering an additional selector thread for add_reader support via tornado. Use `asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())` to avoid this warning.
  self._get_loop()
```

:::{tab} 解决策略（从根源）
在 `Lib/site-packages/tornado/platform/asyncio.py` 中添加：

```python
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
:::

:::{tab} 修改配置文件
如果不想修改环境内的包，可以在你的应用的主程序或者配置文件（例如 Sphinx 项目的 `conf.py` 中）中添加如下代码：

```python
import sys

if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
:::