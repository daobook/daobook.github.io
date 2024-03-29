# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import ablog

if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'daobook'
copyright = '2021, xinetzone'
author = 'xinetzone'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_book_theme",
    "ablog",
    "myst_nb",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_thebe",
    "sphinx_copybutton",
    "sphinx_comments",
    "sphinx_panels",
    "sphinx_inline_tabs",
    # "sphinx.ext.todo",
    # "sphinxcontrib.bibtex",
    # "sphinx_togglebutton",
    # "sphinx.ext.viewcode",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.doctest",
    # "sphinx_design",
    # "sphinx.ext.ifconfig",
    # "sphinx_automodapi.automodapi",
    # "sphinxext.opengraph",
]

myst_enable_extensions = [
    "colon_fence",
    "amsmath",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    # "linkify",
    # "replacements",
    # "smartquotes",
    # "substitution",
    # "tasklist",
]

comments_config = {
    "hypothesis": True,
    "dokieli": False,
    "utterances": {
        "repo": "daobook/daobook.github.io",
        "optional": "config",
    }
}

# MyST NB 设置
nb_mime_priority_overrides = [
    ("html", "text/html", 0),
    ("latex", "text/latex", 20),
    ("html", "application/vnd.plotly.v1+json", 10),
    # ("image", "image/svg+xml", None)
    # (
    #     "application/vnd.jupyter.widget-view+json",
    #     "application/javascript",
    #     "text/html",
    #     "image/svg+xml",
    #     "image/png",
    #     "image/jpeg",
    #     "text/markdown",
    #     "text/latex",
    #     "text/plain",
    # ), 0)
]

# 如果你希望stderr和stdout中的每个输出都被合并成一个流，请使用以下配置。
# 避免将 jupter 执行报错的信息输出到 cmd 
nb_merge_streams = True
execution_allow_errors = True

extlinks = {
    # 'duref': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #           'restructuredtext.html#%s', ''),
    # 'durole': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #            'roles.html#%s', ''),
    # 'dudir': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #           'directives.html#%s', ''),
    'github': ('https://github.com/%s', ''),
    'daobook': ('https://daobook.github.io/%s', ''),
    'sphinx-locales': ('https://sphinx-locales.github.io/%s', ''),
    'ablog': ('https://daobook.github.io/ablog/zh-CN/%s', ''),
    'docutils': ('https://daobook.github.io/docutils/%s', '')
}

intersphinx_mapping = {
    'python': ('https://daobook.github.io/cpython', None),
    'sphinx': ('https://daobook.github.io/sphinx', None),
    'peps': ('https://daobook.github.io/peps', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', ablog.get_html_templates_path()]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["default.css"]

# -- 国际化输出 ----------------------------------------------------------------

locale_dirs = ['../locales/']  # path is example but recommended.
gettext_compact = False  # optional.
epub_show_urls = 'footnote'
# -- 主题设置 -------------------------------------------------------------------

# 定制主侧栏
html_sidebars = {
    "*": [
        # 显示标志和网站标题。
        "sidebar-logo.html",
        #一个基于 bootstrap 的搜索栏（来自 PyData Sphinx Theme）
        "search-field.html",
        # 一个用于你的书基于 bootstrap 的导航菜单。
        "sbt-sidebar-nav.html"
    ],
    "posts/**": [
        "postcard.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
    ],
}

extra_navbar = """<p>
    版权所有 © 2021
    <a href="https://daobook.github.io/">Dao Book</a>
</p>
<p>
    由 <a href="https://ebp.jupyterbook.org/">EBP</a> 
    提供技术支持
</p>
"""

html_theme_options = {
    "path_to_docs": "doc/",
    "repository_url": "https://github.com/daobook/daobook.github.io",
    "repository_branch": "main",
    "use_issues_button": True,
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": True,
    "use_repository_button": True,
    "home_page_in_toc": False,
    "extra_navbar": extra_navbar,
    "toc_title": "导航",
    "launch_buttons": {
        # https://mybinder.org/v2/gh/daobook/daobook.github.io/main
        "binderhub_url": "https://mybinder.org",
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
        "colab_url": "https://colab.research.google.com/",
        # 你可以控制有人点击启动按钮时打开的界面。
        "notebook_interface": "jupyterlab",
        "thebe": True,  # Thebe 实时代码单元格
    },
}

# -- 自定义网站的标志 --------------
html_logo = 'logo.jpg'
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.png"

# -- 自定义网站的标题 --------------
# html_title = '动手学习 Python'

# ========== ABlog 配置 ============================================================
blog_path = "posts"
blog_post_pattern = "posts/*.md"
blog_baseurl = "https://daobook.github.io"
fontawesome_included = True
post_auto_image = 1
post_auto_excerpt = 2
bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "author_year"
# --    博客作者、语言和位置 -------------------------------------------------

# 一个作者名字的字典，映射到作者的完整显示名称和链接。
# 字典的键值应该在 ``post`` 指令中使用，以指代作者。默认是 ``{}``。
blog_authors = {
    "lxw": ("刘新伟", None),
}

# 语言代码名称的字典，映射到这些语言的完整显示名称和链接。
# 类似于 :confval:`blog_authors`，
# 字典的键应该在 `post` 指令中使用，以指代位置。默认是 `{}`。
blog_languages = {'zh': ('Chinese', None), 'en': ('English', None)}

# 默认作者的名字
blog_default_author = "lxw"
# 默认语言的代码名称
blog_default_language = 'zh'
# 在 blog_locations 中定义的默认位置的名称。
# blog_default_location = None

# -- 博客帖子相关 --------------------------------------------------------

# 帖子的日期格式。默认 ``'%b %d, %Y'``
#  ``datetime.date.strftime()`` 的参数
post_date_format = '%c'
post_date_format_short = '%b %d, %Y'

# todo_include_todos = True

def setup(app):
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    app.add_object_type('setuptools-confval', 'setuptools-confval',
                        objname='setuptools configuration value',
                        indextemplate='pair: %s; setuptools configuration value')