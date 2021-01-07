# PowerEdgeR610FanScript
Fan Speed Script for the Dell PowerEdge R610 rack server.

First enable manual fan control by doing
```
ipmitool raw 0x30 0x30 0x01 0x00
```

you can revert to auto by doing
```
ipmitool raw 0x30 0x30 0x01 0x01
```
