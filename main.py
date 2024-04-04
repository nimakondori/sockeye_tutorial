import torch
from src.data import train_loader
from src.model import encoder, decoder
from src.model import LitAutoEncoder
import lightning as L



if __name__ == "__main__":

    assert torch.cuda.is_available(), "CUDA is not available. Installing a GPU is highly recommended."
    # print versions of torch, cuda
    print("torch version:", torch.__version__)
    print("cuda version:", torch.version.cuda)
    print("cudnn version:", torch.backends.cudnn.version())

    # Define the model
    autoencoder = LitAutoEncoder(encoder, decoder)

   # train the model 
    # (hint: here are some helpful Trainer arguments for rapid idea iteration)
    trainer = L.Trainer(limit_train_batches=500, max_epochs=100)
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)

    
    # evaluate the model 
    encoder = autoencoder.encoder
    encoder.eval()

    # embed 4 fake images!
    fake_image_batch = torch.rand(4, 28 * 28, device=autoencoder.device)
    embeddings = encoder(fake_image_batch)
    print("⚡" * 20, "\nPredictions (4 image embeddings):\n", embeddings, "\n", "⚡" * 20)




