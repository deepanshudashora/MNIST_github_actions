import torch
import pytest
from src.model import Net

@pytest.fixture
def model():
    return Net()

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
    """Test 3: Check if model produces stable outputs (no NaN values)"""
    x = torch.randn(10, 1, 28, 28)
    output = model(x)
    assert not torch.isnan(output).any(), "Model produced NaN values" 