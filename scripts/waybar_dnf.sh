#!/bin/bash

# dnf

# 	 

# css classes
#custom-dnf-good
#custom-dnf-bad

# return {"text": "$text", "tooltip": "$tooltip", "class": "$class"}
# " Tracking dnf updates... "
# number_updates=$(dnf check-update | grep -v "Fedora" | grep -v "^[[:space:]]*$" | grep -v "Última comprobación de caducidad" | wc -l)

# print a spinner as json while the process is running
function spinner {
	local pid=$!
	local delay=0.75
	local spinstr='|/-\'
	while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
		local temp=${spinstr#?}
		echo -e "{\"text\":\"  \",\"tooltip\":\"Checking for updates\",\"class\":\"loading\"}"
		local spinstr=$temp${spinstr%"$temp"}
		sleep $delay
		printf "\b\b\b\b\b\b"
	done
	printf "    \b\b\b\b"
}

# check if there are updates and show a spinner while the process is running
function print_updates {
	number_updates=$(dnf check-update | grep -v "Fedora" | grep -v "^[[:space:]]*$" | grep -v "Última comprobación de caducidad" | wc -l)

	if [ "$number_updates" -gt 0 ]; then
		echo -e "{\"text\":\"  $number_updates\",\"tooltip\":\"$number_updates updates\",\"class\":\"bad\"}"
	else
		# tooltips are the first 10 packages
		echo -e "{\"text\":\"  \",\"tooltip\":\"No updates\",\"class\":\"good\"}"
	fi
}

# check if there are updates and show a spinner while the process is running
print_updates
# spinner
