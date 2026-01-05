---
title: "Cloudflare ddns update shell script"
date: 2024-04-27
author: pengjianqing
categories: ['Uncategorized']
---

I am running my NAS at home, and it has the public IP, but the IP will be changed randomly, so I need to bind it to the subdomain in the Cloudflare, so I can visit it even the IP changed. So this shell script is using to update the A Record in the DNS Recording.

The script is post to the github as well

- https://gist.github.com/pjq/80fb9444a623b9540b0a48a14f202a41

```
`#!/bin/bash

# CHANGE THESE
auth_email="xxxxx@gmail.com"
auth_key="xxxxxxxx" # found in cloudflare account settings
zone_name="xxxxx"
sub_domains=("sub1" "sub2")
zone_id="your_zone_id"

# MAYBE CHANGE THESE
export HTTP_PROXY=""
export HTTPS_PROXY=""

ip_file="ip.txt"
log_file="cloudflare.log"

# Fetch IP Address
get_ip() {
    curl --noproxy '*' -s http://ipv4.icanhazip.com
}

# Log function for output and date
log() {
    if [ "$1" ]; then
        echo -e "[$(date)] - $1" >> $log_file
    fi
}

# Check for changes in IP
check_ip() {
    local ip=$1
    if [ ${ip} == "165.227.51.176" ];then
        log "It's the proxied IP address, exit."
        exit 0
    fi

    if [ -f $ip_file ]; then
        old_ip=$(cat $ip_file)
        if [ $ip == $old_ip ]; then
            log "IP has not changed."
            exit 0
        fi
    fi
}

# Modified get_identifiers function to handle separate identifier files for each subdomain
get_identifiers() {
    local sub_domain=$1
    local id_file="${sub_domain}_cloudflare.ids"  # Separate file for each subdomain
    local record_name="${sub_domain}.${zone_name}"
    local zone_identifier=
    local record_identifier=

    if [ -f $id_file ] && [ $(wc -l $id_file | cut -d " " -f 1) == 2 ]; then
        zone_identifier=$(head -1 $id_file)
        record_identifier=$(tail -1 $id_file)
    else
        zone_identifier=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=$zone_name" -H "X-Auth-Email: $auth_email" -H "Authorization: Bearer $auth_key" -H "Content-Type: application/json" | grep -Po '(? $id_file
        echo "$record_identifier" >> $id_file
    fi

    log "Fetched identifiers for $sub_domain - Zone ID: $zone_identifier, Record ID: $record_identifier"
    echo $zone_identifier $record_identifier
}

# Update Cloudflare record
update_record() {
    local zone_identifier=$1
    local record_identifier=$2
    local ip=$3
    local sub_domain=$4
    local record_name="${sub_domain}.${zone_name}"

    update=$(curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/$zone_identifier/dns_records/$record_identifier" -H "X-Auth-Email: $auth_email" -H "Authorization: Bearer $auth_key" -H "Content-Type: application/json" --data "{\"id\":\"$zone_identifier\",\"type\":\"A\",\"name\":\"$record_name\",\"content\":\"$ip\"}")

    if [[ $update == *"\"success\":false"* ]]; then
        message="API UPDATE FAILED for $sub_domain. DUMPING RESULTS:\n$update"
        log "$message"
        echo -e "$message"
        exit 1
    else
        message="IP changed to: $ip for $sub_domain"
        echo "$ip" > $ip_file
        log "$message"
        echo "$message"
    fi
}

# Script execution starts here
log "Check Initiated"
ip=$(get_ip)

check_ip $ip

for sub_domain in "${sub_domains[@]}"; do
    log "Processing $sub_domain"
    identifiers=($(get_identifiers $sub_domain))
    update_record ${identifiers[0]} ${identifiers[1]} $ip $sub_domain
done`
```