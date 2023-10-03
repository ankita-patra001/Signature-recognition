import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

# Data augmentation 
train_datagen = ImageDataGenerator(
        rotation_range=15,
        zoom_range=0.1,
        width_shift_range=0.1,
        height_shift_range=0.1
    )

test_datagen = ImageDataGenerator() 

train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(ROWS, COLS),
        batch_size=32,
        class_mode='categorical'
    )

valid_generator = test_datagen.flow_from_directory(
        VALID_DIR,
        target_size=(ROWS, COLS),
        batch_size=32,
        class_mode='categorical'
    )

# Use pretrained ResNet model
model = keras.applications.resnet50.ResNet50(
        weights='imagenet', 
        input_shape=(ROWS, COLS, 3), 
        include_top=False
    )

# Freeze early layers
for layer in model.layers[:100]:
    layer.trainable = False

# Add custom layers
x = model.output
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(len(SIGNATURE_CLASSES), activation='softmax')(x)

# Compile model
model = Model(inputs=model.input, outputs=predictions)
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.0001))

# Train model using image generator
model.fit_generator(
        train_generator, 
        steps_per_epoch=len(train_generator),
        epochs=10,
        validation_data=valid_generator
    )
