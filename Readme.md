# Partsegmentation Annotations

Generated annotations for [Virtual KITTI Dataset v1.3.1](https://europe.naverlabs.com/research/computer-vision/proxy-virtual-worlds-vkitti-1/) from my PhD thesis 'Camera-based 3D Vehicle Detection using Semantic Segmentation for Automated Driving' ("Kamerabasierte 3D-Fahrzeugerkennung mittels semantischer Segmentierung für das automatisierte Fahren").
In my work i separate a vehicle within a semantic segmentation into 29 fine-grained subclasses and use this output as an input to a modell-based pose estimation algorithm. As long as my thesis is not published please refer to the following papers.

[Fine-grained vehicle representations for autonomous driving](https://ieeexplore.ieee.org/abstract/document/8569930/)

[6DoF vehicle pose estimation using segmentation-based part correspondences](https://ieeexplore.ieee.org/abstract/document/8917012/)

## Format & Usage
The `dataset` folder holds the annotation for the partsegmentation in the original Virtual KITTI format (pngs). Please notice that the folder structure is based on the version 1.3.1.

Please refer to `example.py` for loading the data. Use `requirements.txt` to install required python packages via pip.




## About the used models
The used 3D CAD-models are not publicly available and need to be purchased. Yohann Cabon gave me the sources for most of the models:

Hatchback, SUV, Hybrid, Sedan4doors - [Polypixel3d](http://www.polypixel3d.com/portfolio/3d-model-cars-vehicle-pack-volume-one) / [Unity Assetstore](https://www.assetstore.unity3d.com/en/#!/content/32882)

Peugeot 207 - [Archive3d](http://archive3d.net/?a=download&id=964df051)

Renault Kangoo [Arhcive3d](http://www.archive3d.net/?a=download&id=a6a23d88)

Buses / Ambulance models - [Unity Assetstore](https://www.assetstore.unity3d.com/en/#!/content/16567) (not used by us)

Firetruck - [Archive3d](http://archive3d.net/?a=download&id=ae53751a) (not used by us)