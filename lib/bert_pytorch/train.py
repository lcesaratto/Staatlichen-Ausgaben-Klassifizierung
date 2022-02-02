# from tqdm.auto import tqdm
from datasets import load_metric
import torch

from lib.bert_pytorch.model_preparation import Model, set_seed
from lib.bert_pytorch.helper_functions import get_device
from lib.bert_pytorch.data_preparation import get_dataloaders


def train_model_on_train_data(TRAIN_DATA_PATH, MODEL_NAME, BATCH_SIZE, NUM_EPOCHS, SEED=42):

    set_seed(SEED)

    train_dataloader, validation_dataloader = get_dataloaders(TRAIN_DATA_PATH, 
                                                                MODEL_NAME, 
                                                                BATCH_SIZE,
                                                                create_validation_set = True,
                                                                )

    model_class = Model(MODEL_NAME, NUM_EPOCHS, len(train_dataloader))
    model, optimizer, lr_scheduler = model_class.get_model_optimizer_scheduler()

    device = get_device()

    model = model.to(device)

    # progress_bar = tqdm(range(model_class.get_num_training_steps()))

    training_stats = []

    try:
        for epoch in range(NUM_EPOCHS):
            print(f"EPOCH {epoch+1}/{NUM_EPOCHS}\n")
            model.train()
            total_train_loss = 0

            for step, batch in enumerate(train_dataloader):
                model.zero_grad()
                parameters = {
                    "input_ids" : batch[0].to(device),
                    "attention_mask" :  batch[1].to(device), 
                    "labels" : batch[2].to(device)
                }
                outputs = model(**parameters)

                loss = outputs.loss
                total_train_loss += loss.item()
                loss.backward()

                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

                optimizer.step()
                lr_scheduler.step()
                optimizer.zero_grad()
                # progress_bar.update(1)

                if step % 100 == 0 and step != 0:
                    print(f"BATCH {step}/{len(train_dataloader)}:\tTraining loss({loss.item()})")

            training_stats.append({
                "epoch":epoch+1,
                "training_loss":total_train_loss/len(train_dataloader)
                })

            total_val_loss = 0
            metric = load_metric("f1")

            model.eval()
            for batch in validation_dataloader:

                parameters = {
                    "input_ids" : batch[0].to(device),
                    "attention_mask" :  batch[1].to(device), 
                    "labels" : batch[2].to(device)
                }
                with torch.no_grad():
                    outputs = model(**parameters)

                logits = outputs.logits
                loss = outputs.loss
                total_val_loss += loss.item()

                predictions = torch.argmax(logits, dim=-1)
                metric.add_batch(predictions=predictions, references=parameters["labels"])

            training_stats[epoch]["validation_loss"] = total_val_loss/len(validation_dataloader)
            training_stats[epoch]["validation_f1_score"] = metric.compute(average='weighted')

            print(f"\nAvg training loss:    {training_stats[epoch]['training_loss']}")
            print(f"Avg validation loss:  {training_stats[epoch]['validation_loss']}")
            print(f"F1 validation score:  {training_stats[epoch]['validation_f1_score']}\n")

    except RuntimeError as e:
        print(e)
    
    return model, training_stats


def train_model_on_full_train_data(TRAIN_DATA_PATH, MODEL_NAME, BATCH_SIZE, NUM_EPOCHS, SEED=42):

    set_seed(SEED)

    train_dataloader= get_dataloaders(TRAIN_DATA_PATH, 
                                        MODEL_NAME, 
                                        BATCH_SIZE,
                                        create_validation_set = False,
                                        )

    model_class = Model(MODEL_NAME, NUM_EPOCHS, len(train_dataloader))
    model, optimizer, lr_scheduler = model_class.get_model_optimizer_scheduler()

    device = get_device()

    model = model.to(device)

    training_stats = []

    try:
        for epoch in range(NUM_EPOCHS):
            print(f"EPOCH {epoch+1}/{NUM_EPOCHS}\n")
            model.train()
            total_train_loss = 0

            for step, batch in enumerate(train_dataloader):
                model.zero_grad()
                parameters = {
                    "input_ids" : batch[0].to(device),
                    "attention_mask" :  batch[1].to(device), 
                    "labels" : batch[2].to(device)
                }
                outputs = model(**parameters)

                loss = outputs.loss
                total_train_loss += loss.item()
                loss.backward()

                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

                optimizer.step()
                lr_scheduler.step()
                optimizer.zero_grad()

                if step % 100 == 0 and step != 0:
                    print(f"BATCH {step}/{len(train_dataloader)}:\tTraining loss({loss.item()})")

            training_stats.append({
                "epoch":epoch+1,
                "training_loss":total_train_loss/len(train_dataloader)
                })

            print(f"\nAvg training loss:    {training_stats[epoch]['training_loss']}")

    except RuntimeError as e:
        print(e)
    
    return model, training_stats