# MCP Development Project

This project demonstrates Model Context Protocol (MCP) implementation with a calculator server and client that can interact with GUI applications.

## Project Structure

### Core Files

#### `example_mcp_server.py`
FastMCP server providing mathematical tools and GUI automation capabilities:

**Mathematical Tools:**
- Basic operations: `add`, `subtract`, `multiply`, `divide`
- Advanced math: `power`, `sqrt`, `cbrt`, `factorial`, `log`
- Trigonometry: `sin`, `cos`, `tan`
- List operations: `add_list`
- String operations: `strings_to_chars_to_int` - converts string characters to ASCII values
- `int_list_to_exponential_sum` - calculates sum of exponentials
- `fibonacci_numbers` - generates Fibonacci sequence

**GUI Automation Tools (Pinta):**
- `open_paint` - Opens Pinta image editor in fullscreen
- `draw_rectangle` - Draws rectangles using xdotool
- `add_text_in_paint` - Adds text at specified coordinates

**Resources:**
- `greeting://{name}` - Dynamic greeting resource

**Prompts:**
- `review_code` - Code review prompt
- `debug_error` - Error debugging prompt

#### `talk2mcp.py`
MCP client that connects to the server and executes multi-step mathematical operations using Gemini LLM:

**Features:**
- Connects to `example_mcp_server.py` via stdio transport
- Uses Gemini 2.0 Flash for agentic reasoning
- Iterative task execution (max 3 iterations)
- Automatic GUI automation when final answer is reached
- Timeout handling for LLM requests

**Example Query:**
```python
query = "Find the ASCII values of characters in INDIA and then return sum of exponentials of those values."
```

**Workflow:**
1. LLM analyzes available tools
2. Makes function calls: `FUNCTION_CALL: strings_to_chars_to_int|INDIA`
3. Processes results iteratively
4. Returns final answer and displays in Pinta

### Helper Scripts

#### `mouse_tracker.py`
Utility to track mouse position in real-time:
- Prints mouse coordinates every 3 seconds
- Useful for finding GUI element coordinates for automation
- Requires tkinter support

**Usage:**
```bash
source .venv/bin/activate
python mouse_tracker.py
```

#### `open_pinta.py`
Standalone script to open Pinta on a specific display:
- Sets DISPLAY environment variable to `:1`
- Opens Pinta image editor
- Verifies the process started successfully

**Usage:**
```bash
python open_pinta.py
```

## Setup

### Prerequisites

1. **Python 3.11** with tkinter support
2. **System packages:**
   ```bash
   sudo apt-get install xdotool wmctrl pinta
   ```

3. **Python environment:**
   ```bash
   # Create venv with Linuxbrew Python (has tkinter)
   /home/linuxbrew/.linuxbrew/opt/python@3.11/bin/python3.11 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Environment variables:**
   Create `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   DISPLAY=:1
   ```

### Dependencies

```
mcp
python-dotenv
google-generativeai
pyautogui
Pillow
```

## Running the Project

### 1. Start the MCP client with agentic workflow:

```bash
source .venv/bin/activate
python talk2mcp.py
```

This will:
- Connect to the MCP server
- Execute the query using Gemini LLM
- Call mathematical functions iteratively
- Display results in Pinta when complete

### 2. Use helper scripts:

**Track mouse position:**
```bash
source .venv/bin/activate
python mouse_tracker.py
# Move mouse to desired location, note coordinates
# Press Ctrl+C to stop
```

**Open Pinta manually:**
```bash
python open_pinta.py
```

## How It Works

### MCP Communication Flow

```
talk2mcp.py (Client)
    �
StdioServerParameters
    �
example_mcp_server.py (Server)
    �
FastMCP Tools
    �
Pinta GUI / Math Operations
```

### Agentic Workflow Example

Given query: "Find ASCII values of INDIA and sum their exponentials"

**Iteration 1:**
```
LLM � FUNCTION_CALL: strings_to_chars_to_int|INDIA
Server � [73, 78, 68, 73, 65]
```

**Iteration 2:**
```
LLM � FUNCTION_CALL: int_list_to_exponential_sum|73,78,68,73,65
Server � 5.891618587355098e+33
```

**Iteration 3:**
```
LLM � FINAL_ANSWER: [5.891618587355098e+33]
Actions: open_paint � draw_rectangle � add_text_in_paint
```

## Troubleshooting

### Tkinter Issues
If you get "No module named '_tkinter'":
```bash
# Ensure using Linuxbrew Python with tkinter
brew list | grep python
# Should show: python-tk@3.11

# Recreate venv with correct Python
rm -rf .venv
/home/linuxbrew/.linuxbrew/opt/python@3.11/bin/python3.11 -m venv .venv
```

### Process Cleanup Warnings
Asyncio subprocess cleanup warnings are harmless but can be minimized by:
- Using `atexit` handlers (already implemented)
- Allowing cleanup sleep time (already implemented)

### GUI Automation
- Use `mouse_tracker.py` to find exact coordinates
- Adjust coordinates in `example_mcp_server.py` tool functions
- Ensure `DISPLAY` environment variable is set correctly

## License

MIT
