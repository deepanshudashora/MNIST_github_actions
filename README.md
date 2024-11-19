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
<details>
<summary>Click to expand model parameters</summary>

```python
{
    "total_params": "Loading...",
    "trainable_params": "Loading...",
    "non_trainable_params": "Loading...",
    "model_size_mb": "Loading..."
}
```
</details>

# Training Logs
<details>
<summary>Click to expand training logs</summary>

```
Loading training logs...
```
</details>

# Results

## Accuracy Plot
![Accuracy and Loss Plots](images/accuracy_plot.png)

## Sample Output
![Sample Predictions](images/prediction.png)

## Misclassified Images
![Misclassified Images](images/missclassified.png)

## Accuracy Report for Each class
![Class-wise Accuracy](images/accuracy_per_class.png)

<details>
<summary>Click to see detailed class-wise accuracy</summary>

```json
Loading class-wise accuracy...
```
</details>
