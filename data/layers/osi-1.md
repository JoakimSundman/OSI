---
number: 1
name: Physical
pdu: Bit
protocols: []
---

## Summary

The physical layer specifies how data is transmitted physically from one device to another. 

## Main

The physical layer is the first layer of the OSI model and is responsible for the physical connection between devices. The physical medium can be copper (electrical), fiber (optical), Wi-Fi (RF). The specification of layer 1 defines the transmission and reception of raw bit streams between a device and a shared physical medium. There are no device addresses in layer 1, meaning that all connected devices receive the same data. A consequence of this is that only one device can transmit at a time. If more than one does, a collision occurs. A collision will corrupt the transmitted data, rendering it all useless. Layer 1 has no way of detecting collisions or controlling the media access on its own, that is left to the layer above (Layer 2 Data link).

The physical layer is still fundamental as it defines and represents how devices communicate physically.

## Troubleshooting

Depends on the medium, if it's cable check the it's fully connected and is not loose in any ports. Otherwise test with another cable as the cable could also be the problem.
If the medium is Wi-Fi then checking the connection on the device side is necessary to determine where the network is breaking. A possible problem could also be the networking card on the device itself. 

## Security

- Physical access to ports, cables, and connected devices.

## Examples

### The immovable file

The network just went down and took the router with it. You need to move a file from your workstation to your laptop, and nobody has a USB stick. Connecting the two devices with an Ethernet cable gives the data a physical medium to travel across: layer 1 can now carry bits from one machine to the other.

That alone is not enough to transfer the file. The computers still need addresses, a way to package the data, and a program to send it. Those jobs belong to the layers above.

### The HUB

You want to connect 4 devices together to share a session for gaming. However this is not possible using only one cable as its limited to 2 devices. So instead you use a hub which can connect all 4 devices physically. As mentioned in the main text, with only the first layer of the network stack this gaming session would still not be possible as collisions would happen all the time, but atleast with the hub all 4 devices are connected and with added layers a gaming session is possible. 

Hubs are rare today and have generally been replaced by switches. 