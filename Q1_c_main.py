from Q1_c_model import *
from Q1_c_data import *

# Your source path
src_path = 'C:\\Users\\lxtom\\Segmentation\\'
epoch_num = 2000
batch_size = 10
# online augmentation for better generalization
data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
# training and validation generator
myGene = trainGenerator(batch_size,src_path+'NeuralNetworkData\\train','image','label',data_gen_args,save_to_dir = None,num_class=2)
valGene = trainGenerator(batch_size,src_path+'NeuralNetworkData\\test','image','label',dict(),save_to_dir = None,num_class=2)

# build unet model
model = unet()
tensorboard = tf.keras.callbacks.TensorBoard(log_dir=src_path+'training_logs')
model_checkpoint = tf.keras.callbacks.ModelCheckpoint('SavedModel.hdf5',monitor='loss',verbose=1, save_best_only=True)
for idx in range(1,epoch_num):
    model.fit_generator(myGene,steps_per_epoch=50,epochs=idx,initial_epoch=idx-1, callbacks=[tensorboard, model_checkpoint],validation_data=valGene,validation_steps=4)

    testGene = testGenerator(src_path+"NeuralNetworkData\\test\\image")
    results = model.predict_generator(testGene,40,verbose=1)
    saveResult(src_path+"NeuralNetworkData\\test",results)