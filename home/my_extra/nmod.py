import math


def get_score(cpu, gpu, chipset):
    d_cpu = {
        'Hexa-core 2.39 GHz': 1.5,
        'Quad-core 1.4 GHz Cortex-A53': 3,
    }

    d_gpu = {
        'Adreno 512': 1.2,
        'Adreno 306': 2.3,
    }

    d_chipset = {
        'Apple A11 Bionic': 2.1,
        'Qualcomm MSM8917 Snapdragon 425': 3.3,
    }

    cpu_rt = d_cpu.get(cpu)
    gpu_rt = d_gpu.get(gpu)
    chipset_rt = d_chipset.get(chipset)

    scr = ((1 / math.pow(2, cpu_rt)) + (1 / math.pow(2, gpu_rt)) + (1 / math.pow(2, chipset_rt))) / 3

    return scr
