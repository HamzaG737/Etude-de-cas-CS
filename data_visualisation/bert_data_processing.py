import pandas as pd

test_data = pd.read_csv('Data/testset_sent.csv')
train_data = pd.read_csv('Data/trainset_sent.csv')

train_data_list = []

for line in train_data.to_dict('records'):
  text = line['text']
  pol = text['polarity']
  encoded = encode_text(text)
  train_data_list += [[encoded['input_ids'], encoded['attention_mask'], pol]]

train_preprocessed = pd.DataFrame(train_data_list, columns=['input_ids', 'attention_mask', 'polarity'])
