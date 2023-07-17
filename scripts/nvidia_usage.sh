#!/bin/bash

used=$(nvidia-settings -t -q [gpu:0]/UsedDedicatedGPUMemory)
total=$(nvidia-settings -t -q [gpu:0]/TotalDedicatedGPUMemory)
awk "BEGIN {printf \"%.0f\", $used/$total*100}"
