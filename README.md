# MNIST Model Training

![Build Status](https://github.com/deepanshudashora/MNIST_github_actions/actions/workflows/python-app.yml/badge.svg)

- [Problem Statement](#Problem-Statement)
- [File Structure](#File-Structure)
- [Model Parameters](#Model-Parameters)
- [Training Logs](#Training-Logs)
- [Results](#Results)
  * [Accuracy Plot](#Accuracy-Plot)
  * [Sample Output](#Sample-Output)
  * [Misclassified Images](#Misclassified-Images)
  * [Accuracy Report for Each class](#Accuracy-Report-for-Each-class)

# Problem Statement
Training a CNN model on MNIST dataset with GitHub Actions integration for automated testing and deployment.

# File Structure
* model.py - Contains Model Architecture
* utils.py - Contains training utilities and helper functions
* src/ - Source code directory
* tests/ - Test files directory
* logs/ - Training logs and metrics
* images/ - Generated plots and visualizations

# Model Parameters
```python
<<<<<<< HEAD
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 4, 26, 26]              36
              ReLU-2            [-1, 4, 26, 26]               0
       BatchNorm2d-3            [-1, 4, 26, 26]               8
           Dropout-4            [-1, 4, 26, 26]               0
            Conv2d-5           [-1, 10, 24, 24]             360
              ReLU-6           [-1, 10, 24, 24]               0
       BatchNorm2d-7           [-1, 10, 24, 24]              20
           Dropout-8           [-1, 10, 24, 24]               0
         MaxPool2d-9           [-1, 10, 12, 12]               0
           Conv2d-10            [-1, 8, 12, 12]              80
             ReLU-11            [-1, 8, 12, 12]               0
      BatchNorm2d-12            [-1, 8, 12, 12]              16
          Dropout-13            [-1, 8, 12, 12]               0
           Conv2d-14            [-1, 4, 12, 12]              32
             ReLU-15            [-1, 4, 12, 12]               0
      BatchNorm2d-16            [-1, 4, 12, 12]               8
          Dropout-17            [-1, 4, 12, 12]               0
           Conv2d-18           [-1, 10, 10, 10]             360
             ReLU-19           [-1, 10, 10, 10]               0
      BatchNorm2d-20           [-1, 10, 10, 10]              20
          Dropout-21           [-1, 10, 10, 10]               0
           Conv2d-22             [-1, 16, 8, 8]           1,440
             ReLU-23             [-1, 16, 8, 8]               0
      BatchNorm2d-24             [-1, 16, 8, 8]              32
          Dropout-25             [-1, 16, 8, 8]               0
           Conv2d-26             [-1, 12, 6, 6]           1,728
             ReLU-27             [-1, 12, 6, 6]               0
      BatchNorm2d-28             [-1, 12, 6, 6]              24
          Dropout-29             [-1, 12, 6, 6]               0
           Conv2d-30             [-1, 16, 4, 4]           1,728
             ReLU-31             [-1, 16, 4, 4]               0
      BatchNorm2d-32             [-1, 16, 4, 4]              32
          Dropout-33             [-1, 16, 4, 4]               0
        AvgPool2d-34             [-1, 16, 1, 1]               0
           Conv2d-35             [-1, 10, 1, 1]             160
================================================================
Total params: 6,084
Trainable params: 6,084
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.40
Params size (MB): 0.02
Estimated Total Size (MB): 0.43
----------------------------------------------------------------
=======
{
    "total_params": 6084,
    "trainable_params": 6084,
    "non_trainable_params": 0,
    "model_size_mb": 0.0232086181640625
}
>>>>>>> 52b3a653ba7a7bb414c8f0f4f77b5e2631ac2cd5
```
</details>

# Training Logs
```
Training: 100%|██████████| 938/938 [00:39<00:00, 23.51it/s, Loss=0.0079, Accuracy=93.67%]
Training Progress: 100%|██████████| 1/1 [00:45<00:00, 45.05s/it, Train Loss=0.2454, Test Loss=0.0506, Train Acc=93.67%, Test Acc=98.50%]
Test set: Average loss: 0.0506, Accuracy: 9850/10000 (98.50%)

```
<<<<<<< HEAD
=======
2024-11-19 13:56:21,671: utils.py: device: cpu
2024-11-19 13:56:21,671: utils.py: transformation Details ::: 
2024-11-19 13:56:56,381: utils.py: Training Losses : [0.2521550218080248]
2024-11-19 13:56:56,381: utils.py: Training Accuracy : [93.4]
2024-11-19 13:56:56,381: utils.py: Test Losses : [0.058875421562790874]
2024-11-19 13:56:56,381: utils.py: Test Accuracy : [98.21]
2024-11-19 13:56:56,385: pyplot.py: Loaded backend agg version v2.2.
2024-11-19 13:56:56,388: font_manager.py: findfont: Matching sans\-serif:style=normal:variant=normal:weight=normal:stretch=normal:size=10.0.
2024-11-19 13:56:56,388: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,388: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBol.ttf', name='STIXNonUnicode', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,388: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmtt10.ttf', name='cmtt10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,388: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmr10.ttf', name='cmr10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,388: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Italic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,388: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf', name='cmmi10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymBol.ttf', name='STIXSizeTwoSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-BoldOblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 1.335
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerifDisplay.ttf', name='DejaVu Serif Display', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 0.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Oblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 1.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-BoldOblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymBol.ttf', name='STIXSizeThreeSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymReg.ttf', name='STIXSizeFourSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymReg.ttf', name='STIXSizeOneSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmex10.ttf', name='cmex10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniIta.ttf', name='STIXNonUnicode', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymBol.ttf', name='STIXSizeOneSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymReg.ttf', name='STIXSizeTwoSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBolIta.ttf', name='STIXNonUnicode', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymReg.ttf', name='STIXSizeThreeSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmsy10.ttf', name='cmsy10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansDisplay.ttf', name='DejaVu Sans Display', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUni.ttf', name='STIXNonUnicode', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 0.33499999999999996
2024-11-19 13:56:56,389: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneral.ttf', name='STIXGeneral', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-BoldItalic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBol.ttf', name='STIXGeneral', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBolIta.ttf', name='STIXGeneral', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmss10.ttf', name='cmss10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFiveSymReg.ttf', name='STIXSizeFiveSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Bold.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymBol.ttf', name='STIXSizeFourSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralItalic.ttf', name='STIXGeneral', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmb10.ttf', name='cmb10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Bold.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf', name='Liberation Serif', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf', name='Liberation Sans', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf', name='Liberation Mono', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-MediumItalic.ttf', name='Lato', style='italic', variant='normal', weight=500, stretch='normal', size='scalable')) = 11.145
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=400, stretch='condensed', size='scalable')) = 11.25
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-HeavyItalic.ttf', name='Lato', style='italic', variant='normal', weight=800, stretch='normal', size='scalable')) = 11.43
2024-11-19 13:56:56,390: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Heavy.ttf', name='Lato', style='normal', variant='normal', weight=800, stretch='normal', size='scalable')) = 10.43
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Medium.ttf', name='Lato', style='normal', variant='normal', weight=500, stretch='normal', size='scalable')) = 10.145
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=700, stretch='condensed', size='scalable')) = 1.535
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=200, stretch='normal', size='scalable')) = 0.24
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf', name='Lato', style='italic', variant='normal', weight=600, stretch='normal', size='scalable')) = 11.24
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=700, stretch='condensed', size='scalable')) = 10.535
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=700, stretch='condensed', size='scalable')) = 11.535
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-BlackItalic.ttf', name='Lato', style='italic', variant='normal', weight=900, stretch='normal', size='scalable')) = 11.525
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 0.05
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf', name='Liberation Serif', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Thin.ttf', name='Lato', style='normal', variant='normal', weight=200, stretch='normal', size='scalable')) = 10.24
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf', name='Liberation Sans Narrow', style='normal', variant='normal', weight=400, stretch='condensed', size='scalable')) = 10.25
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Black.ttf', name='Lato', style='normal', variant='normal', weight=900, stretch='normal', size='scalable')) = 10.525
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf', name='Liberation Mono', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf', name='Liberation Mono', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', name='Liberation Sans', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf', name='Liberation Sans Narrow', style='italic', variant='normal', weight=400, stretch='condensed', size='scalable')) = 11.25
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', name='Liberation Sans', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf', name='Liberation Sans', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,391: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Light.ttf', name='Lato', style='normal', variant='normal', weight=300, stretch='normal', size='scalable')) = 10.145
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf', name='Liberation Sans Narrow', style='normal', variant='normal', weight=700, stretch='condensed', size='scalable')) = 10.535
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf', name='Liberation Serif', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Regular.ttf', name='Lato', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Semibold.ttf', name='Lato', style='normal', variant='normal', weight=600, stretch='normal', size='scalable')) = 10.24
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=400, stretch='condensed', size='scalable')) = 10.25
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-HairlineItalic.ttf', name='Lato', style='italic', variant='normal', weight=100, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Italic.ttf', name='Lato', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf', name='Liberation Serif', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-LightItalic.ttf', name='Lato', style='italic', variant='normal', weight=300, stretch='normal', size='scalable')) = 11.145
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=700, stretch='condensed', size='scalable')) = 0.5349999999999999
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf', name='Liberation Mono', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 0.33499999999999996
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuMathTeXGyre.ttf', name='DejaVu Math TeX Gyre', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,392: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Bold.ttf', name='Lato', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-BoldItalic.ttf', name='Lato', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-ThinItalic.ttf', name='Lato', style='italic', variant='normal', weight=200, stretch='normal', size='scalable')) = 11.24
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 1.05
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 1.335
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Hairline.ttf', name='Lato', style='normal', variant='normal', weight=100, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=400, stretch='condensed', size='scalable')) = 0.25
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf', name='Liberation Sans Narrow', style='italic', variant='normal', weight=700, stretch='condensed', size='scalable')) = 11.535
2024-11-19 13:56:56,393: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=400, stretch='condensed', size='scalable')) = 1.25
2024-11-19 13:56:56,393: font_manager.py: findfont: Matching sans\-serif:style=normal:variant=normal:weight=normal:stretch=normal:size=10.0 to DejaVu Sans ('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf') with score of 0.050000.
2024-11-19 13:56:56,460: font_manager.py: findfont: Matching sans\-serif:style=normal:variant=normal:weight=normal:stretch=normal:size=12.0.
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBol.ttf', name='STIXNonUnicode', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmtt10.ttf', name='cmtt10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmr10.ttf', name='cmr10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Italic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmmi10.ttf', name='cmmi10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,460: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymBol.ttf', name='STIXSizeTwoSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-BoldOblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 1.335
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerifDisplay.ttf', name='DejaVu Serif Display', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 0.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Oblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 1.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-BoldOblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymBol.ttf', name='STIXSizeThreeSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymReg.ttf', name='STIXSizeFourSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymReg.ttf', name='STIXSizeOneSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmex10.ttf', name='cmex10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniIta.ttf', name='STIXNonUnicode', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizOneSymBol.ttf', name='STIXSizeOneSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizTwoSymReg.ttf', name='STIXSizeTwoSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUniBolIta.ttf', name='STIXNonUnicode', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizThreeSymReg.ttf', name='STIXSizeThreeSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmsy10.ttf', name='cmsy10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,461: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansDisplay.ttf', name='DejaVu Sans Display', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUni.ttf', name='STIXNonUnicode', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 0.33499999999999996
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneral.ttf', name='STIXGeneral', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-BoldItalic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBol.ttf', name='STIXGeneral', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralBolIta.ttf', name='STIXGeneral', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmss10.ttf', name='cmss10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFiveSymReg.ttf', name='STIXSizeFiveSym', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-Bold.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXSizFourSymBol.ttf', name='STIXSizeFourSym', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/STIXGeneralItalic.ttf', name='STIXGeneral', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/cmb10.ttf', name='cmb10', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Bold.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,462: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf', name='Liberation Serif', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf', name='Liberation Sans', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf', name='Liberation Mono', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-MediumItalic.ttf', name='Lato', style='italic', variant='normal', weight=500, stretch='normal', size='scalable')) = 11.145
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=400, stretch='condensed', size='scalable')) = 11.25
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-HeavyItalic.ttf', name='Lato', style='italic', variant='normal', weight=800, stretch='normal', size='scalable')) = 11.43
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Heavy.ttf', name='Lato', style='normal', variant='normal', weight=800, stretch='normal', size='scalable')) = 10.43
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Medium.ttf', name='Lato', style='normal', variant='normal', weight=500, stretch='normal', size='scalable')) = 10.145
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf', name='DejaVu Sans Mono', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=700, stretch='condensed', size='scalable')) = 1.535
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=200, stretch='normal', size='scalable')) = 0.24
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf', name='Lato', style='italic', variant='normal', weight=600, stretch='normal', size='scalable')) = 11.24
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=700, stretch='condensed', size='scalable')) = 10.535
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=700, stretch='condensed', size='scalable')) = 11.535
2024-11-19 13:56:56,463: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-BlackItalic.ttf', name='Lato', style='italic', variant='normal', weight=900, stretch='normal', size='scalable')) = 11.525
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 0.05
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf', name='Liberation Serif', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Thin.ttf', name='Lato', style='normal', variant='normal', weight=200, stretch='normal', size='scalable')) = 10.24
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf', name='Liberation Sans Narrow', style='normal', variant='normal', weight=400, stretch='condensed', size='scalable')) = 10.25
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Black.ttf', name='Lato', style='normal', variant='normal', weight=900, stretch='normal', size='scalable')) = 10.525
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf', name='Liberation Mono', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf', name='Liberation Mono', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', name='Liberation Sans', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf', name='Liberation Sans Narrow', style='italic', variant='normal', weight=400, stretch='condensed', size='scalable')) = 11.25
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', name='Liberation Sans', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf', name='Liberation Sans', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Light.ttf', name='Lato', style='normal', variant='normal', weight=300, stretch='normal', size='scalable')) = 10.145
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf', name='Liberation Sans Narrow', style='normal', variant='normal', weight=700, stretch='condensed', size='scalable')) = 10.535
2024-11-19 13:56:56,464: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf', name='Liberation Serif', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Regular.ttf', name='Lato', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Semibold.ttf', name='Lato', style='normal', variant='normal', weight=600, stretch='normal', size='scalable')) = 10.24
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf', name='DejaVu Serif', style='normal', variant='normal', weight=400, stretch='condensed', size='scalable')) = 10.25
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-HairlineItalic.ttf', name='Lato', style='italic', variant='normal', weight=100, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Italic.ttf', name='Lato', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf', name='Liberation Serif', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-LightItalic.ttf', name='Lato', style='italic', variant='normal', weight=300, stretch='normal', size='scalable')) = 11.145
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=700, stretch='condensed', size='scalable')) = 0.5349999999999999
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', name='DejaVu Sans Mono', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf', name='Liberation Mono', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf', name='DejaVu Serif', style='italic', variant='normal', weight=400, stretch='normal', size='scalable')) = 11.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 0.33499999999999996
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuMathTeXGyre.ttf', name='DejaVu Math TeX Gyre', style='normal', variant='normal', weight=400, stretch='normal', size='scalable')) = 10.05
2024-11-19 13:56:56,465: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Bold.ttf', name='Lato', style='normal', variant='normal', weight=700, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-BoldItalic.ttf', name='Lato', style='italic', variant='normal', weight=700, stretch='normal', size='scalable')) = 11.335
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-ThinItalic.ttf', name='Lato', style='italic', variant='normal', weight=200, stretch='normal', size='scalable')) = 11.24
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=400, stretch='normal', size='scalable')) = 1.05
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=700, stretch='normal', size='scalable')) = 1.335
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/lato/Lato-Hairline.ttf', name='Lato', style='normal', variant='normal', weight=100, stretch='normal', size='scalable')) = 10.335
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf', name='DejaVu Sans', style='normal', variant='normal', weight=400, stretch='condensed', size='scalable')) = 0.25
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf', name='Liberation Sans Narrow', style='italic', variant='normal', weight=700, stretch='condensed', size='scalable')) = 11.535
2024-11-19 13:56:56,466: font_manager.py: findfont: score(FontEntry(fname='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf', name='DejaVu Sans', style='oblique', variant='normal', weight=400, stretch='condensed', size='scalable')) = 1.25
2024-11-19 13:56:56,466: font_manager.py: findfont: Matching sans\-serif:style=normal:variant=normal:weight=normal:stretch=normal:size=12.0 to DejaVu Sans ('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf') with score of 0.050000.

```
</details>

>>>>>>> 52b3a653ba7a7bb414c8f0f4f77b5e2631ac2cd5
# Results

## Accuracy Plot
![Accuracy and Loss Plots](images/accuracy_plot.png)

## Sample Output
![Sample Predictions](images/prediction.png)

## Misclassified Images
![Misclassified Images](images/missclassified.png)

## Accuracy Report for Each class
![Class-wise Accuracy](images/accuracy_per_class.png)

```json
<<<<<<< HEAD
{' zero': 98.77300613496932,
 ' one': 98.37837837837837,
 ' two': 97.0059880239521,
 ' three': 100.0,
 ' four': 97.91666666666667,
 ' five': 99.1869918699187,
 ' six': 98.70967741935483,
 ' seven': 98.93048128342247,
 ' eight': 96.18320610687023,
 ' nine': 97.24137931034483}
=======
{
    " zero": 97.98657718120805,
    " one": 98.88888888888889,
    " two": 99.35483870967742,
    " three": 98.57142857142857,
    " four": 100.0,
    " five": 100.0,
    " six": 98.15950920245399,
    " seven": 97.10982658959537,
    " eight": 96.875,
    " nine": 96.85534591194968
}
>>>>>>> 52b3a653ba7a7bb414c8f0f4f77b5e2631ac2cd5
```
</details>
