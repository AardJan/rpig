import board
import adafruit_mcp3xxx.mcp3008 as MCP

def get_pin_MCP(pin_value):
    if pin_value == "P0":
        return MCP.P0
    elif pin_value == "P1":
        return MCP.P1
    elif pin_value == "P2":
        return MCP.P2    
    elif pin_value == "P3":
        return MCP.P3
    elif pin_value == "P4":
        return MCP.P4
    elif pin_value == "P5":
        return MCP.P5
    elif pin_value == "P6":
        return MCP.P6
    elif pin_value == "P7":
        return MCP.P7
    elif pin_value == "P8":
        return MCP.P8
    else:
        raise "Wrong ping number"

def get_pin_board(pin_value):
    if pin_value == "D0":
        return board.D0
    elif pin_value == "D1":
        return board.D1 , 
    elif pin_value == "D2":
        return board.D2
    elif pin_value == "D3":
        return board.D3
    elif pin_value == "D4":
        return board.D4
    elif pin_value == "D5":
        return board.D5
    elif pin_value == "D6":
        return board.D6
    elif pin_value == "D7":
        return board.D7
    elif pin_value == "D8":
        return board.D8
    elif pin_value == "D9":
        return board.D9
    elif pin_value == "D10":
        return board.D10
    elif pin_value == "D11":
        return board.D11
    elif pin_value == "D12":
        return board.D12
    elif pin_value == "D13":
        return board.D13
    elif pin_value == "D14":
        return board.D14
    elif pin_value == "D15":
        return board.D15
    elif pin_value == "D16":
        return board.D16
    elif pin_value == "D17":
        return board.D17
    elif pin_value == "D18":
        return board.D18
    elif pin_value == "D19":
        return board.D19
    elif pin_value == "20":
        return board.D20
    elif pin_value == "D21":
        return board.D21
    elif pin_value == "D22":
        return board.D22
    elif pin_value == "D23":
        return board.D23
    elif pin_value == "D24":
        return board.D24
    elif pin_value == "D25":
        return board.D25
    elif pin_value == "D26":
        return board.D26
    elif pin_value == "D27":
        return board.D27