from flask import Flask, request, jsonify, render_template
import os
import json
import torch
from torch import optim
from torchvision import models, transforms
import numpy as np
from PIL import Image
import io
#import cv2
from torch import nn
from collections import OrderedDict


use_cuda = torch.cuda.is_available()

app = Flask(__name__, static_url_path='/static')

def load_checkpoint(filepath):
    model = models.resnet50(pretrained=True)
    model.to('cpu')

    fc_inputs = model.fc.in_features
    num_classes = 73 #TO-DO: Should pass this into the save checkpoint during training!

    model.fc = nn.Sequential(
        nn.Linear(fc_inputs, 256),
        nn.ReLU(),
        nn.Dropout(0.4),
        nn.Linear(256, num_classes),  # Since 10 possible outputs
        nn.LogSoftmax(dim=1)  # For using NLLLoss()
    )

    optimizer =  optim.Adam(model.parameters())
    checkpoint = torch.load(filepath, map_location='cpu')
    model_state_dict = checkpoint['model_state_dict']

#### Fix since the model was trained on parallel GPUs!!!
#    new_state_dict = OrderedDict()
#    for k, v in model_state_dict.items():
#        name = k[7:]  # remove 'module.' of dataparallel
#        new_state_dict[name] = v


    model.load_state_dict(model_state_dict)
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']

    for param in model.parameters():
        param.require_grad = False

    model.eval()
    #model.train()

    with open('item_id_to_class.json', 'r') as f:
        class_to_idx = json.load(f)
        #distros_dict = json.load(f)


    return model, optimizer, class_to_idx


#Load Model Once at App Init
trained_model, optimizer, class_to_idx = load_checkpoint('model/checkpoint-19.pth')

def lookup_class_by_idx(lookup_dict, lookup_value):
    return_class = ''
    return_class = [key for key in lookup_dict.items() if key[1] == lookup_value][0][0]
    return return_class

#Predict Item using Input Image, Model
def predict_item(pil_image, model, lookup_index):
    # load the image and return the predicted breed
    mean_train_set, std_train_set = [0.485, 0.456, 0.406],[0.229, 0.224, 0.225]

    image_transforms = transforms.Compose([transforms.Resize(256),
                                           transforms.CenterCrop(224),
                                           transforms.ToTensor(),
                                           transforms.Normalize(mean_train_set, std_train_set)])

    image_tensor = image_transforms(pil_image)

    if torch.cuda.is_available():
        image_tensor = image_tensor.view(1, 3, 224, 224).cuda()
    else:
        image_tensor = image_tensor.view(1, 3, 224, 224)


    with torch.no_grad():
        model.eval()

        out = model(image_tensor)
        ps = torch.exp(out)
        topk, topclass = ps.topk(3, dim=1)

        predicted_results = []

        for i in range(3):
            print("Prediction", i + 1, ":", lookup_class_by_idx(lookup_index, topclass.cpu().numpy()[0][i]), ", Score: ", topk.cpu().numpy()[0][i])
            predicted_results.append({'index':  str(topclass.cpu().numpy()[0][i]), 'class': str(lookup_class_by_idx(lookup_index, topclass.cpu().numpy()[0][i])), 'score': str(topk.cpu().numpy()[0][i])})

    return predicted_results




@app.route('/about')
def render_about_page():
    return render_template('about.html')

@app.route('/model')
def render_model_page():
    return render_template('model.html')

@app.route('/')
def render_page():
    #return "Hello World!"
    return render_template('product-web-app.html')

@app.route('/uploadajax', methods=['POST'])
def upload_file():
    """
    retrieve the image uploaded and make sure it is an image file
    """
    file = request.files['file']
    image_extensions = ['jpg', 'jpeg', 'png']
    if file.filename.split('.')[1] not in image_extensions:
        return jsonify('Please upload an appropriate image type')

    image_bytes = file.read()
    pil_image = Image.open(io.BytesIO(image_bytes))

    nparr = np.frombuffer(image_bytes, np.uint8)

    img_np = np.array(Image.open(io.BytesIO(nparr)))

    item_detected = predict_item(pil_image, trained_model, class_to_idx)
    return jsonify(item_detected)


if __name__ == '__main__':
    #app.run(debug=False, port=os.getenv('PORT', 5000))
    #trained_model, optimizer, class_to_idx = load_checkpoint('model/checkpoint-3.pth')
    app.run(debug=False, host='0.0.0.0')
