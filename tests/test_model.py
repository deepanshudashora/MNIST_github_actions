import torch
import pytest
from ..model import Net
from ..utils import get_device, data_transformation
from torchvision import datasets
import torch.nn.functional as F

@pytest.fixture
def model():
    return Net()

@pytest.fixture
def device():
    return get_device()

@pytest.fixture
def test_loader():
    transformation_matrix = {
        "center_crop_size": 22,
        "center_crop_probability": 0.3,
        "mean_of_data": (0.1307,),
        "std_of_data": (0.3081,),
        "random_rotation_angle": (-7.0, 7.0)
    }
    _, test_transforms = data_transformation(transformation_matrix)
    test_data = datasets.MNIST('../data', train=False, download=True, transform=test_transforms)
    return torch.utils.data.DataLoader(test_data, batch_size=1000, shuffle=False)

def test_model_parameters(model):
    """Test 1: Ensure model has less than 10,000 parameters"""
    total_params = sum(p.numel() for p in model.parameters())
    assert total_params < 10000, f"Model has {total_params} parameters, should be less than 10000"

def test_forward_shape(model):
    """Test 2: Verify model output shape is correct"""
    batch_size = 64
    x = torch.randn(batch_size, 1, 28, 28)
    output = model(x)
    assert output.shape == (batch_size, 10), f"Expected shape (64, 10), got {output.shape}"

def test_model_stability(model):
    """Test 4: Check if model produces stable outputs (no NaN values)"""
    x = torch.randn(10, 1, 28, 28)
    output = model(x)
    assert not torch.isnan(output).any(), "Model produced NaN values"

def test_loss_computation(model):
    """Test 5: Verify loss computation is working correctly"""
    x = torch.randn(32, 1, 28, 28)
    target = torch.randint(0, 10, (32,))
    output = model(x)
    loss = F.nll_loss(output, target)
    assert not torch.isnan(loss), "Loss computation produced NaN"
    assert loss > 0, "Loss should be positive during initial training" 