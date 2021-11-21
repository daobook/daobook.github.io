# CPython

{guilabel}`预览`：{daobook}`cpython`

在 {github}`daobook/cpython` 的 `xin` 分支维护了 {github}`python/cpython`/`3.10` 的中文版本。

基于 Sphinx4.x 构建中文文档。支持自动部署到 `gh-pages`。

## `xin` 分支的生成

`xin` 分支的生成过程：

首先，基于分支 `main`，直接使用 `sphinx-quickstart` 生成 `make.bat` 于 Windows 平台使用（原来的 `make.bat` 重命名为 `make-old.bat`）。

接着，在 `conf.py` 中添加如下内容，以支持 `zh_CN`：

```python
# sphinx-intl & zh_CN
language = 'zh_CN'
locale_dirs = ['../locales/']
gettext_compact = False
```

接着，引入 {github}`daobook/python-docs-zh-cn` 的 `xin` 分支的中文 `.po` 文件：

```shell
git clone https://github.com/daobook/python-docs-zh-cn.git locales/zh_CN/LC_MESSAGES/
rm -rf locales/zh_CN/LC_MESSAGES/.git

```

然后，生成 `.pot` 文件，并更新 `.po` 文件：

```shell
cd Doc
make gettext
sphinx-intl update -p build/gettext -l zh_CN
```

最后，生成 HTML 文档，便可以预览了：

```shell
make html
```

## 变更

- 于 2021/11/08 引入 {github}`python/python-docs-zh-cn` 的 `3.10` 分支的中文 `po` 文件。
- 更新 `library/language.po`、 `library/ast.po`。（2021/11/21）