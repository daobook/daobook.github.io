# 数据集

* [nuScenes](https://www.nuscenes.org/) - 安波福于2019年3月公开了其数据集，并在[GitHub](https://github.com/nutonomy/nuscenes-devkit)公开教程。数据集拥有从波士顿和新加坡收集的1000个“场景”的信息，包含每个城市环境中都有的最复杂的一些驾驶场景。该数据集由140万张图像、39万次激光雷达扫描和140万个3D人工注释边界框组成，是迄今为止公布的最大的多模态3D AV数据集。
* [H3D - HRI-US](https://usa.honda-ri.com/hdd/introduction/h3d) - 本田研究所于2019年3月发布其无人驾驶方向数据集，相关介绍于[arXiv:1903.01568](https://arxiv.org/abs/1903.01568)介绍。本数据集使用3D LiDAR扫描仪收集的大型全环绕3D多目标检测和跟踪数据集。 其包含160个拥挤且高度互动的交通场景，在27,721帧中共有100万个标记实例。凭借独特的数据集大小，丰富的注释和复杂的场景，H3D聚集在一起，以激发对全环绕3D多目标检测和跟踪的研究。
* [ApolloCar3D] - 该数据集包含5,277个驾驶图像和超过60K的汽车实例，其中每辆汽车都配备了具有绝对模型尺寸和语义标记关键点的行业级3D CAD模型。该数据集比PASCAL3D +和KITTI（现有技术水平）大20倍以上。
* [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/raw_data.php) - 数据集为使用各种传感器模式，例如高分辨率彩色和灰度立体相机，Velodyne 3D激光扫描仪和高精度GPS/IMU惯性导航系统，在10-100 Hz下进行6小时拍摄的交通场景。
* [Cityscape Dataset](https://www.cityscapes-dataset.com/)  - 专注于对城市街景的语义理解。 大型数据集，包含从50个不同城市的街景中记录的各种立体视频序列，高质量的像素级注释为5000帧，另外还有一组较大的20000个弱注释帧。 因此，数据集比先前的类似尝试大一个数量级。 可以使用带注释的类的详细信息和注释示例。
* [Mapillary Vistas Dataset](https://www.mapillary.com/dataset/vistas?pKey=xyW6a0ZmrJtjLw2iJ71Oqg&lat=20&lng=0&z=1.5)-数据集是一个新颖的大规模街道级图像数据集，包含25,000个高分辨率图像，注释为66个对象类别，另有37个类别的特定于实例的标签。通过使用多边形来描绘单个对象，以精细和细粒度的样式执行注释。
* [CamVid](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/) -剑桥驾驶标签视频数据库（CamVid）是第一个具有对象类语义标签的视频集合，其中包含元数据。 数据库提供基础事实标签，将每个像素与32个语义类之一相关联。 该数据库解决了对实验数据的需求，以定量评估新兴算法。 虽然大多数视频都使用固定位置的闭路电视风格相机拍摄，但我们的数据是从驾驶汽车的角度拍摄的。 驾驶场景增加了观察对象类的数量和异质性。
* [Caltech数据集](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/) - 加州理工学院行人数据集包括大约10小时的640x480 30Hz视频，这些视频来自在城市环境中通过常规交通的车辆。 大约250,000个帧（137个近似分钟的长段）共有350,000个边界框和2300个独特的行人被注释。 注释包括边界框和详细遮挡标签之间的时间对应。 更多信息可以在我们的PAMI 2012和CVPR 2009基准测试文件中找到。
* [Comma.ai](https://archive.org/details/comma-dataset) - 7.25小时的高速公路驾驶。 包含10个可变大小的视频片段，以20 Hz的频率录制，相机安装在Acura ILX 2016的挡风玻璃上。与视频平行，还记录了一些测量值，如汽车的速度、加速度、转向角、GPS坐标，陀螺仪角度。 这些测量结果转换为均匀的100 Hz时基。
* [Oxford's Robotic Car](http://robotcar-dataset.robots.ox.ac.uk/) - 超过100次重复对英国牛津的路线进行一年多采集拍摄。 该数据集捕获了许多不同的天气，交通和行人组合，以及建筑和道路工程等长期变化。
* [伯克利BDD100K数据](https://bdd-data.berkeley.edu/) - 超过100K的视频和各种注释组成，包括图像级别标记，对象边界框，可行驶区域，车道标记和全帧实例分割，该数据集具有地理，环境和天气多样性
* [Udacity](https://github.com/udacity/self-driving-car/tree/master/datasets) - 为[Udacity Challenges](https://www.udacity.com/self-driving-car)发布的Udacity数据集。 包含ROSBAG训练数据。 （大约80 GB）。
* [University of Michigan North Campus Long-Term Vision and LIDAR Dataset](http://robots.engin.umich.edu/nclt/) -  包括全方位图像，3D激光雷达，平面激光雷达，GPS和本体感应传感器，用于使用Segway机器人收集的测距。
* [University of Michigan Ford Campus Vision and Lidar Data Set](http://robots.engin.umich.edu/SoftwareData/Ford)  - 基于改进的福特F-250皮卡车的自动地面车辆测试台收集的数据集。 该车配备了专业（Applanix POS LV）和消费者（Xsens MTI-G）惯性测量单元（IMU），Velodyne 3D激光雷达扫描仪，两个推扫式前视Riegl激光雷达和Point Grey Ladybug3全方位摄像头 系统。
* [DIPLECS Autonomous Driving Datasets (2015)](http://cvssp.org/data/diplecs/)  - 通过在Surrey乡村周围驾驶的汽车中放置高清摄像头来记录数据集。 该数据集包含大约30分钟的驾驶时间。 视频为1920x1080，采用H.264编解码器编码。 通过跟踪方向盘上的标记来估计转向。 汽车的速度是从汽车的速度表OCR估算的（但不保证方法的准确性）。
* [Velodyne SLAM Dataset from Karlsruhe Institute of Technology](http://www.mrt.kit.edu/z/publ/download/velodyneslam/dataset.html)  - 在德国卡尔斯鲁厄市使用Velodyne HDL64E-S2扫描仪记录的两个具有挑战性的数据集。
* [SYNTHetic collection of Imagery and Annotations (SYNTHIA)](http://synthia-dataset.net/)  - 包括从虚拟城市渲染的照片般逼真的帧集合，并为13个类别提供精确的像素级语义注释：misc，天空，建筑，道路，人行道，围栏，植被，杆，汽车，标志，行人， 骑自行车的人，车道标记。
* [CSSAD Dataset](http://aplicaciones.cimat.mx/Personal/jbhayet/ccsad-dataset)  - 包括若干真实世界的立体数据集，用于在自动驾驶车辆的感知和导航领域中开发和测试算法。 然而，它们都没有记录在发展中国家，因此它们缺乏在街道和道路上可以找到的特殊特征，如丰富的坑洼，减速器和特殊的行人流。 该立体数据集是从移动的车辆记录的，并且包含高分辨率立体图像，其补充有从IMU，GPS数据和来自汽车计算机的数据获得的定向和加速度数据。
* [Daimler Urban Segmetation Dataset](http://www.6d-vision.com/scene-labeling)  - 包括城市交通中记录的视频序列。 该数据集由5000个经过校正的立体图像对组成，分辨率为1024x440。 500帧（序列的每10帧）带有5个类的像素级语义类注释：地面，建筑，车辆，行人，天空。 提供密集视差图作为参考，但是这些不是手动注释的，而是使用半全局匹配（sgm）计算的。
* [Self Racing Cars - XSens/Fairchild Dataset](http://data.selfracingcars.com/)  - 文件包括来自Fairchild FIS1100 6自由度（DoF）IMU，Fairchild FMT-1030 AHRS，Xsens MTi-3 AHRS和Xsens MTi-G-710 GNSS / INS的测量结果。 事件中的文件都可以在MT Manager软件中读取，该软件可作为MT软件套件的一部分提供，可在此处获得。
* [MIT AGE Lab](http://lexfridman.com/automated-synchronization-of-driving-data-video-audio-telemetry-accelerometer/)  -  由AgeLab收集的1,000多小时多传感器驾驶数据集的一小部分样本。
* [LaRA](http://www.lara.prd.fr/lara) -巴黎的交通信号灯数据集
* [KUL Belgium Traffic Sign Dataset](http://www.vision.ee.ethz.ch/~timofter/traffic_signs/)  - 具有10000多个交通标志注释的大型数据集，数千个物理上不同的交通标志。 用8个高分辨率摄像头录制的4个视频序列安装在一辆面包车上，总计超过3个小时，带有交通标志注释，摄像机校准和姿势。 大约16000张背景图片。 这些材料通过GeoAutomation在比利时，佛兰德斯地区的城市环境中捕获。
* [博世小交通灯](https://hci.iwr.uni-heidelberg.de/node/6132) - 用于深度学习的小型交通灯的数据集。
* [LISA: Laboratory for Intelligent & Safe Automobiles, UC San Diego Datasets](http://cvrr.ucsd.edu/LISA/datasets.html)  - 交通标志，车辆检测，交通灯，轨迹模式。
* [Multisensory Omni-directional Long-term Place Recognition (MOLP) dataset for autonomous driving](http://hcr.mines.edu/code/MOLP.html) - 它是在美国科罗拉多州的一年内使用全向立体相机录制的。[论文](https://arxiv.org/abs/1704.05215)
* [DeepTesla](https://selfdrivingcars.mit.edu/deeptesla/) - 主要包括tesla在两种不同驾驶模式（human driving和autopilot）下的前置相机录制的视频和车辆的转向控制信号。数据可以从这里下载:[百度云](https://pan.baidu.com/s/1c2J2IFA#list/path=%2F)。可以参考此[GitHub](https://github.com/CJHMPower/deep-tesla)

