{
    "experiment_group": "experiment_group_name",
    "experiments": [
            {
            "experiment_name":"experiment_name_1",
            "dataset": "ConversionDataset",
            "network": "ranking_network",
            "model": "RankingTrainer",
            "dataset_args": {
                "data_arg_1": 200000,
                "data_arg_2": "test_arg",
                "data_arg_3": ["feat_1", "feat_2", "feat_3", "feat_4"]
                },
            "dataset_args": {
                "net_arg_1": 200000,
                "net_arg_2": "test_arg",
                "net_arg_3": ["feat_1", "feat_2", "feat_3", "feat_4"]
            },
            "train_args": {
                "train_arg_1": 200000,
                "train_arg_2": "test_arg",
                "train_arg_3": ["feat_1", "feat_2", "feat_3", "feat_4"]
            }
        }
    ]
}