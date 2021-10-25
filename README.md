# Sound-Shaper
it's a Python Project which you can manipualte wave as you wish! 

本工程允许用户拖拽一个波形，生成想要的外观，并将这个波形播放出来

**使用`pip install -r requirements.txt`安装工程所需要的依赖**
  
## Point.py

负责管理曲线控制点组件，其中Pointdata类负责控制最终的控制点

## BSpling.py

负责由控制点生成B样条曲线（准均匀）

## mysound.py

负责处理一切有关音频的服务


