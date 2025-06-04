## 2024-06-13 修改记录

- 优化浏览器跳转行为：同域跳转复用当前tab，跨域跳转自动新建tab。
  - 修改文件：venv/lib/python3.13/site-packages/browser_use/browser/context.py
    - navigate_to方法中，增加了同域/跨域判断逻辑：
      - 同域：page.goto(url)
      - 跨域：create_new_tab(url)
