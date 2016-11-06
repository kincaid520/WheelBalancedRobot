import mcp4725

dacLeft  = mcp4725.MCP4725(mcp4725.ADDRESS1)
dacRight = mcp4725.MCP4725(mcp4725.ADDRESS2)

print 'dac_left.setVoltage(0)'
dacLeft.set_voltage(2)
print 'dac_left.counterclockwise()'
dacLeft.counterclockwise()
print 'dac_right.setVoltage(0)'
dacRight.set_voltage(2)
print 'dac_right.clockwise()'
dacRight.clockwise()
