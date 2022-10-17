# packaging.python.org

{guilabel}`预览`：{daobook}`packaging.python.org`

{daobook}`#` 工作是：

- {github}`daobook/packaging.python.org`：fork 项目 {github}`pradyunsg/packaging.python.org`，并基于 `main` 切出分支 `xin` 用于中国化；同时部署到 `gh-pages` 分支。

## 关于部署的思考

软件包的存在是为了安装（或 部署），所以在你包装任何东西之前，你要对下面的部署问题有一些答案：

- 谁是你的软件的用户？你的软件是否会被其他从事软件开发的开发人员、数据中心的操作人员或不太懂软件的群体安装？
- 你的软件是要在服务器、桌面、移动客户端（手机、平板电脑等）上运行，还是嵌入到专用设备中？
- 你的软件是单独安装，还是成批部署？