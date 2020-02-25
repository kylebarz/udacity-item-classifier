import os
import torch
from torchvision import models, transforms

trained_model = torch.load('model/product_classifier_model_74.pth', map_location='cpu')
#trained_model.load_state_dict(state_dict)
trained_model.load_state_dict(torch.load('model/product_classifier_model_74.pth', map_location='cpu'))

#print(trained_model_history)