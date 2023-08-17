from keras.models import Sequential
from keras.layers import Dense
from .utils import Trad
import numpy as np
from .models import EurUsd
from celery import shared_task
from django.db import transaction

# Build the model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(9,)))  # First Dense layer
model.add(Dense(128, activation='relu'))  # Second Dense layer
model.add(Dense(256, activation='relu'))  # Third Dense layer
model.add(Dense(128, activation='relu'))  # Fourth Dense layer
model.add(Dense(64, activation='relu'))  # Fifth Dense layer
model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.load_weights('media/model_weights.h5')


dict_norm = {
 'open': {'min': 1.08766, 'max': 1.10575},
 'close': {'min': 1.08765, 'max': 1.10576},
 'high': {'min': 1.08779, 'max': 1.10646},
 'low': {'min': 1.08742, 'max': 1.10493},
 'volume': {'min': 1.0, 'max': 2243.0}
}

def min_max_norm(value, min_max):
    min = float(min_max['min'])
    max = float(min_max['max'])
    return (float(value) -min)/(max - min)

def predict(instance):
    print('make prediction !!')
    norm_instance = {}
    norm_instance['month'] = instance['month']/12
    norm_instance['hour'] = instance['hour']/24
    norm_instance['day'] = instance['hour']/31
    norm_instance['minute'] = instance['minute']/60

    for key in dict_norm:
        norm_instance[key] = min_max_norm(instance[key], dict_norm[key])

    return model.predict(
            list(norm_instance.values())
    )[0] > 0.5

@shared_task
def get_and_insert_new_data():
    print('get_and_insert_new_data !!')
    trad = Trad()
    data = trad.get_data(number=1)
    assert len(data)> 0
    instance = data[0]
    try:
        with transaction.atomic():
            # Create or update data using Django ORM
            instance['direction'] = predict(instance)
            print('instance : ', instance)
            eur_usd = EurUsd.objects.create( 
                timestamp = instance['timestamp'],
                open = instance['open'],
                close = instance['close'],
                high = instance['high'],
                low = instance['low'],
                volume = instance['volume'],
                date = instance['date'],
                month = instance['month'],
                day = instance['day'],
                hour = instance['hour'],
                minute = instance['minute'],
                direction = instance['direction']
            )
            print('saving ...')
            print('saved instance: %s' % instance)
            # You can also update existing instances
            # instance.field = new_value
            # instance.save()
    except Exception as e:
        # Handle exceptions if needed
        print(f"Error: {e}")
    