import mcp4725

dac_left  = mcp4725.MCP4725(mcp4725.ADDRESS1)
dac_right = mcp4725.MCP4725(mcp4725.ADDRESS2)

print dac_left.setVoltage(0)
dac_left.counterclockwise()
print dac_right.setVoltage(0)
dac_right.counterclockwise()
