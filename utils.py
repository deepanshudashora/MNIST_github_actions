import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
import numpy as np
# Data to plot accuracy and loss graphs

import os
os.makedirs("logs/", exist_ok=True)
os.makedirs("images/", exist_ok=True)

import logging
logging.basicConfig(filename='logs/network.log', format='%(asctime)s: %(filename)s: %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)



test_incorrect_pred = {'images': [], 'ground_truths': [], 'predicted_vals': []}

def get_device():
    cuda = torch.cuda.is_available()
    device = torch.device("cuda" if cuda else "cpu")
    logger.info("device: %s" % device)
    return device


def data_transformation(transformation_matrix):
    # Train Transform
    logger.info("transformation Details ::: ", transformation_matrix)
    train_transforms = transforms.Compose([
        transforms.RandomApply([transforms.CenterCrop(transformation_matrix["center_crop_size"]), ], p=transformation_matrix["center_crop_probability"]),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize(transformation_matrix["mean_of_data"],transformation_matrix["std_of_data"]),
        transforms.RandomRotation(transformation_matrix["random_rotation_angle"], fill=(0,)),
        ])

    # Test data transformations
    test_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(transformation_matrix["mean_of_data"],transformation_matrix["std_of_data"])
        ])
    
    # Save augmentation examples
    test_data = datasets.MNIST('../data', train=False, download=True, transform=transforms.ToTensor())
    save_augmentation_examples(train_transforms, test_data)

    return train_transforms, test_transforms


def GetCorrectPredCount(pPrediction, pLabels):
  return pPrediction.argmax(dim=1).eq(pLabels).sum().item()

def train(model, device, train_loader, optimizer):
    model.train()
    pbar = tqdm(train_loader, desc='Training')
    
    train_loss = 0
    correct = 0
    processed = 0

    for batch_idx, (data, target) in enumerate(pbar):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()

        # Predict
        pred = model(data)

        # Calculate loss
        loss = F.nll_loss(pred, target)
        train_loss += loss.item()

        # Backpropagation
        loss.backward()
        optimizer.step()
        
        correct += GetCorrectPredCount(pred, target)
        processed += len(data)

        pbar.set_postfix({
            'Loss': f'{loss.item():0.4f}',
            'Accuracy': f'{100*correct/processed:0.2f}%'
        })

    train_loss /= len(train_loader)
    train_accuracy = 100 * correct / processed
    return train_loss, train_accuracy

def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    processed = 0

    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(test_loader):
            data, target = data.to(device), target.to(device)

            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            correct += GetCorrectPredCount(output, target)
            processed += len(data)

    test_loss /= processed
    test_accuracy = 100 * correct / processed
    
    print(f'Test set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{processed} ({test_accuracy:.2f}%)')
    return test_loss, test_accuracy


def fit_model(model,training_parameters,train_loader,test_loader,device):
    train_losses = []
    test_losses = []
    train_acc = []
    test_acc = []

    optimizer = optim.SGD(model.parameters(), lr=training_parameters["learning_rate"], momentum=training_parameters["momentum"])
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=training_parameters["step_size"], gamma=training_parameters["gamma"])
    
    epochs = tqdm(range(1, training_parameters["num_epochs"]+1), desc="Training Progress" )
    for epoch in epochs:
        train_loss, train_accuracy = train(model, device, train_loader, optimizer)
        test_loss, test_accuracy = test(model, device, test_loader)
        
        train_losses.append(train_loss)
        test_losses.append(test_loss)
        train_acc.append(train_accuracy)
        test_acc.append(test_accuracy)
        
        epochs.set_postfix({
            'Train Loss': f'{train_loss:.4f}',
            'Test Loss': f'{test_loss:.4f}',
            'Train Acc': f'{train_accuracy:.2f}%',
            'Test Acc': f'{test_accuracy:.2f}%'
        })
        
        scheduler.step()
        
    logging.info('Training Losses : %s', train_losses)
    logging.info('Training Accuracy : %s', train_acc)
    logging.info('Test Losses : %s', test_losses)
    logging.info('Test Accuracy : %s', test_acc)
        
    return train_losses, test_losses, train_acc, test_acc

def plot_accuracy_report(train_losses, test_losses, train_acc, test_acc):
    # Debugging: print the lengths and samples of data
    print(f"train_losses length: {len(train_losses)}")
    print(f"test_losses length: {len(test_losses)}")
    print(f"train_acc length: {len(train_acc)}")
    print(f"test_acc length: {len(test_acc)}")
    
    # Check that the input lists are not empty
    if not all([train_losses, test_losses, train_acc, test_acc]):
        print("Error: One or more input lists are empty.")
        return
    
    if len(train_losses) != len(test_losses) or len(train_losses) != len(train_acc) or len(train_losses) != len(test_acc):
        print("Error: Input lists have mismatched lengths.")
        return

    # Create the 'images' directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot Training Loss
    axs[0, 0].plot(train_losses)
    axs[0, 0].set_title("Training Loss")
    axs[0, 0].set_xlabel('Epochs')
    axs[0, 0].set_ylabel('Loss')

    # Plot Training Accuracy
    axs[1, 0].plot(train_acc)
    axs[1, 0].set_title("Training Accuracy")
    axs[1, 0].set_xlabel('Epochs')
    axs[1, 0].set_ylabel('Accuracy')

    # Plot Test Loss
    axs[0, 1].plot(test_losses)
    axs[0, 1].set_title("Test Loss")
    axs[0, 1].set_xlabel('Epochs')
    axs[0, 1].set_ylabel('Loss')

    # Plot Test Accuracy
    axs[1, 1].plot(test_acc)
    axs[1, 1].set_title("Test Accuracy")
    axs[1, 1].set_xlabel('Epochs')
    axs[1, 1].set_ylabel('Accuracy')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Debugging: Show the plot before saving it
    plt.show()

    # Save the plot
    plt.savefig('images/accuracy_plot.png')

    # Close the plot
    plt.close()

def show_random_results(test_loader, grid_size, model, device):
    cols, rows = grid_size[0], grid_size[1]
    figure = plt.figure(figsize=(20, 20))
    for i in range(1, cols * rows + 1):
        k = np.random.randint(0, len(test_loader.dataset))
        img, label = test_loader.dataset[k]
        img = img.unsqueeze(0)
        pred = model(img.to(device))

        figure.add_subplot(rows, cols, i)
        plt.title(
            f"Predicted Label: {pred.argmax().item()}\nTrue Label: {label}", 
            fontsize=20  # Increase this value to make the text size larger
        )
        plt.axis("off")
        plt.imshow(img.squeeze(), cmap="gray")

    # Save the plot
    plt.savefig('images/prediction.png')
    plt.close()

def plot_misclassified(model,grid_size,test_loader,device):
    count = 0
    k = 0
    misclf = list()
    while count<=20:
        img, label = test_loader.dataset[k]
        pred = model(img.unsqueeze(0).to(device))
        pred = pred.argmax().item()

        k += 1
        if pred!=label:
            misclf.append((img, label, pred))
            count += 1
    
    rows, cols = grid_size[0],grid_size[1]
    figure = plt.figure(figsize=(20,20))

    for i in range(1, cols * rows + 1):
        img, label, pred = misclf[i-1]

        figure.add_subplot(rows, cols, i)
        plt.title(f"Predcited label {pred}\n True Label: {label}",fontsize=20)
        plt.axis("off")
        plt.imshow(img.squeeze(), cmap="gray")

    # Save the plot
    plt.savefig('images/missclassified.png')
    plt.close()

def calculate_accuracy_per_class(model,device,test_loader,test_data):  
    model = model.to(device)
    model.eval()
    class_correct = list(0. for i in range(10))
    class_total = list(0. for i in range(10))
    final_output = {}
    
    with torch.no_grad():
        for data in tqdm(test_loader, desc="Calculating class accuracies" ):
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = model(images.to(device))
            _, predicted = torch.max(outputs, 1)
            c = (predicted == labels).squeeze()
            for i in range(10):
                label = labels[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1

    classes = test_data.classes
    for i in range(10):
        accuracy = 100 * class_correct[i] / class_total[i]
        final_output[classes[i].split("-")[1]] = accuracy
        
    original_class = list(final_output.keys())
    class_accuracy = list(final_output.values())
    plt.figure(figsize=(8, 6))
    plt.bar(original_class, class_accuracy)
    plt.xlabel('classes')
    plt.ylabel('accuracy')
    
    # Save the plot
    plt.savefig('images/accuracy_per_class.png')
    plt.close()
    
    return final_output

def save_augmentation_examples(train_transforms, test_data, num_examples=5):
    """
    Save examples of each augmentation type in a grid
    Args:
        train_transforms: transformation pipeline
        test_data: original dataset
        num_examples: number of examples per augmentation
    """
    plt.figure(figsize=(20, 10))
    
    # Get original images
    original_images = [test_data[i][0] for i in range(num_examples)]
    
    # List of individual transforms to visualize
    transforms_list = [
        transforms.RandomRotation((-10.0, 10.0), fill=(0,)),
        transforms.CenterCrop(20),
        transforms.Normalize((0.1307,), (0.3081,))
    ]
    
    transform_names = ['Original', 'Random Rotation', 'Center Crop', 'Normalized']
    
    # Create a grid: num_examples rows, len(transforms_list)+1 columns
    for idx, img in enumerate(original_images):
        # Original image
        plt.subplot(num_examples, len(transform_names), idx*len(transform_names) + 1)
        plt.imshow(img.squeeze(), cmap='gray')
        if idx == 0:
            plt.title('Original', pad=20,fontsize=20)
        plt.axis('off')
        
        # Apply each transform
        for t_idx, transform in enumerate(transforms_list):
            plt.subplot(num_examples, len(transform_names), idx*len(transform_names) + t_idx + 2)
            
            # Apply transform
            if isinstance(transform, transforms.Normalize):
                # For normalize, we need to show the effect differently
                img_normalized = transform(img.clone())
                img_show = (img_normalized - img_normalized.min()) / (img_normalized.max() - img_normalized.min())
            else:
                img_show = transform(img.clone())
            
            plt.imshow(img_show.squeeze(), cmap='gray')
            if idx == 0:
                plt.title(transform_names[t_idx + 1], pad=20,fontsize=20)
            plt.axis('off')
    
    plt.tight_layout()
    os.makedirs('images', exist_ok=True)
    plt.savefig('images/augmentation_examples.png', bbox_inches='tight', dpi=300)
    plt.close()