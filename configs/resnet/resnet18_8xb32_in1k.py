_base_ = [
    '../_base_/models/resnet18_in1k.py', '../_base_/datasets/bmc_bs32.py',
    '../_base_/schedules/bmc_bs256.py', '../_base_/default_runtime.py'
]
