time python -m src.autoencoder data/avery/GSE37199/clinical.csv -o
data/avery/GSE37199/clinical_pretrained_10000_confounded.csv -b plate -r data/gpl570/checkpoints/weights.ckpt -i 10000
time python -m src.autoencoder data/avery/GSE37199/clinical.csv -o
data/avery/GSE37199/clinical_pretrained_1000_confounded.csv -b plate -r data/gpl570/checkpoints/weights.ckpt -i 1000
time python -m src.autoencoder data/avery/GSE37199/clinical.csv -o
data/avery/GSE37199/clinical_pretrained_100_confounded.csv -b plate -r data/gpl570/checkpoints/weights.ckpt -i 100
time python -m src.autoencoder data/avery/GSE37199/clinical.csv -o
data/avery/GSE37199/clinical_pretrained_confounded.csv -b plate -r data/gpl570/checkpoints/weights.ckpt -i 0
