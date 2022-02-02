import torch
import random
import logging
import numpy as np
import os
from transformers import    AutoModelForSequenceClassification,\
                            AdamW,\
                            get_scheduler

def set_seed(seed):
    """ Set all seeds to make results reproducible (deterministic mode).
        When seed is a false-y value or not supplied, disables deterministic mode. """

    if seed:
        logging.info(f"Running in deterministic mode with seed {seed}")
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        np.random.seed(seed)
        random.seed(seed)
        os.environ['PYTHONHASHSEED'] = str(seed)
    else:
        logging.info(f"Running in non-deterministic mode")

class Model():
    def __init__(self, model_name, num_epochs, length_dataloader):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels = 24, # The number of output labels--2 for binary classification.
            output_attentions = False, # Whether the model returns attentions weights.
            output_hidden_states = False, # Whether the model returns all hidden-states.
        )
        self.optimizer = AdamW(self.model.parameters(),lr = 2e-5)
        self.num_epochs = num_epochs
        self.num_training_steps = self.num_epochs * length_dataloader
        self.lr_scheduler = get_scheduler(
                                    "linear",
                                    optimizer=self.optimizer,
                                    num_warmup_steps=0,
                                    num_training_steps=self.num_training_steps
                                    )
    
    def get_model_optimizer_scheduler(self):
        return self.model, self.optimizer, self.lr_scheduler

    def get_num_training_steps(self):
        return self.num_training_steps


