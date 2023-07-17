#!/bin/bash

function usage {
	used=$(nvidia-settings -t -q [gpu:0]/UsedDedicatedGPUMemory)
	total=$(nvidia-settings -t -q [gpu:0]/TotalDedicatedGPUMemory)
	awk "BEGIN {printf \"%.0f\", $used/$total*100}"
}

function temperature {
	nvidia-settings -t -q [gpu:0]/GPUCoreTemp
}

# return: { "text": "50", "tooltip": "Temperature: 50°C 50%" }

echo "{\"text\":\"$(usage)\", \"tooltip\":\"Temperature: $(temperature)°C\"}"
