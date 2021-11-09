# Sphinx 国际化

下面讨论 Sphinx 项目文档翻译为多语言的方法。

本文以 {github}`sphinx-doc/sphinx-intl` 转换为中英双语文档为例来说明实际的操作方法。

## 研究需要翻译的项目

研究需要翻译的项目的文档生成方法。

- fork {github}`sphinx-doc/sphinx-intl`，并克隆到本地，比如 {github}`daobook/sphinx-intl`。为了更好的管理项目，可以切换出一个新的分支，比如：`develop` 分支。

```sh
git checkout -b develop
```

- 需要配置 Sphinx 环境，即使用 PyPI 安装如下包：

```
sphinx
sphinx-rtd-theme
sphinx-intl
sphinxcontrib-websupport
```

- 进入文档目录，并生成 `.po` 文件：

```sh
cd doc
sphinx-build -b gettext ./ _build/gettext
sphinx-intl update -p _build/gettext -l zh_CN
```

- 翻译 `.po` 为目标语言（即你翻译后的语言），比如（这里被存放在 `locale/` 文件夹下）：

```po
#: ../../basic.rst:3
msgid "Basic"
msgstr ""
```

只需要将 `msgid` 的值翻译为 `msgstr` 的值，如 `zh_CN` 的 `基础`，即：

```po
#: ../../basic.rst:3
msgid "Basic"
msgstr "基础"
```

- 待翻译结束（由你决定），便需要将 `.po` 编译为 `.mo` 文件（其中 `zh-CN` 是目标语言的代号），同时输出最终的文档：

```sh
sphinx-build -D language=zh_CN -b html ./ _build/html/zh-CN
```

如若要保留英语原文，可以使用如下命令：

```sh
sphinx-build -D language=en -b html ./ _build/html
```

这样，`/docs/_build/html` 目录下存储了中英两个版本的内容。

## 完善翻译

我在 GitHub 创建了一个组织 {github}`sphinx-locales`。目的是为了提高翻译效率，可以将 `locale/` 文件夹上传，与他人协助翻译。

再回到项目 {github}`daobook/sphinx-intl`，把 `locale/` 放置在 {github}`sphinx-locales/sphinx-intl`，并使用 GitHub Action 令上述的翻译过程自动化。

首先，创建文件 {file}`requirements.txt`，用于配置该项目的 Sphinx 环境。

```sh
git clone git@github.com:sphinx-locales/sphinx-intl.git sphinx-intl-locale
cd sphinx-intl-locale
```
 
然后，将 {github}`daobook/sphinx-intl` 生成的 `locale/` 复制到 `sphinx-intl-locale/` 目录下，并改名为 `locales/`。

接着，创建文件 {file}`.github/workflows/deploy.yml` 用于部署自动化流程。

```{eval-rst}
.. code-block:: yaml
    :caption: daobook/sphinx-intl deploy.yml
    :name: sphinx-intl:deploy.yml
    :linenos:
    :emphasize-lines: 30,35,40,41,47

    name: deploy
    on:
    push:
        branches:
        - main

    jobs:
    # 这个工作流程包含一个名为 "build" 的 job
    build:
        # job 将运行的运行器的类型
        runs-on: ubuntu-latest

        # steps 将作为工作的一部分而执行的任务序列
        steps:
        # 这个动作在 $GITHUB_WORKSPACE 下签出你的版本库，以便工作流就可以访问它
        - uses: actions/checkout@v2
        # 设定 Python 环境
        - name: Set up Python
            uses: actions/setup-python@v2
            with:
            python-version: 3.9
        # 设定 conda 环境
        - uses: s-weigand/setup-conda@v1
        - run: conda --version
        - run: which python

        # 安装依赖包
        - name: Install dependencies
            run: |
            pip install -r requirements.txt
        
        # 克隆
        - name: Clone
            run: |
            git clone https://github.com/daobook/sphinx-intl.git draft

        # 构建 Sphinx 文档
        - name: Build the book
            run: |
            cp locales/ -rf draft/doc/locale/
            cd draft/doc
            sphinx-build -b gettext ./ _build/gettext
            sphinx-intl update -p _build/gettext -l zh_CN
            sphinx-build -D language=en -b html ./ _build/html/
            sphinx-build -D language=zh_CN -b html ./ _build/html/zh-CN
            cd ../..
            cp -rf draft/docs/_build/ _build
            rm -rf draft/

        # 部署 HTML 到 gh-pages 分支
        - name: GitHub Pages action
            uses: peaceiris/actions-gh-pages@v3.6.1
            with:
            github_token: ${{ secrets.GITHUB_TOKEN }}
            publish_dir: _build/html
            user_name: "github-actions[bot]"
            user_email: "github-actions[bot]@users.noreply.github.com"
```

最后，使用 Git 上传，便会自动化部署到 {sphinx-locales}`sphinx-intl` 预览效果。可以不断的修改，直到你觉得翻译的意思没有问题为止。

```{note}
对于 Jupyter Book 项目，需要做一些调整：

```yaml
- name: Build the book
  run: |
    cp locales/ -rf draft/doc/locale/
    cd draft/doc
    jb build --builder custom --custom-builder gettext --path-output _gettext .
    rm -rf _gettext/_build/.jupyter_cache/ _gettext/_build/jupyter_execute 
    sphinx-intl update -p _gettext/_build/gettext -l zh_CN
    jb build .
    ...
```

```{important}
高亮的部分是依据您的项目而定的。
```

## 更新源文档

如果 {github}`sphinx-doc/sphinx-intl` 文档有所改动，相应的 `locales/` 则需要更新。基于此，再次回到项目 {github}`daobook/sphinx-intl` 的 `develop` 分支下。

首先，{sphinx-locales}`sphinx-intl` 翻译的 `locales/` 覆盖 {github}`daobook/sphinx-intl` 的 `doc/locale`：

```sh
git clone https://github.com/sphinx-locales/sphinx-intl.git draft/
rm -rf doc/locale
cp -rf draft/locales/ doc/locale/
rm -rf draft
```

其次，进入文档目录，并生成 `.po` 文件：

```sh
cd doc
sphinx-build -b gettext ./ _build/gettext
sphinx-intl update -p _build/gettext -l zh_CN
```

最后，校队并翻译 `.po` 文件。觉得，翻译的差不多了，再次将其 `locale/` 文件夹替换掉 {sphinx-locales}`sphinx-intl` 的 `locales/` 文件夹。

## 贡献源文档

如若您需要对源文档，即 {github}`sphinx-doc/sphinx-intl` 的 `/docs/` 中的内容做出修改或者添加等贡献行为，则可以这样做。

首先，贡献源文档，并更新 {sphinx-locales}`sphinx-intl` 的 `locales/` 文件夹。
其次，创建 {github}`daobook/sphinx-intl` 的自动化流程 `.github/workflows/deploy.yml`：

```{eval-rst}
.. code-block:: yaml
    :linenos:
    :emphasize-lines: 5,10,15,17,23,24
    
    ...
      # 安装依赖包
      - name: Install dependencies
        run: |
          pip install -r doc/requirements.txt
      
      # 克隆
      - name: Clone
        run: |
          git clone https://github.com/sphinx-locales/sphinx-intl.git draft

      # 构建 Sphinx 文档
      - name: Build the book
        run: |
          cp -rf draft/locales/ doc/locale/
          rm -rf draft/
          cd doc
          sphinx-build -b gettext ./ _build/gettext
          sphinx-intl update -p _build/gettext -l zh_CN
          sphinx-build -D language=en -b html ./ _build/html/
          sphinx-build -D language=zh_CN -b html ./ _build/html/zh-CN
          cd ..
          cp -rf doc/_build/ _build/
          rm -rf doc/_build/
    ...
```

其中，`...` 部分，同 [](sphinx-intl:deploy.yml)。

```{important}
高亮的部分是依据您的项目而定的。
```

## 小技巧

VSCode 中 `po` 文件的高亮，可以使用 vscode 插件 [gettext](https://marketplace.visualstudio.com/items?itemName=mrorz.language-gettext)。