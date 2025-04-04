

from datasets import load_dataset

dataset = load_dataset("daily_dialog" , trust_remote_code=True)

# Veri kümesinin ilk örneğine bakalım
print(dataset["train"].column_names)

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["act"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

import torch
from torch import nn
from transformers import BertModel

class SimpleChatbot(nn.Module):
    def __init__(self):
        super(SimpleChatbot, self).__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")
        self.fc = nn.Linear(768, 30522)  # BERT'in kelime tahmini yaptığı vektör boyutu

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask=attention_mask)
        return self.fc(outputs.last_hidden_state)

# Modeli oluştur
model = SimpleChatbot()

from torch.utils.data import DataLoader
from torch.optim import Adam

# Eğitim verisini DataLoader'a dönüştür
train_dataloader = DataLoader(tokenized_datasets["train"], batch_size=8, shuffle=True)

# Optimizasyon ve kayıp fonksiyonu
optimizer = Adam(model.parameters(), lr=5e-5)
loss_fn = nn.CrossEntropyLoss()

# Modeli GPU'da çalıştır (mümkünse)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Eğitim döngüsü
for epoch in range(3):  # 3 Epoch boyunca eğit
    for batch in train_dataloader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask)
        loss = loss_fn(outputs.view(-1, 30522), labels.view(-1))
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1} loss: {loss.item()}")

def sohbet_et(metin):
    inputs = tokenizer(metin, return_tensors="pt").to(device)
    outputs = model(**inputs)
    yanit = tokenizer.decode(torch.argmax(outputs.logits, dim=-1)[0], skip_special_tokens=True)
    return yanit

print(sohbet_et("Nasılsın?"))
