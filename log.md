## 2024-06-13 修改记录

- 新增：关闭浏览器时自动终结运行中的agent任务。
  - 修改文件：src/webui/components/browser_settings_tab.py
    - 在close_browser函数中，增加了如下逻辑：
      - 如果有正在运行的agent任务（bu_current_task），则调用bu_agent.stop()方法终止agent任务，并确保bu_current_task被取消。
      - 这样可以保证关闭浏览器时，相关agent任务也会被终止。
