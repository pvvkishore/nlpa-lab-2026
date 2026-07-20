# NLPA Lab 2026 — Setup Guide

**Natural Language Processing Applications Laboratory**
**Koneru Lakshmaiah Education Foundation**

---

This guide takes you from a fresh Windows laptop to running your
first tokenization lab with a local AI assistant. No cloud APIs.
No internet cost. Everything runs on your own machine.

**Estimated time**: 60–90 minutes for the full setup (mostly
downloads). You only do this once.

**What you will have at the end**:

- A local AI model (Qwen2.5-Coder) running on your GPU
- JupyterLab configured for the NLP labs
- A chat widget inside your notebooks that lets you ask Qwen
  questions about your code and outputs
- Everything working **offline** after setup

---

## Table of contents

- **Phase 1** — Check your laptop meets requirements
- **Phase 2** — Install Anaconda (Python + JupyterLab)
- **Phase 3** — Install Ollama (the local AI runtime)
- **Phase 4** — Download the AI models
- **Phase 5** — Download the lab files
- **Phase 6** — Create the Python environment
- **Phase 7** — Build the chat helper file
- **Phase 8** — First run: verify everything works
- **Phase 9** — How to use the lab notebooks
- **Appendix A** — Troubleshooting common problems
- **Appendix B** — Freeing your GPU for training

---

# Phase 1 — Check your laptop

Before installing anything, verify your laptop can run this lab.

## 1.1 Hardware requirements

| Component | Minimum | Recommended |
|---|---|---|
| **OS** | Windows 10 (build 1903+) | Windows 11 |
| **RAM** | 8 GB | 16 GB |
| **GPU** | NVIDIA GPU with 6 GB VRAM | NVIDIA GPU with 8 GB+ VRAM |
| **Disk** | 20 GB free | 40 GB free |
| **Internet** | For setup only | — |

Without an NVIDIA GPU, the labs will still run but AI responses
will be much slower (30-60 seconds per answer instead of 5-10).

## 1.2 Check your Windows version

1. Press **Win + R** on your keyboard
2. Type `winver` and press Enter
3. A window opens showing your Windows version

You need **Windows 10 version 1903 or later**, or any version of
Windows 11.

## 1.3 Check your GPU

1. Press **Win + X** and select **Device Manager**
2. Expand **Display adapters**
3. Look for a line starting with **NVIDIA GeForce** or
   **NVIDIA Quadro**

If you see one, note the model name (e.g. "GTX 1070", "RTX 3060").
If you see only "Intel HD Graphics" or "AMD Radeon", you don't
have an NVIDIA GPU — the labs will run on CPU but slowly.

## 1.4 Check your disk space

1. Open **File Explorer** (Win + E)
2. Click **This PC** on the left
3. Look at your C: drive

You need at least **20 GB free on C:**. If you have less, free
up space now (delete old downloads, uninstall unused apps).

## Phase 1 complete when...

- You know your Windows version is 10 (1903+) or 11
- You know whether you have an NVIDIA GPU
- You have at least 20 GB free on C:

---

# Phase 2 — Install Anaconda

Anaconda is a Python distribution that includes conda (a package
manager) and Jupyter. We use it because it handles Python
versions and library conflicts cleanly.

## 2.1 Download Anaconda

1. Open your web browser
2. Go to: **https://www.anaconda.com/download**
3. Click the big green **Download** button for Windows
4. You may be asked for your email — you can skip this by
   clicking "No thanks, just download"
5. The installer file (~800 MB) downloads to your Downloads
   folder. Filename looks like:
   `Anaconda3-2026.02-Windows-x86_64.exe`

## 2.2 Run the Anaconda installer

1. Open **File Explorer** → **Downloads**
2. Double-click the `Anaconda3-...exe` file
3. If Windows shows a security warning, click **More info** →
   **Run anyway**

## 2.3 Installer settings — important choices

Click through the installer with these choices:

- **Welcome screen**: Next
- **License Agreement**: I Agree
- **Installation Type**: **Just Me** (recommended)
- **Destination Folder**: Accept default
  (`C:\Users\YOUR_NAME\anaconda3`)
- **Advanced Installation Options** — ⚠️ **read carefully**:
    - ☐ **Add Anaconda3 to my PATH environment variable**
      (leave unchecked — Anaconda recommends this)
    - ☑ **Register Anaconda3 as my default Python 3.11**
      (check this)
    - ☑ **Clear the package cache upon completion** (check this)

Click **Install**. Takes 5-10 minutes.

At the end, click **Next**, then **Finish**. You can uncheck
the "Anaconda Tutorial" boxes.

## 2.4 Verify Anaconda installed correctly

1. Press **Win**, type `anaconda prompt`, press Enter
2. A dark terminal window opens
3. The prompt should start with `(base)` — for example:
   `(base) C:\Users\Dr.PVVK>`

Type this and press Enter:

```
conda --version
```

You should see something like `conda 24.11.3`.

Type this next:

```
python --version
```

You should see `Python 3.11.x` (any 3.11 version is fine).

## Phase 2 complete when...

- Anaconda Prompt opens
- `conda --version` prints a version number
- `python --version` prints Python 3.11.x

---

# Phase 3 — Install Ollama

Ollama is what actually runs the AI model on your machine. It
listens for requests on your laptop and returns AI-generated
responses.

## 3.1 Download the Ollama installer

1. Open your web browser
2. Go to: **https://ollama.com/download**
3. Click **Download for Windows**
4. The file `OllamaSetup.exe` (~1.4 GB) downloads to your
   Downloads folder

## 3.2 Run the Ollama installer

1. Open **File Explorer** → **Downloads**
2. Double-click `OllamaSetup.exe`
3. If Windows SmartScreen warns you, click **More info** →
   **Run anyway**
4. The installer has a single **Install** button — click it
5. Installation takes 30-60 seconds
6. When done, the installer closes itself
7. You should see a **llama icon** appear in your system tray
   (bottom-right corner of your screen, near the clock)

## 3.3 Verify Ollama is running

1. Open a **new Anaconda Prompt** (Win → type `anaconda
   prompt` → Enter)

2. Type this and press Enter:

```
ollama --version
```

You should see something like `ollama version is 0.30.11`.

3. Then type this:

```
curl http://localhost:11434
```

You should see the text `Ollama is running` on the next line.

If both work, Ollama is installed and its background service
is active.

## 3.4 Configure Ollama (optional, but recommended)

By default, Ollama stores its models on your C: drive. If C: is
tight on space, move the storage to D: (or wherever you have
more space):

1. Press **Win**, type `environment variables`, click
   **Edit the system environment variables**
2. In the window that opens, click **Environment Variables...**
3. Under **User variables**, click **New...**
4. Variable name: `OLLAMA_MODELS`
5. Variable value: `D:\ollama_models` (or your preferred path)
6. Click **OK** three times to save

Then create the folder — in Anaconda Prompt:

```
mkdir D:\ollama_models
```

Then **quit Ollama** (right-click the llama icon in system
tray → Quit) and start it again from the Start menu. It will
now use D: for models.

## 3.5 Configure Ollama for offline use

1. Click the llama icon in your system tray → click the
   Ollama window that opens
2. Click **Settings** (gear icon in the sidebar)
3. Turn OFF these two toggles:
    - ☐ **Cloud** (Enable cloud models and web search)
    - ☐ **Auto-download updates**
4. Leave OFF: **Expose Ollama to the network** (security)
5. Confirm the **Model location** shows `D:\ollama_models`
   (or wherever you set it)

## Phase 3 complete when...

- `ollama --version` prints a version
- `curl http://localhost:11434` prints "Ollama is running"
- Cloud and Auto-download-updates are turned off in Settings

---

# Phase 4 — Download the AI models

Ollama can run many models. For this lab we need three:

| Model | Size | Purpose |
|---|---|---|
| `qwen2.5-coder:7b` | 4.7 GB | Main chat model (fast, capable) |
| `qwen2.5-coder:1.5b` | 986 MB | Smaller model for comparison |
| `nomic-embed-text` | 274 MB | Embeddings (used in later labs) |

Total: about 6 GB.

## 4.1 Pull the first model

In Anaconda Prompt:

```
ollama pull qwen2.5-coder:7b
```

This downloads the 4.7 GB model. Time depends on your
connection — expect 10-30 minutes. You'll see a progress bar.

**If the download stalls or fails**: press Ctrl+C, then run
the command again. Ollama resumes from where it stopped.

When done, you'll see the word `success` on its own line.

## 4.2 Pull the other two models

```
ollama pull qwen2.5-coder:1.5b
```

Then:

```
ollama pull nomic-embed-text
```

Both are small, together take 2-5 minutes.

## 4.3 Verify all three models are present

```
ollama list
```

You should see three rows — one per model — with their sizes
and modification times.

## 4.4 Test that the AI actually runs

```
ollama run qwen2.5-coder:7b "Say hello in five words."
```

Wait 3-5 seconds — the model loads into your GPU's memory the
first time. Then you'll see a short response like:

```
Hello! How are you today?
```

Type `/bye` and press Enter to exit.

## Phase 4 complete when...

- `ollama list` shows three models
- The test command produced a short reply
- No error messages

---

# Phase 5 — Download the lab files

The lab notebooks, environment file, and setup scripts are
distributed via GitHub. You will download them as a ZIP file
(no Git installation needed).

## 5.1 Download the ZIP

1. Open your web browser
2. Go to: **https://github.com/pvvkishore/nlpa-lab-2026**

   (Your instructor will announce the actual URL in class.)

3. Click the green **Code** button (top-right of the file list)
4. Click **Download ZIP** at the bottom of the dropdown menu
5. The file `nlpa-lab-2026-main.zip` downloads to your
   Downloads folder

## 5.2 Extract the ZIP

1. Open **File Explorer** → **Downloads**
2. Right-click `nlpa-lab-2026-main.zip`
3. Select **Extract All...**
4. In the "Extract to" field, type or browse to a location
   you'll remember. Recommended:
   ```
   C:\Users\YOUR_NAME\NLPA_LAB_2026
   ```
5. Uncheck "Show extracted files when complete"
6. Click **Extract**

## 5.3 Verify the files are there

In Anaconda Prompt:

```
dir C:\Users\%USERNAME%\NLPA_LAB_2026
```

(The `%USERNAME%` automatically expands to your Windows user.)

You should see files including:

```
environment.yml
setup_data.py
README.md
01a_tokenization_classical.ipynb
01b_tokenization_learned.ipynb
```

## Phase 5 complete when...

- The lab folder exists at
  `C:\Users\YOUR_NAME\NLPA_LAB_2026`
- The folder contains `environment.yml` and the notebook files

---

# Phase 6 — Create the Python environment

Now we create a dedicated Python environment for the lab. This
keeps the lab's libraries isolated from anything else on your
machine.

## 6.1 Navigate to the lab folder

In Anaconda Prompt:

```
cd C:\Users\%USERNAME%\NLPA_LAB_2026
```

Your prompt should now show that path.

## 6.2 Create the environment from the YAML file

```
conda env create -f environment.yml
```

This reads `environment.yml` and installs Python 3.11 plus all
required libraries: JupyterLab, ollama, transformers, spaCy,
NLTK, Stanza, and more.

Takes 5-10 minutes. You'll see many "Downloading..." and
"Installing..." messages. Some warnings are normal.

When done, you'll see:

```
done
#
# To activate this environment, use
#
#     $ conda activate nlpa_2026
#
```

## 6.3 Activate the new environment

```
conda activate nlpa_2026
```

Your prompt should change from `(base)` to `(nlpa_2026)`.

**Important**: from now on, whenever you open Anaconda Prompt
to work on this lab, first run `conda activate nlpa_2026` to
switch to the lab's environment.

## 6.4 Download the data files

Some libraries need extra data (spaCy's English model, Stanza's
models, HuggingFace tokenizer files). Run the setup script:

```
python setup_data.py
```

This downloads about 600 MB. Takes 5-15 minutes depending on
your connection. You'll see progress bars for each download.

When done, you'll see:

```
Setup complete. All tokenizers are ready to use offline.
```

## 6.5 Verify the environment works

```
python -c "from ollama import Client; c = Client(host='http://localhost:11434'); print([m.model for m in c.list().models])"
```

You should see a list of your three Ollama models:

```
['nomic-embed-text:latest', 'qwen2.5-coder:1.5b', 'qwen2.5-coder:7b']
```

## Phase 6 complete when...

- Your prompt shows `(nlpa_2026)` when activated
- `setup_data.py` finished with "Setup complete"
- The Python one-liner prints your three model names

---

# Phase 7 — Build the chat helper file

The lab notebooks use a helper file called `nlpa_chat.py` that
provides a chat widget for talking to Qwen inside notebooks.
You will create this file yourself — this teaches you what's
inside and how it works.

## 7.1 Open a text editor

We'll use Windows Notepad — simple and always available.

In Anaconda Prompt (still in the NLPA_LAB_2026 folder):

```
notepad nlpa_chat.py
```

Notepad opens with a blank file. If Notepad asks whether to
create the file, click **Yes**.

## 7.2 Paste the helper code

Copy the entire block below (all ~110 lines) and paste it
into Notepad.

**Important**: use "Paste" from Notepad's Edit menu (or press
Ctrl+V) — do not type it by hand, you'll make mistakes.

```python
"""
NLPA Lab 2026 — Local Qwen chat widget with cell-referencing.

Usage in any lab notebook:
    from nlpa_chat import chat
    chat()

Then in the widget, ask questions like:
    - "why did wasn't split into three tokens?"    (normal chat)
    - "@cell 5 explain the output"                 (references cell 5)
    - "@3 what does this code do?"                 (@N is shorthand)
    - "@last why is this the answer?"              (last-run cell)
"""

import re
import sys
from io import StringIO
from ollama import Client
import ipywidgets as widgets
from IPython.display import display
from IPython import get_ipython

_client = Client(host='http://localhost:11434')
_captured = {}
_last_exec = [0]
_buf = [None]
_orig_stdout = [None]


class _Tee:
    def __init__(self, real, buf):
        self.real = real
        self.buf = buf
    def write(self, s):
        self.real.write(s)
        self.buf.write(s)
        return len(s)
    def flush(self):
        self.real.flush()


def _pre_run(info):
    _buf[0] = StringIO()
    _orig_stdout[0] = sys.stdout
    sys.stdout = _Tee(sys.stdout, _buf[0])


def _post_run(result):
    if _orig_stdout[0] is not None:
        sys.stdout = _orig_stdout[0]
    n = result.execution_count
    if n is not None and _buf[0] is not None:
        _captured[n] = _buf[0].getvalue()
        _last_exec[0] = n
    _buf[0] = None
    _orig_stdout[0] = None


def _install_capture():
    ip = get_ipython()
    if ip is None or getattr(ip, '_nlpa_capture_installed', False):
        return
    ip.events.register('pre_run_cell', _pre_run)
    ip.events.register('post_run_cell', _post_run)
    ip._nlpa_capture_installed = True


def _resolve_cell_refs(msg):
    ip = get_ipython()
    def replace(m):
        ref = m.group(1).lower()
        if 'last' in ref:
            n = _last_exec[0]
        else:
            n = int(re.search(r'\d+', ref).group())
        try:
            code = ip.user_ns['In'][n]
        except (IndexError, KeyError):
            code = '(cell not found)'
        out = _captured.get(n, '(no output captured)')
        return f"\n\n[Cell {n} code]\n{code}\n\n[Cell {n} output]\n{out}\n\n"
    pattern = r'@(cell\s*\d+|\d+|last)'
    return re.sub(pattern, replace, msg, flags=re.IGNORECASE)


def chat():
    _install_capture()
    inp = widgets.Textarea(
        placeholder="Ask Qwen — use @cell N to reference a cell",
        layout=widgets.Layout(width='100%', height='60px'),
    )
    model = widgets.Dropdown(
        options=['qwen2.5-coder:7b', 'qwen2.5-coder:1.5b'],
        value='qwen2.5-coder:7b',
        description='Model:',
    )
    ask = widgets.Button(description='Ask', button_style='primary',
                         icon='paper-plane')
    clear = widgets.Button(description='Clear', button_style='warning',
                           icon='trash')
    out = widgets.Output(
        layout=widgets.Layout(
            border='1px solid #ccc',
            padding='10px',
            max_height='400px',
            overflow_y='auto',
        )
    )

    def on_ask(_):
        q = inp.value.strip()
        if not q:
            return
        expanded = _resolve_cell_refs(q)
        with out:
            print(f"\n>>> You ({model.value}):\n{q}\n\n<<< Qwen:")
            for chunk in _client.chat(
                model=model.value,
                messages=[{'role': 'user', 'content': expanded}],
                stream=True,
            ):
                print(chunk.message.content, end='', flush=True)
            print("\n" + "-" * 60)
        inp.value = ''

    def on_clear(_):
        out.clear_output()

    ask.on_click(on_ask)
    clear.on_click(on_clear)
    display(widgets.VBox([widgets.HBox([model, ask, clear]),
                          inp, out]))
    return None
```

## 7.3 Save and close

1. Press **Ctrl+S** to save
2. Close Notepad

## 7.4 Verify the file is correct

In Anaconda Prompt:

```
python -c "import nlpa_chat; print('OK')"
```

You should see `OK` printed.

**If you see an error** like `SyntaxError` or `IndentationError`,
the paste got mangled. Delete the file and try again:

```
del nlpa_chat.py
notepad nlpa_chat.py
```

Then re-paste the code above carefully.

## Phase 7 complete when...

- File `nlpa_chat.py` exists in your lab folder
- `python -c "import nlpa_chat; print('OK')"` prints `OK`

---

# Phase 8 — First run: verify everything works

Now we actually launch JupyterLab and run our first cells.

## 8.1 Launch JupyterLab

In Anaconda Prompt (in the lab folder, with `nlpa_2026`
activated):

```
jupyter lab
```

Three things happen:

1. Startup messages scroll for a few seconds
2. Your default browser opens automatically
3. You see the JupyterLab interface — file browser on the left,
   Launcher tab in the middle

**Important**: leave this Anaconda Prompt window OPEN. Closing
it kills the JupyterLab server.

## 8.2 Open the first lab notebook

1. In the file browser (left side), you should see all the lab
   files
2. Double-click `01a_tokenization_classical.ipynb`
3. The notebook opens as a new tab

## 8.3 Run the setup cells

Click on the first code cell in the notebook (usually near the
top). Press **Shift+Enter** to run it.

This runs the cell and moves the cursor to the next one.
Continue pressing **Shift+Enter** to run each cell in order.

Watch for:

- Green ✓ or `[N]:` (where N is a number) on the left of each
  cell — means it ran successfully
- Red error messages — means something went wrong (see
  Appendix A)

The very first cell that uses AI (probably called `chat()`)
takes 3-5 seconds because the AI model loads into your GPU
memory. This is one-time — later calls are instant.

## 8.4 Test the chat widget

When you reach a cell containing `chat()`, run it. A widget
appears with:

- A **Model** dropdown
- A blue **Ask** button
- An orange **Clear** button
- A text area
- An empty output box below

In the text area, type:

```
Hello! Please say one sentence back to confirm you're working.
```

Click **Ask**.

Wait a few seconds — you should see Qwen's response stream
into the output box word by word.

## Phase 8 complete when...

- JupyterLab opens in your browser
- You can open a lab notebook
- Cells run without errors
- The chat widget produces a real Qwen response

---

# Phase 9 — How to use the lab notebooks

Now you're set up. Here's how to actually work in the labs.

## 9.1 The teaching rhythm

Each lab follows a repeating pattern:

1. **Read** a short markdown cell explaining what we're about to do
2. **Run** a small code cell (usually 3-5 lines)
3. **Look** at the output
4. **Ask** Qwen about it using the chat widget
5. Move to the next code cell

Don't just run cells and move on. The learning happens when
you ask Qwen questions.

## 9.2 The chat widget

The chat widget is your AI teaching assistant. It sees:

- Every cell you've run this session
- The output of every cell
- Your questions

To use it:

- Type a question in the text area
- Click **Ask** (or press Ctrl+Enter as a shortcut)
- Watch the response stream in
- Click **Clear** to wipe the conversation

You can insert a chat widget **anywhere in the notebook** by
adding a new code cell with just `chat()` in it. Do this
whenever you want a conversation checkpoint after several
code cells.

## 9.3 Referring to specific cells

The most powerful feature: reference a specific cell by its
execution number (the `[N]:` on its left).

Examples of questions:

```
@cell 5 explain what this code does
```

```
@cell 5 why did the output show 12 tokens instead of 9?
```

```
@3 what happens if I change the regex pattern?
```

```
@last give me an edge case where this would fail
```

Special references:

- `@cell N` or `@N` — refers to cell number N
- `@last` — refers to the most recently run cell

When you use these, Qwen automatically sees the cell's code
and its output — you don't need to copy-paste them.

## 9.4 How to ask productive questions

Bad question: *"What is regex?"*
(Too generic — Qwen gives a textbook answer.)

Good question: *"@cell 5 why did `wasn't` become three tokens
instead of two?"*
(Specific — Qwen reasons about your actual code.)

Try these patterns:

- Ask **why**, not **what**
- Reference **specific outputs** you see
- Ask for **comparisons** ("compare cell 3 and cell 7")
- **Push back** if the answer seems wrong
- Ask for **edge cases** where the code would fail

## 9.5 Ending a session

When you're done:

1. Save your notebook: **Ctrl+S** or File → Save Notebook
2. Close the browser tab
3. Go back to the Anaconda Prompt where JupyterLab is running
4. Press **Ctrl+C** twice → answer `y` to shut down

Your notebook is saved automatically. Next session, just
reopen it and continue.

## 9.6 Reopening the lab later

For every subsequent session:

1. Open **Anaconda Prompt**
2. Activate the environment:
   ```
   conda activate nlpa_2026
   ```
3. Navigate to the lab folder:
   ```
   cd C:\Users\%USERNAME%\NLPA_LAB_2026
   ```
4. Launch JupyterLab:
   ```
   jupyter lab
   ```

Ollama runs automatically in the background — you don't need
to start it manually.

## Phase 9 complete when...

- You know how to run cells with Shift+Enter
- You've asked Qwen at least three different questions
- You know how to use `@cell N` references
- You know how to reopen the lab in the next session

---

# Appendix A — Troubleshooting

Common problems and their fixes.

## A.1 "conda: command not recognized"

**Cause**: you're in regular Command Prompt or PowerShell, not
Anaconda Prompt.

**Fix**: close the current window. Press Win, type
`anaconda prompt`, click it. Try again.

## A.2 "ollama: command not recognized"

**Cause**: Ollama was installed but the PATH didn't update in
your current Anaconda Prompt.

**Fix**: close the Anaconda Prompt and open a new one.

## A.3 Chat widget shows "You: ..." but no Qwen response

**Cause 1**: Ollama service stopped.

**Check**: in a new Anaconda Prompt:
```
curl http://localhost:11434
```
Should print "Ollama is running". If not, right-click the llama
icon in system tray → Quit. Then start Ollama from the Start
menu.

**Cause 2**: model not loaded, first request is slow.

**Fix**: wait 10-15 seconds. First response after starting is
slower because the model loads into GPU memory.

## A.4 "CUDA error" or "PTX unsupported toolchain"

**Cause**: your NVIDIA driver is too old for the CUDA version
Ollama needs.

**Fix**: update your NVIDIA driver.

1. Go to **https://www.nvidia.com/en-us/drivers/**
2. Select your GPU (Product Type: GeForce; Product Series:
   your card's series; Product: your specific model)
3. Download the latest **Game Ready Driver**
4. Run the installer, choose **Custom (Advanced)** → check
   **Perform a clean installation**
5. Reboot after install

Verify with:
```
nvidia-smi
```
The CUDA Version at the top-right should be 12.6 or higher.

## A.5 "Access denied" when deleting files

**Cause**: file is currently in use or has restricted
permissions.

**Fix**: close any programs that might be using it. If it's a
protected system file, don't delete it — leave it alone.

## A.6 "Import Error" in JupyterLab

**Cause**: you're not in the `nlpa_2026` environment when you
launched Jupyter.

**Check**: in the Anaconda Prompt running JupyterLab, your
prompt should show `(nlpa_2026)`.

**Fix**: press Ctrl+C twice in that Anaconda Prompt to stop
JupyterLab. Then:
```
conda activate nlpa_2026
jupyter lab
```

## A.7 Widget renders twice

**Cause**: cell was rendered from a previous run and current
run stacked on top.

**Fix**: click the cell → from top menu **Edit → Clear Outputs
of Selected Cells** → re-run the cell.

## A.8 JupyterLab won't launch — "port already in use"

**Cause**: an old JupyterLab is still running somewhere.

**Fix**: in Anaconda Prompt:
```
jupyter lab --port=8889
```
This uses a different port. Or restart your laptop to clear
all previous sessions.

## A.9 Downloads keep failing during setup

**Cause**: slow or unstable internet.

**Fix**: retry the failed command. All the setup commands
resume from where they stopped:

- `ollama pull ...` — resumes from last blob
- `pip install ...` — retries failed packages
- `python setup_data.py` — skips what's already downloaded

Just re-run the same command until it completes.

## A.10 "No module named nlpa_chat"

**Cause**: the notebook can't find `nlpa_chat.py`.

**Fix**: verify `nlpa_chat.py` is in the same folder as the
notebook. In Anaconda Prompt:
```
dir C:\Users\%USERNAME%\NLPA_LAB_2026\nlpa_chat.py
```
If the file isn't there, redo Phase 7.

---

# Appendix B — Freeing your GPU for training

The AI model uses about 5 GB of your GPU's memory while it's
loaded. If you want to train your own PyTorch model on the
same laptop, you'll want that memory back.

## B.1 Free the GPU with one command

Create a script `free-gpu.ps1` in your lab folder. In Anaconda
Prompt:

```
notepad free-gpu.ps1
```

Paste this content:

```powershell
$models = @("qwen2.5-coder:7b", "qwen2.5-coder:1.5b", "nomic-embed-text:latest")
foreach ($m in $models) {
    $body = '{"model":"' + $m + '","keep_alive":0}'
    Invoke-RestMethod -Uri "http://localhost:11434/api/generate" `
                      -Method Post -Body $body -ContentType "application/json" | Out-Null
}
Write-Host "Ollama models evicted. Current GPU status:" -ForegroundColor Green
nvidia-smi --query-gpu=memory.used,memory.free --format=csv
```

Save with Ctrl+S and close Notepad.

## B.2 Run it whenever you need the GPU

```
powershell -ExecutionPolicy Bypass -File free-gpu.ps1
```

You'll see a green message and your current GPU memory usage.
The AI is now unloaded from GPU memory.

**Note**: next time you ask the chat widget a question, the
model auto-reloads into GPU memory. Free-gpu just means "let it
go for now; reload later if needed."

## B.3 When to use this

- Before running a heavy PyTorch training job
- If Windows warns you're low on GPU memory
- Never needed if you're only doing lab work

---

# You're done

If you completed all 9 phases, you have:

- A local AI model running on your laptop
- A Python environment with all NLP tools installed
- Working JupyterLab notebooks
- A chat widget that lets Qwen see your code and outputs

Now open `01a_tokenization_classical.ipynb` and begin the
first lab.

---

**Questions during lab?** Ask Qwen first — often faster than
the instructor. Ask the instructor if Qwen doesn't help.

**Report bugs** in this guide: tell your instructor or open an
issue at the GitHub repository.

**Version**: 1.0 — 2026-07-02
**Maintainer**: Dr. P.V.V. Kishore, KLEF
