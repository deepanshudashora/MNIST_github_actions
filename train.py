# Initialized Logger
import torch
import torch.optim as optim
from torchvision import datasets
from model import Net
from utils import data_transformation, get_device, \
                  fit_model, plot_accuracy_report, \
                  show_random_results, plot_misclassified, \
                  calculate_accuracy_per_class
import os
import json

# CUDA?
device = get_device()
print("Available Device :: ", device)

transformation_matrix = {"image_size":(28,28),
                         "random_rotation_angle":(-5.0, 5.0),
                         "mean_of_data":(0.1307,),
                         "std_of_data": (0.3081,),
                         "center_crop_size": (24,24),
                         "center_crop_probability" : 0.1,
                         }

dataloader_kwargs = {'batch_size': 64, 'shuffle': True, 'num_workers': 1, 'pin_memory': True}


train_transforms, test_transforms = data_transformation(transformation_matrix)
train_data = datasets.MNIST('../data', train=True, download=True, transform=train_transforms)
test_data = datasets.MNIST('../data', train=False, download=True, transform=test_transforms)

train_loader = torch.utils.data.DataLoader(train_data, **dataloader_kwargs)
test_loader = torch.utils.data.DataLoader(test_data, **dataloader_kwargs)

model = Net().to(device)

def count_model_parameters(model):
    """Count model parameters"""
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    non_trainable_params = total_params - trainable_params
    
    return {
        "total_params": total_params,
        "trainable_params": trainable_params,
        "non_trainable_params": non_trainable_params,
        "model_size_mb": sum(p.numel() * p.element_size() for p in model.parameters()) / (1024 * 1024)
    }

def update_readme_with_model_params(model):
    try:
        with open('README.md', 'r') as f:
            readme = f.read()
        
        # Get model parameters
        params = count_model_parameters(model)
        
        # Update model parameters section
        params_section = f"""```python
{json.dumps(params, indent=4)}
```"""
        # Find the model parameters section and update it
        start = readme.find('# Model Parameters')
        end = readme.find('# Training Logs')
        if start != -1 and end != -1:
            new_section = f"# Model Parameters\n<details>\n<summary>Click to expand model parameters</summary>\n\n{params_section}\n</details>\n\n"
            readme = readme[:start] + new_section + readme[end:]
            
        with open('README.md', 'w') as f:
            f.write(readme)
    except Exception as e:
        print(f"Error updating README with model params: {e}")

#model_summary = summary(model, input_size=(1, 28, 28))

# print(type(model_summary))
update_readme_with_model_params(model)

training_parameters = {"learning_rate":0.01,
                       "momentum":0.9,
                       "step_size":6,
                       "gamma":0.3,
                       "max_lr":0.017,
                       "num_epochs":1
                       }
train_losses, test_losses, train_acc, test_acc = fit_model(model,training_parameters,train_loader,test_loader,device)

plot_accuracy_report(train_losses, test_losses, train_acc, test_acc)

grid_size = (4,4)
show_random_results(test_loader,grid_size,model,device)

grid_size = (4,4)
plot_misclassified(model,grid_size,test_loader,device)

# Get the final_output from calculate_accuracy_per_class
final_output = calculate_accuracy_per_class(model,device,test_loader,test_data)

def save_metrics(train_losses, test_losses, train_acc, test_acc):
    metrics = {
        'train_loss': train_losses,
        'test_loss': test_losses,
        'train_accuracy': train_acc,
        'test_accuracy': test_acc
    }
    os.makedirs('logs', exist_ok=True)
    with open('logs/metrics.json', 'w') as f:
        json.dump(metrics, f)

def save_class_accuracy(class_accuracies):
    with open('logs/class_accuracy.json', 'w') as f:
        json.dump(class_accuracies, f)

# Save metrics and model
save_metrics(train_losses, test_losses, train_acc, test_acc)
torch.save(model.state_dict(), 'model.pth')
save_class_accuracy(final_output)

# Update README
def update_readme_with_logs():
    try:
        with open('README.md', 'r') as f:
            readme = f.read()
        
        # Update logs section
        if os.path.exists('logs/network.log'):
            with open('logs/network.log', 'r') as f:
                logs = f.read()
            logs_section = f"```\n{logs}\n```"
            
            # Find and update logs section
            start = readme.find('# Training Logs')
            end = readme.find('# Results')
            if start != -1 and end != -1:
                new_section = f"# Training Logs\n<details>\n<summary>Click to expand training logs</summary>\n\n{logs_section}\n</details>\n\n"
                readme = readme[:start] + new_section + readme[end:]
        
        # Update class-wise accuracy
        if os.path.exists('logs/class_accuracy.json'):
            with open('logs/class_accuracy.json', 'r') as f:
                class_acc = json.load(f)
            class_acc_section = f"```json\n{json.dumps(class_acc, indent=4)}\n```"
            
            # Find and update class accuracy section
            acc_start = readme.find('<details>\n<summary>Click to see detailed class-wise accuracy</summary>')
            acc_end = readme.find('</details>', acc_start)
            if acc_start != -1 and acc_end != -1:
                new_acc_section = f"<details>\n<summary>Click to see detailed class-wise accuracy</summary>\n\n{class_acc_section}\n</details>"
                readme = readme[:acc_start] + new_acc_section + readme[acc_end + 10:]
        
        with open('README.md', 'w') as f:
            f.write(readme)
    except Exception as e:
        print(f"Error updating README with logs: {e}")

update_readme_with_logs()