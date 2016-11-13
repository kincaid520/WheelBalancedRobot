import mcp4725

dacLeft  = mcp4725.MCP4725(mcp4725.ADDRESS1)
dacRight = mcp4725.MCP4725(mcp4725.ADDRESS2)

print 'dacLeft.set_voltage(0)'
dacLeft.set_voltage(0)
print 'dacLeft.set_counterclockwise()'
dacLeft.set_counterclockwise()
print 'dacRight.set_voltage(0)'
dacRight.set_voltage(0)
print 'dacRight.set_clockwise()'
dacRight.set_clockwise()
