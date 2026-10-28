# LP3 Practical Codes

A collection of practical exercises for Design and Analysis of Algorithms (DAA), Information Retrieval (IR), Cyber Security and Digital Forensics (CSDF), and Machine Learning (ML). The repository contains standalone Python scripts, Java programs, and Jupyter notebooks; it is not one application and has no single build command.

## Contents

| Folder | Topics | How to run |
|---|---|---|
| [`CSDF CODES/`](CSDF%20CODES/) | CAPTCHA generation, email-header parsing, log analysis, and disk/partition recovery demonstrations | Python 3; some scripts also need Pillow or Linux forensic utilities |
| [`DAA CODES/`](DAA%20CODES/) | Knapsack, Huffman coding, N-Queens, and Tower of Hanoi source | Java JDK (`javac` and `java`) |
| [`IR CODES/`](IR%20CODES/) | Cosine similarity, MapReduce counting, PageRank, stop-word removal, and topic-sensitive PageRank | Python 3 standard library |
| [`ML Codes/`](ML%20Codes/) | Classification, regression, an artificial neural network, and gradient descent | Jupyter and the Python ML packages; most notebooks need datasets that are not included |

## Requirements

- Python 3 for the Python examples and notebooks.
- A Java Development Kit (JDK) for the Java examples.
- JupyterLab or Jupyter Notebook to open the `.ipynb` files.
- Additional packages and data are listed in the relevant sections below.

## Quick start on Linux

Open a terminal, install the basic tools if needed, and move to the repository root:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip openjdk-17-jdk
cd "/path/to/lp3-practical-codes"
```

Check that the tools are available:

```bash
python3 --version
javac -version
java -version
```

Run a standard-library Python example directly from the repository root:

```bash
python3 "IR CODES/CosineSimiliarity.py"
```

Run a Java program from the root without placing compiled `.class` files in the repository:

```bash
mkdir -p /tmp/lp3-java-build
javac -d /tmp/lp3-java-build "DAA CODES/FractionalKnapsack.java"
java -cp /tmp/lp3-java-build FractionalKnapsack
```

Replace `FractionalKnapsack` with `KnapsackDP`, `GreedyHuffmanEncoding`, or `NQueens` to compile and run those programs. Each program prompts for its input. Paths with spaces are quoted because the folder names contain spaces.

## Folder guides

### `CSDF CODES/`

| File | What it does | Requirements and notes |
|---|---|---|
| `Captcha.py` | Creates a six-character CAPTCHA image, displays it, and asks for the text. | On Debian/Ubuntu, install Pillow with `sudo apt install python3-pil`; alternatively install it in an active virtual environment with `python -m pip install pillow`. Run with `python3 "CSDF CODES/Captcha.py"`. It writes `captcha.png` in the terminal's current directory (overwriting a file of that name) and tries to open an image viewer. |
| `EmailHeader.py` | Parses and prints fields and routing IP addresses from a sample email header embedded in the script. | Python standard library; no input file or third-party package required. Run with `python3 "CSDF CODES/EmailHeader.py"`. |
| `LogCapture&EventCorrelation.py` | Creates sample `system.log`, parses its events, groups them by IP, and flags repeated failed logins. | Python standard library. Run with `python3 "CSDF CODES/LogCapture&EventCorrelation.py"`. It creates or overwrites `system.log` in the current directory. |
| `FileRecovery.py` | Makes a disk image, lists deleted-file entries, and extracts a selected inode. | Linux utilities: `lsblk`, `dd`, and Sleuth Kit (`fls`, `istat`, `icat`). Run only on media you own or are authorized to examine. See the recovery safety notes below. |
| `PartitionRecovery.py` | Displays block-device information and launches `fdisk` and TestDisk to inspect a selected device. | Linux utilities: `lsblk`, `fdisk`, `sudo`, and `testdisk`. It is an interactive recovery tool, not a read-only guarantee. See the recovery safety notes below. |
| `captcha.png` | Sample CAPTCHA image kept with the exercises. | The script saves its output relative to the current directory, not necessarily beside the script. |

To install the optional Linux recovery utilities on Debian/Ubuntu:

```bash
sudo apt install sleuthkit testdisk
```

`lsblk`, `fdisk`, and `dd` are commonly provided by the base Linux installation. Install missing tools with your distribution's package manager.

**Disk recovery safety:** Work from a copy or forensic image whenever possible, verify device paths carefully, and save output to a different drive with sufficient free space. `FileRecovery.py` opens the chosen image and recovered-file paths for writing, so an existing file at either path can be overwritten. `PartitionRecovery.py` invokes `sudo` and TestDisk; do not choose a write/repair operation unless you intend to change the device and have a verified backup. Never experiment on a disk containing important data.

### `DAA CODES/`

| File | What it does | Notes |
|---|---|---|
| `FractionalKnapsack.java` | Greedy fractional knapsack, sorting items by value-to-weight ratio. | Compile and run as `FractionalKnapsack` using the Linux Java instructions above. |
| `KnapsackDP.java` | 0/1 knapsack using dynamic programming; prints the maximum value and selected items. | Compile and run as `KnapsackDP`. |
| `GreedyHuffmanEncoding.java` | Builds a Huffman tree, displays codes, and demonstrates encoding and decoding entered text. | Compile and run as `GreedyHuffmanEncoding`. |
| `NQueens.java` | Solves N-Queens by backtracking with the first queen fixed at the top-left square. | Compile and run as `NQueens`. Because of that fixed starting position, it may report no solution for values that have no solution under this constraint. |
| `TowerOfHanoi.java` | Contains commented-out examples for iterative Fibonacci, recursive Fibonacci, and Tower of Hanoi. | The source is currently entirely inside comments, so it does not define a runnable `TowerOfHanoi` class. Uncomment or extract the desired example before compiling it. |
| `*.class` | Previously compiled Java bytecode files. | Compile from the `.java` source instead; the checked-in `.class` files may not match the current source. |

The Java examples use only the JDK. The folder's `.gitignore` excludes generated `.class` files.

### `IR CODES/`

All five scripts use Python's standard library. Run any one from the repository root with `python3 "IR CODES/<filename>.py"`:

| File | What it does |
|---|---|
| `CosineSimiliarity.py` | Compares two entered text strings using word-frequency cosine similarity. The filename uses the spelling `Similiarity`. |
| `MapReduce.py` | Demonstrates map, shuffle/group, and reduce phases by counting alphabetic characters in an embedded sample string. |
| `PageRankAlgo.py` | Calculates PageRank for a small directed graph defined in the script and prints the ranking. |
| `StopWordRemoval.py` | Removes a small built-in set of stop words from entered text. |
| `TopicPageRank.py` | Parses embedded XML, builds a directed graph, and calculates PageRank personalized to the `AI` topic. |

### `ML Codes/`

These are notebooks rather than command-line scripts. Install Jupyter and the common data-science packages in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn
jupyter lab
```

Then open the notebook from the Jupyter file browser. Or launch a specific notebook from the repository root:

```bash
jupyter lab "ML Codes/GradientDescent.ipynb"
```

Install TensorFlow only for the neural-network notebook:

```bash
python -m pip install tensorflow
```

TensorFlow support depends on your Python version and Linux platform; use a compatible Python environment if installation fails. The other notebooks primarily use pandas and scikit-learn, with plotting libraries used in the regression notebook.

| Notebook | Exercise | Data needed |
|---|---|---|
| `DiabetesKNN.ipynb` | Diabetes classification using KNN with scaling and classification metrics. | `diabetes.csv`; the notebook expects an `Outcome` column. |
| `GradientDescent.ipynb` | Gradient descent on \(f(x)=(x+3)^2\). | No external dataset. |
| `KNN&SVM.ipynb` | Email spam classification using TF-IDF, KNN, and SVM. | `emails.csv` with `text` and `spam` columns (`0` for normal and `1` for spam). |
| `Linear&RandomForestRegression.ipynb` | Uber fare prediction using linear and random-forest regression. | `uber.csv`, placed in the notebook's working directory. |
| `NNClassifier.ipynb` | Customer churn prediction using a neural network with dropout and early stopping. | `Churn_Modelling.csv`; TensorFlow is also required. |

The CSV datasets are not included in this repository. Obtain data you are authorized to use and place it where the corresponding notebook expects it. In Jupyter, check the notebook's working directory if it cannot find a dataset.

## General usage notes

- Run one example at a time; each script or notebook is a separate practical exercise.
- Interactive Python and Java programs prompt for input in the terminal. Use valid numeric values where prompted.
- Some scripts create files in the current working directory. Check for existing files with the same name before running them.
- Notebooks retain cell outputs and execution order. Use **Restart Kernel and Run All Cells** for a clean run after placing required datasets.
- There is no shared application entry point, automated test suite, or dependency manifest in this repository.
