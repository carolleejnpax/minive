import torch
import torchvision.models as models
import onnx

# Load the PyTorch model
model = models.resnet18(pretrained=True)

# Add the batch dimension to the input shape
dummy_input = torch.randn(1, 3, 224, 224)

# Export the model to ONNX
torch.onnx.export(model, dummy_input, "path/to/your/model.onnx")
