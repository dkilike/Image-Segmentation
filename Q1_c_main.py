from Q1_c_model import *
from Q1_c_data import *

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"


data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(2,'NeuralNetworkData\\train','image','label',data_gen_args,save_to_dir = None)

model = unet()
model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,class_weight=[1,5000],steps_per_epoch=300,epochs=1,callbacks=[model_checkpoint])

testGene = testGenerator("C:\\Users\\lxtom\\Segmentation\\NeuralNetworkData\\test\\image")
results = model.predict_generator(testGene,50,verbose=1)
saveResult("C:\\Users\\lxtom\\Segmentation\\NeuralNetworkData\\test\\image",results)