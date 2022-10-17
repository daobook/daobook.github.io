---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: python 3
  language: python
  name: python3
---

# 在你的markdown文件中执行代码

如果你想在这些 markdown 文件中加入计算内容。你可以使用 MyST Markdown 来定义单元，这些单元将在你的书构建时执行。Jupyter Book 使用 *jupytext* 来做这个。

首先，向文件添加 Jupytext 元数据。例如，要将 Jupytext 元数据添加到这个 markdown 页面，运行这个命令：

```sh
jupyter-book myst init markdown.md
```

一旦一个 markdown 文件中包含了 Jupytext 元数据，你就可以在构建时添加以下指令来运行该代码：

````
```{code-cell}
print("Here is some code to execute")
```
````

```{code-cell}
print("Here is some code to execute")
```

当你的书被构建时，任何 `{code-cell}` 块的内容都会被你的默认 Jupyter 内核执行，其输出将与你的其他内容一起显示。

关于用 Jupyter Book 执行计算内容的更多信息。见 [MyST-NB文档](https://myst-nb.readthedocs.io/)。
