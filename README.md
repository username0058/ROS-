# ROS-
1，img_pub.py与img_sub.py是最终选拔任务要求完成的两个Python文件，img_sub.py中使用的white_balance函数引用自网上他人整理的代码，执行这个函数可以一定程度上减少阴影影响，但是实际运行过程中
仍然会出现误差，代码中hsv的颜色范围还需要随环境光调整才能减少误差。
经测试可以在rqt_image_view中展示处理后的实时效果视频（有时还有少部分误差的框选，以后还需要优化，另外这是当时环境的调节结果）
2，用imshow展示的处理效果图：![BAHNF_KKQX VB{@TZSHOB{I](https://user-images.githubusercontent.com/119773558/215322934-4e4d8a16-d152-459b-abfb-f0c99d3932d1.png)
（实在没什么红的了就拿了个红色挂坠挂窗户上）
3，src文件中存储的cpp文件为网上拷贝的调用摄像头的代码，不是C++的复写文件，因为还太菜了，C++的语法规则大体了解，但是面向对象编程等操作依然没学到，尝试在这里写起来发现很困难。开学后我会进一步系统学习
C++，争取继续提高代码能力（记性太差了假期学的这些也还需要复习呜呜呜...）（我们大类今年突然删除了以前每届应该学习的C++课，估计以后全校就剩我们大类不教编程了，这些只能先自学）
4，imgpub.py与imgsub.py是网上的参考代码，我自己调试摄像头时候用的，编写另外两个作业.py文件过程中受到了古月居老师和这些资料和代码的启发。
5，感谢各位学长在假期一直以来对我的帮助，让我新学到了挺多东西（例如opencv和python的简单应用，linux系统的简单操作，git的简单使用······），今后我会继续巩固复习假期所学，下一步打算是巩固
python语法，详细学习C++的编写操作，照着git的课程学到更多git的用法，学习了解更多ros的实际应用等等。
6,一些今后还要解决的问题：rosrun uvb_camera uvb_camera_node这句命令似乎不存在，类似的sudo apt-get install ros-neotic-image-*以及sudo apt-get install ros-neotic-rqt-image-view这些命令也无法在ros-neotic中运行，还没查到解决办法，这里用自写代码和rqt_image可视化模块却可以直接查看摄像头，试用rviz不成功。
