# Python

```{toctree}
:glob:

*
```

如果需要在 Ubuntu20.04 安装 Pandoc，可以：

```yaml
- name: install pandoc
    uses: r-lib/actions/setup-pandoc@v1
    with:
        pandoc-version: '2.6'
```