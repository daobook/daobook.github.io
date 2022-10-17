# SOTA代码

## 物体检测|Object Detection  
* `Stereo R-CNN` [HKUST-Aerial-Robotics/Stereo-RCNN](https://github.com/HKUST-Aerial-Robotics/Stereo-RCNN)  - `CVPR2019`   
研究机构 : 港科大Aerial Robotics Group和大疆  
论文 : [Stereo R-CNN based 3D Object Detection for Autonomous Driving](https://arxiv.org/abs/1902.09738)
* `SimpleDet`[tusimple/simpledet](https://github.com/tusimple/simpledet) - `SOTA on consumer grade hardware at large scale`   
研究机构 : 图森  
论文 : [SimpleDet: A Simple and Versatile Distributed Framework for Object Detection and Instance Recognition](https://arxiv.org/abs/1903.05831)      
* `PointPillars` [traveller59/second.pytorch](https://github.com/traveller59/second.pytorch) -`SOTA for Birds Eye View Object Detection on KITTI Cyclists Moderate`   
研究机构 : nuTonomy（安波福下的公司）  
论文 : [PointPillars: Fast Encoders for Object Detection from Point Clouds](https://arxiv.org/abs/1812.05784),
* `PointRCNN`[sshaoshuai/PointRCNN](https://github.com/sshaoshuai/PointRCNN) -
`KITTI for 3D Object Detection (Cars)` : #2,Cars-Easy(AP:84.32%); #1,Cars-Moderate(AP:75.42%); #1,Cars-Hard(AP:67.86%)   
研究机构 : 香港中文大学  
论文 : [PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud](https://arxiv.org/abs/1812.04244)
* [sshkhr/BigDataCup18_Submission](https://github.com/sshkhr/BigDataCup18_Submission) -
IEEE International Conference On Big Data Cup 2018(2018年IEEE国际大数据杯会议的道路损伤检测和分类挑战),   
研究机构 :  印度科学研究所   
论文 : [Road Damage Detection And Classification In Smartphone Captured Images Using Mask R-CNN](https://arxiv.org/abs/1811.04535)
* `Complex-YOLO`[AI-liu/Complex-YOLO](https://github.com/AI-liu/Complex-YOLO) -  
研究机构 : 法里奥、伊尔默瑙理工大学  
论文:[Complex-YOLO: Real-time 3D Object Detection on Point Clouds](https://arxiv.org/abs/1803.06199)
* [kujason/avod](https://github.com/kujason/avod) -`KITTI 3D Object Detection for cars`#2 Cars-Hard(AP:66.38%)   
研究机构 : 滑铁卢大学工程学院机械与机电工程系    
论文 : [Joint 3D Proposal Generation and Object Detection from View Aggregation](https://arxiv.org/abs/1712.02294)  
* `PointNet`[charlesq34/pointnet](https://github.com/charlesq34/pointnet)- 
`SOTA（Object Localization & 3D Object Detection）` :Cars、Cyclists、Pedestrian   
研究机构 : 斯坦福大学、Nuro公司、加州大学圣地亚哥分校     
论文 : [Frustum PointNets for 3D Object Detection from RGB-D Data](https://arxiv.org/abs/1711.08488)
* `SqueezeDet`[BichenWuUCB/squeezeDet](https://github.com/BichenWuUCB/squeezeDet) -`SOTA for KITTI(2016)`  
研究机构 : 伯克利、[DeepScale](http://deepscale.ai/)（专注于自动驾驶感知技术）         
论文 : [SqueezeDet: Unified, Small, Low Power Fully Convolutional Neural Networks for Real-Time Object Detection for Autonomous Driving](https://arxiv.org/abs/1612.01051) 
* `VoxelNet`[charlesq34/pointnet](https://github.com/charlesq34/pointnet) - 
`SOTA（Object Localization & 3D Object Detection）`:Cars、Cyclists、Pedestrian  
研究机构 : 苹果公司    
论文 : [VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection](https://arxiv.org/abs/1711.06396)  

## 分割|Segmentation

* `LEDNet`[xiaoyufenfei/LEDNet](https://github.com/xiaoyufenfei/LEDNet) - 暂未released，Semantic Segmentation: `Real-time(71FPS)`、Semantic Segmentation(Mean IoU 70.6%)，ICIP 2019  
研究机构 : 南京邮电大学、天普大学   
论文 : [LEDNet: A Lightweight Encoder-Decoder Network for Real-Time Semantic Segmentation](https://arxiv.org/abs/1905.02423)，
* `swiftnet`[orsic/swiftnet](https://github.com/orsic/swiftnet) - 
Real-Time Semantic Segmentation on Cityscapes #9,Semantic Segmentation(Mean IoU:75.5%);#2,`Real-time(Mean IoU:75.5%)`;#3,`Real-time(Frame:39.9 fps)`,`CVPR2019`   
研究机构 : 萨格勒布大学 电气工程与计算学院   
论文 : [In Defense of Pre-trained ImageNet Architectures for Real-time Semantic Segmentation of Road-driving Images](https://arxiv.org/abs/1903.08469) 
* [YangZhang4065/AdaptationSeg](https://github.com/YangZhang4065/AdaptationSeg) - SOTA for `Image-to-Image Translation` on SYNTHIA-to-Cityscapes  
研究机构 :  IEEE Member  
论文 : [A Curriculum Domain Adaptation Approach to the Semantic Segmentation of Urban Scenes](https://arxiv.org/abs/1812.09953)
* `BiSeNet`[ycszen/TorchSeg](https://github.com/ycszen/TorchSeg) -
Cityscapes：#2，Real-time（`Frame:65.5 Fps`）;#8 (`Mean IoU 78.9%`)、CamVid：#2，Mean IoU 68.7%;ECCV 2018  
研究机构 : 多谱信息处理技术国家级重点实验室、华中科技大学自动化学院、北大、旷视  
论文 : [BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation](https://arxiv.org/abs/1808.00897)
* [MSiam/TFSegmentation](https://github.com/MSiam/TFSegmentation) - 
Benchmarking Framework（Cityscapes dataset for urban scenes）      
研究机构 : 阿尔伯塔大学、开罗大学    
论文 : [RTSeg: Real-time Semantic Segmentation Comparative Study](https://arxiv.org/abs/1803.02758)
* `MultiNet`[MarvinTeichmann/MultiNet](https://github.com/MarvinTeichmann/MultiNet) -  SOTA for KITTI(Road Segmentation)  
研究机构 : 多伦多大学计算机科学、剑桥大学工程系、[FZI研究中心](https://www.fzi.de/en/about-us/)、Uber ATG   
论文 : [MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving](https://arxiv.org/abs/1612.07695)  
* [bermanmaxim/LovaszSoftmax](https://github.com/bermanmaxim/LovaszSoftmax) - Cityscapes:#1 for `Real-Time（76.9 fps）`、#16 for Mean IoU(63.06%),`CVPR 2018`   
研究机构 : 鲁汶大学  
论文 : [The Lovász-Softmax loss: A tractable surrogate for the optimization of the intersection-over-union measure in neural networks](https://arxiv.org/abs/1705.08790),
* [BichenWuUCB/SqueezeSeg](https://github.com/BichenWuUCB/SqueezeSeg) -  
研究机构 : 伯克利      
论文 : [SqueezeSeg: Convolutional Neural Nets with Recurrent CRF for Real-Time Road-Object Segmentation from 3D LiDAR Point Cloud](https://arxiv.org/abs/1710.07368),  
* `PSPNet`[tensorflow/models](https://github.com/tensorflow/models/tree/master/research/deeplab)和[hszhao/PSPNet](https://github.com/hszhao/PSPNet) - `SOTA in (Semantic Segmentation & Real-Time Semantic Segmentation)`，[more detail](https://paperswithcode.com/paper/pyramid-scene-parsing-network),`CVPR 2017`   
研究机构 : 香港中文大学、商汤    
论文 : [Pyramid Scene Parsing Network](https://arxiv.org/abs/1612.01105)   

## 传感器融合|Sensor Fusion  

* [HKUST-Aerial-Robotics/VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) - SOTA，IROS 2018,IMU和（单目）摄像头融合的校正方法，用来校准IMU和相机之间的时间偏移。  
研究机构 : [港科大Aerial Robotics Group](http://uav.ust.hk/)  
论文 : [Online Temporal Calibration for Monocular Visual-Inertial Systems](https://arxiv.org/abs/1808.00692),

## 决策系统|Decision Making

* [xinleipan/VirtualtoReal-RL](https://github.com/xinleipan/VirtualtoReal-RL) -在虚拟环境通过强化学习来训练无人驾驶   
研究机构 : Berkley、清华大学、上海交通大学  
论文 : [Virtual to Real Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/1704.03952)
* [非官方][marsauto/europilot](https://github.com/marsauto/europilot)和[非官方][SullyChen/Autopilot-TensorFlow](https://github.com/SullyChen/Autopilot-TensorFlow)   
研究机构 : 英伟达  
论文 : [End to End Learning for Self-Driving Cars](https://arxiv.org/abs/1604.07316)  

## 运动规划|Motion Planer
* [非官方][Iftimie/ChauffeurNet](https://github.com/Iftimie/ChauffeurNet) -  Waymo出品，通过模仿学习对无人车进行运动规划，全文中文翻译:[知乎|每周一篇 & 无人驾驶](https://zhuanlan.zhihu.com/p/57275593)  
研究机构 : Waymo Research  
论文 : [ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst](https://arxiv.org/abs/1812.03079),

