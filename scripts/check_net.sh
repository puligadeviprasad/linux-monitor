#!/bin/bash
CONNS=$(ss -t | grep ESTABLISHED | wc -l)
echo "[$(date +%H:%M:%S)] Active TCP connections: $CONNS"
echo "$(date): NET_CONNS $CONNS" >> logs/network.log
