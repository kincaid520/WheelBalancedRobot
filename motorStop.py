import mcp4725

dac_left  = mcp4725.MCP4725(mcp4725.ADDRESS1)# only work w/ rotation direction
dac_right = mcp4725.MCP4725(mcp4725.ADDRESS2)# work w/ all func

print 'dac_left.setVoltage(0)'
dac_left.setVoltage(2)
print 'dac_left.counterclockwise()'
dac_left.counterclockwise()
print 'dac_right.setVoltage(0)'
dac_right.setVoltage(2)
print 'dac_right.clockwise()'
dac_right.clockwise()
