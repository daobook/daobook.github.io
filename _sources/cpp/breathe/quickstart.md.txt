# 快速上手

- 安装 `breathe`；
- 安装 `doxygen`，并且为要记录的项目生成了 `doxygen` 输出（XML 格式，注意，输出文件夹应包含 index.xml 由 doxygen 生成的输出文件。）（将 `GENERATE_XML` 标签设为 `YES`），假设输出为 `xml/`；
- 使用 `sphinx-quickstart` 创建的文档，并将 `breathe` 添加到 {confval}`extensions` 列表中。
- 告诉 `breathe` 关于项目的信息：

```python
breathe_projects = { "myproject": "xml/" }
```

- 指定默认的项目：

```python
breathe_default_project = "myproject"
```

一旦完成这些工作，你可以使用以下命令：

```rst
.. doxygenindex::
.. doxygenfunction::
.. doxygenstruct::
.. doxygenenum::
.. doxygentypedef::
.. doxygenclass::
```

以包括不同结构的文档。对于这些命令中的每一条，都可以指定以下指令：

`project`
:   指定哪个项目，如 `breathe_projects` 配置值中定义的，应该用于该指令。这取代了默认值。

`path`
:   直接指定到有 `doxygen` 输出的文件夹的路径。这覆盖了 `project` 和 `default project`。