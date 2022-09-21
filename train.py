from train_val_cls import main as train_main


train_main([    '--path=/media/data/datasets/ShapeNet/train_files.txt',
                '--path_val=/media/data/datasets/ShapeNet/test_files.txt',
                '--save_folder=models/cls/',
                '--model=pointcnn_cls',
                '--setting=modelnet_x3_l4',
                '--no_code_backup'
           ])