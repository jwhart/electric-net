"""
simple test / example of the electricalnetwork library
"""

from electrical import SwitchableDevice
from electrical import ElectricalNetwork
from electrical import ElectricalSource
from electrical import ElectricalConductor
from electrical import SimpleConductorJunction

distribution = ElectricalNetwork('ABC')
testFeeder = ElectricalSource(distribution, 'Test', 13, 'kv', 'ABC')
testFeeder2 = ElectricalSource(distribution, 'Test2', 13, 'kv', 'ABC')
fuse = SwitchableDevice(distribution,'A')
fuse2 = SwitchableDevice(distribution,'A')
fuse3 = SwitchableDevice(distribution,'A')
simpleNode = SimpleConductorJunction(distribution, 'A' )
cond1 = ElectricalConductor(distribution,'ABC', testFeeder, simpleNode)
cond2 = ElectricalConductor(distribution,'ABC', fuse2, simpleNode)
cond3 = ElectricalConductor(distribution,'ABC', simpleNode, fuse3)
cond4 = ElectricalConductor(distribution,'ABC', fuse3, testFeeder2)

###  TESTFEEDER -- (cond1)-- SIMPLENODE -- (cond2) -- FUSE2
###`                             |
###                           (cond3)
###                              |
###                            FUSE3 -- (cond4) -- TESTFEEDER2


print "FUSE 3 source will all closed"
srcs = fuse3.getSources()
for src in srcs:
    print "   {0}".format(src.designation)

print "Simple Node sources "
srcs = simpleNode.getSources()
for src in srcs:
    print "   {0}".format(src.designation)


print "Fuse 3 sources after opening fuse 3"
fuse3.open(phase='all')
srcs = fuse3.getSources()
for src in srcs:
    print "   {0}".format(src.designation)

print "Simple Node sources "
srcs = simpleNode.getSources()
for src in srcs:
    print "   {0}".format(src.designation)

print "Closing"
fuse3.close(phase='all')
srcs = fuse3.getSources()
for src in srcs:
    print "   {0}".format(src.designation)
##fuse.open('B')

#print fuse


print "Opening"
fuse3.open(phase='all')
srcs = fuse3.getSources()
for src in srcs:
    print "   {0}".format(src.designation)

print "Closing"
fuse3.close(phase='all')
srcs = fuse3.getSources()
for src in srcs:
    print "   {0}".format(src.designation)
##fuse.open('B')

#print fuse