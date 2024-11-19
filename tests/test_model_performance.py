import torch
import pytest
import json
import os
from model import Net

@pytest.fixture
def model():
    model = Net()
    # Load trained model weights if they exist
    if os.path.exists('model.pth'):
        model.load_state_dict(torch.load('model.pth', map_location='cpu'))
    return model

def test_model_accuracy():
    """Test accuracy from saved metrics"""
    if os.path.exists('logs/metrics.json'):
        with open('logs/metrics.json', 'r') as f:
            metrics = json.load(f)
        assert metrics['test_accuracy'][-1] > 95, "Model accuracy should be > 95%"

def test_class_accuracies():
    """Test per-class accuracy from saved metrics"""
    if os.path.exists('logs/class_accuracy.json'):
        with open('logs/class_accuracy.json', 'r') as f:
            class_acc = json.load(f)
        for class_name, accuracy in class_acc.items():
            assert accuracy > 90, f"Accuracy for class {class_name} should be > 90%"

def test_loss_convergence():
    """Test if loss has converged properly"""
    if os.path.exists('logs/metrics.json'):
        with open('logs/metrics.json', 'r') as f:
            metrics = json.load(f)
        final_loss = metrics['test_loss'][-1]
        assert final_loss < 0.1, f"Final loss {final_loss} should be < 0.1" 